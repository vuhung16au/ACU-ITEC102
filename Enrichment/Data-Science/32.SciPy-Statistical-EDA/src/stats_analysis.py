"""Core SciPy statistical analysis and interpretation utilities.

Demonstrates:
  - Levene's test for equality of variances (``scipy.stats.levene``)
  - Welch's independent two-sample t-test (``scipy.stats.ttest_ind``)
  - Single random 50/50 split sanity check
  - 1,000-iteration Monte Carlo random split simulation & -log10(p-value)
  - Unit-scale comparison (``weight_change`` vs ``weight_height_ratio``)
  - Pairwise Pearson and Spearman correlation matrices with SciPy p-values
"""

from dataclasses import dataclass
import numpy as np
import pandas as pd
from scipy import stats


@dataclass
class GroupComparisonResult:
    """Results from comparing two independent groups using Levene + Welch's t-test."""

    metric_name: str
    unit: str
    group_a_name: str
    group_b_name: str
    n_a: int
    mean_a: float
    std_a: float
    n_b: int
    mean_b: float
    std_b: float
    mean_diff: float
    levene_stat: float
    levene_pvalue: float
    t_stat: float
    p_value: float
    alpha: float

    @property
    def variances_unequal(self) -> bool:
        """Return True when Levene's test indicates significantly different variances."""
        return self.levene_pvalue < self.alpha

    @property
    def is_significant(self) -> bool:
        """Return True when Welch's t-test rejects the null hypothesis at alpha."""
        return self.p_value < self.alpha


@dataclass
class RandomSplitResult:
    """Results from a single random 50/50 split Welch's t-test."""

    group1_size: int
    group2_size: int
    group1_mean: float
    group2_mean: float
    t_stat: float
    p_value: float
    alpha: float

    @property
    def is_significant(self) -> bool:
        """Return True if the random split happened to yield p < alpha."""
        return self.p_value < self.alpha


@dataclass
class MonteCarloSplitResult:
    """Results from repeating random 50/50 split t-tests many times."""

    n_iterations: int
    p_values: np.ndarray
    negative_log10_p: np.ndarray
    proportion_below_alpha: float
    smallest_p_value: float
    alpha: float


@dataclass
class CorrelationAnalysisResult:
    """Pearson and Spearman correlation matrices alongside SciPy p-value matrices."""

    columns: list[str]
    pearson_r: pd.DataFrame
    pearson_p: pd.DataFrame
    spearman_r: pd.DataFrame
    spearman_p: pd.DataFrame
    notable_pairs: list[dict[str, float | str]]


def compare_two_groups(
    group_a: pd.Series | np.ndarray,
    group_b: pd.Series | np.ndarray,
    metric_name: str,
    unit: str,
    group_a_name: str = "Male (sex == 1)",
    group_b_name: str = "Female (sex == 2)",
    alpha: float = 0.05,
) -> GroupComparisonResult:
    """Compare two independent samples using Levene's test and Welch's t-test.

    Why both tests?
      1. ``stats.levene`` checks whether the two groups have equal spread (variance).
         If Levene's p-value < 0.05, equal variance is violated.
      2. ``stats.ttest_ind(..., equal_var=False)`` runs Welch's t-test, which does
         not assume equal variances and is safer in real-world EDA.
    """
    arr_a = np.asarray(group_a, dtype=float)
    arr_b = np.asarray(group_b, dtype=float)

    levene_res = stats.levene(arr_a, arr_b)
    ttest_res = stats.ttest_ind(arr_a, arr_b, equal_var=False)

    mean_a = float(np.mean(arr_a))
    mean_b = float(np.mean(arr_b))

    return GroupComparisonResult(
        metric_name=metric_name,
        unit=unit,
        group_a_name=group_a_name,
        group_b_name=group_b_name,
        n_a=len(arr_a),
        mean_a=mean_a,
        std_a=float(np.std(arr_a, ddof=1)),
        n_b=len(arr_b),
        mean_b=mean_b,
        std_b=float(np.std(arr_b, ddof=1)),
        mean_diff=mean_a - mean_b,
        levene_stat=float(levene_res.statistic),
        levene_pvalue=float(levene_res.pvalue),
        t_stat=float(ttest_res.statistic),
        p_value=float(ttest_res.pvalue),
        alpha=alpha,
    )


def run_single_random_split(
    values: pd.Series | np.ndarray,
    seed: int = 42,
    alpha: float = 0.05,
) -> RandomSplitResult:
    """Randomly split one array into two equal halves and run Welch's t-test.

    Because both halves come from the exact same underlying population, the null
    hypothesis (no true difference) is true by construction. We generally expect
    a p-value > 0.05.
    """
    arr = np.asarray(values, dtype=float)
    half = len(arr) // 2

    rng = np.random.default_rng(seed)
    shuffled_indices = rng.permutation(len(arr))
    group1 = arr[shuffled_indices[:half]]
    group2 = arr[shuffled_indices[half : half * 2]]

    test_res = stats.ttest_ind(group1, group2, equal_var=False)

    return RandomSplitResult(
        group1_size=len(group1),
        group2_size=len(group2),
        group1_mean=float(np.mean(group1)),
        group2_mean=float(np.mean(group2)),
        t_stat=float(test_res.statistic),
        p_value=float(test_res.pvalue),
        alpha=alpha,
    )


