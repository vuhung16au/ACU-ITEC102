# 33. Statsmodels Deep Dive: Diagnostics, OLS & Multiple Testing

A short, sharp enrichment project showing how **`statsmodels`** complements **Pandas** and **SciPy** (`scipy.stats.ttest_ind`) for assumption checking, uncertainty quantification, regression modelling, and multiple-testing control.

---

## Why Pair `statsmodels` with Pandas and SciPy?

While Pandas handles descriptive tables and SciPy runs core hypothesis tests, `statsmodels` adds deeper statistical diagnostics that strengthen analytical reports and reflections:

| Analytical Step | Basic Pandas / SciPy | `statsmodels` Upgrade | Insight Gained |
| :--- | :--- | :--- | :--- |
| **Summary Stats** | `df.describe()` | `DescrStatsW(...).tconfint_mean()` | 95% confidence intervals around each sample mean |
| **Assumption Check** | Histogram / skew | `sm.qqplot(series, line="s")` | Visual check for normality vs heavy-tailed outliers |
| **Correlations** | `df.corr()` / `pearsonr` | `smf.ols("y ~ x1 + x2 + x3", data=df).fit()` | $R^2$, slopes, $p$-values, and structural collinearity |
| **Group Comparison** | `stats.ttest_ind(..., equal_var=False)` | `CompareMeans(...).tconfint_diff()` | Welch degrees of freedom & 95% CI for mean difference |
| **Repeated Splits** | 1,000 raw $p$-values | `multipletests(p_values, method="fdr_bh")` | Separates true signal from ~5% random false positives |

---

## Project Structure

```text
33.Statsmodels-Deep-Dive/
├── .python-version
├── Makefile
├── pyproject.toml
├── main.py
├── README.md
├── QUICKSTART.md
├── docs/
│   └── statsmodels_guide.md
├── images/
│   ├── README.md
│   ├── 01_qqplot_and_mean_ci.png
│   └── 02_ols_and_multiple_testing.png
├── data/
│   └── aus_wellness_survey.csv
├── src/
│   ├── dataset.py
│   └── analysis.py
└── tests/
    └── test_analysis.py
```

---

## Key Results Summary (`N = 15,000`, `SEED = 42`)

1. **Confidence Intervals & Normality:** `DescrStatsW` gives tight 95% CIs (e.g., `weight_change` mean `-0.7685 kg`, 95% CI `[-0.8382, -0.6988]`), while `sm.qqplot` reveals heavy-tailed outliers in the extremes.
2. **OLS & Collinearity:** Simple OLS (`weight_change ~ weight2`) yields $R^2 = 0.0652$ ($\text{slope} = +0.0708$). Adding `wtyrago` (`weight_change ~ weight2 + wtyrago + age`) pushes $R^2 = 1.0000$ (`+1.0000` and `-1.0000`), exposing the exact mathematical definition `weight_change = weight2 - wtyrago`.
3. **Practical vs Statistical Significance:** `scipy.stats.ttest_ind` and `CompareMeans` agree identically ($t = -3.1822$, $p = 1.465 \times 10^{-3}$, $\text{df} = 11{,}580.9$), while the 95% CI `[-0.3833, -0.0911] kg` shows the actual group difference is modest (~`-0.24 kg`).
4. **Multiple Testing Control:** Across 1,000 random 50/50 splits, `64 / 1,000` tests fall below $p = 0.05$ by chance; `multipletests(..., method="fdr_bh")` and `"bonferroni"` reduce false positives to `0 / 1,000`.

Screenshots and diagnostic charts are saved in `images/`. See [QUICKSTART.md](QUICKSTART.md) to run it and [docs/statsmodels_guide.md](docs/statsmodels_guide.md) for code snippets.