def run_monte_carlo_random_splits(
    values: pd.Series | np.ndarray,
    n_iterations: int = 1000,
    seed: int = 42,
    alpha: float = 0.05,
) -> MonteCarloSplitResult:
    """Repeat random 50/50 split t-tests ``n_iterations`` times.

    This experiment illustrates what a p-value really means: even when there is
    NO real difference between groups, roughly 5% (alpha = 0.05) of tests will
    still produce p < 0.05 purely by random chance (Type I error / false positive).
    """
    arr = np.asarray(values, dtype=float)
    half = len(arr) // 2
    rng = np.random.default_rng(seed)

    p_values = np.empty(n_iterations, dtype=float)
    for idx in range(n_iterations):
        shuffled_indices = rng.permutation(len(arr))
        group1 = arr[shuffled_indices[:half]]
        group2 = arr[shuffled_indices[half : half * 2]]
        p_values[idx] = stats.ttest_ind(group1, group2, equal_var=False).pvalue

    # Guard against exact zero before taking -log10
    safe_p = np.clip(p_values, 1e-300, 1.0)
    negative_log10_p = -np.log10(safe_p)

    return MonteCarloSplitResult(
        n_iterations=n_iterations,
        p_values=p_values,
        negative_log10_p=negative_log10_p,
        proportion_below_alpha=float(np.mean(p_values < alpha)),
        smallest_p_value=float(np.min(p_values)),
        alpha=alpha,
    )


def compute_correlation_analysis(
    df: pd.DataFrame,
    columns: list[str] | None = None,
) -> CorrelationAnalysisResult:
    """Compute Pearson and Spearman correlation & p-value matrices using SciPy.

    Unlike ``DataFrame.corr()``, using ``scipy.stats.pearsonr`` and
    ``scipy.stats.spearmanr`` provides both the correlation strength ``r`` (or ``rho``)
    AND the statistical significance ``p-value`` for every variable pair.
    """
    if columns is None:
        columns = [
            "age",
            "htm3",
            "weight1",
            "weight2",
            "weight_change",
            "weight_height_ratio",
            "weekly_exercise_hrs",
            "daily_steps",
        ]

    pearson_r = pd.DataFrame(np.eye(len(columns)), index=columns, columns=columns)
    pearson_p = pd.DataFrame(np.zeros((len(columns), len(columns))), index=columns, columns=columns)
    spearman_r = pd.DataFrame(np.eye(len(columns)), index=columns, columns=columns)
    spearman_p = pd.DataFrame(np.zeros((len(columns), len(columns))), index=columns, columns=columns)

    pair_records: list[dict[str, float | str]] = []

    for i, col_x in enumerate(columns):
        for j in range(i + 1, len(columns)):
            col_y = columns[j]
            x_vals = df[col_x].to_numpy(dtype=float)
            y_vals = df[col_y].to_numpy(dtype=float)

            pr, pp = stats.pearsonr(x_vals, y_vals)
            sr, sp = stats.spearmanr(x_vals, y_vals)

            pearson_r.loc[col_x, col_y] = pearson_r.loc[col_y, col_x] = float(pr)
            pearson_p.loc[col_x, col_y] = pearson_p.loc[col_y, col_x] = float(pp)
            spearman_r.loc[col_x, col_y] = spearman_r.loc[col_y, col_x] = float(sr)
            spearman_p.loc[col_x, col_y] = spearman_p.loc[col_y, col_x] = float(sp)

            pair_records.append(
                {
                    "var_1": col_x,
                    "var_2": col_y,
                    "pearson_r": float(pr),
                    "pearson_p": float(pp),
                    "spearman_r": float(sr),
                    "spearman_p": float(sp),
                }
            )

    # Sort by absolute Pearson correlation descending to highlight strongest links
    notable_pairs = sorted(pair_records, key=lambda item: abs(float(item["pearson_r"])), reverse=True)

    return CorrelationAnalysisResult(
        columns=columns,
        pearson_r=pearson_r,
        pearson_p=pearson_p,
        spearman_r=spearman_r,
        spearman_p=spearman_p,
        notable_pairs=notable_pairs,
    )


def format_group_interpretation(result: GroupComparisonResult) -> str:
    """Create a plain-English statistical interpretation for a two-group test."""
    levene_msg = (
        f"Levene's test p-value is {result.levene_pvalue:.3e} (< {result.alpha}), "
        "indicating unequal group variances, so Welch's t-test is the right choice."
        if result.variances_unequal
        else f"Levene's test p-value is {result.levene_pvalue:.4f} (>= {result.alpha}), "
        "indicating roughly equal variances; Welch's t-test remains safe and valid."
    )

    decision = (
        f"Since p = {result.p_value:.3e} < {result.alpha}, we REJECT H0. "
        f"There is a statistically significant difference in {result.metric_name} between "
        f"{result.group_a_name} and {result.group_b_name}."
        if result.is_significant
        else f"Since p = {result.p_value:.4f} >= {result.alpha}, we DO NOT reject H0. "
        f"There is no statistically significant difference in {result.metric_name}."
    )

    return (
        f"H0: There is no significant difference in average {result.metric_name} between groups.\n"
        f"H1: There is a significant difference in average {result.metric_name} between groups.\n"
        f"- {result.group_a_name}: n = {result.n_a:,}, mean = {result.mean_a:.4f} {result.unit}, "
        f"std = {result.std_a:.4f} {result.unit}\n"
        f"- {result.group_b_name}: n = {result.n_b:,}, mean = {result.mean_b:.4f} {result.unit}, "
        f"std = {result.std_b:.4f} {result.unit}\n"
        f"- Raw difference (A - B): {result.mean_diff:.4f} {result.unit}\n"
        f"- {levene_msg}\n"
        f"- Welch's t-statistic: {result.t_stat:.4f}, p-value: {result.p_value:.3e}\n"
        f"- Conclusion: {decision}"
    )
