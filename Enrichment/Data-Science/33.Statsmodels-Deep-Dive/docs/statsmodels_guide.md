# Going Beyond Basic EDA with `statsmodels`

A concise guide showing how `statsmodels` complements `pandas` and `scipy.stats` to check assumptions, quantify uncertainty, explain correlations, and guard against false positives.

---

## 1. Richer Summary Stats & Normality Diagnostics

- **95% Confidence Intervals (`DescrStatsW`):** `df.describe()` gives point estimates (mean, std, quartiles), whereas `statsmodels.stats.weightstats.DescrStatsW` computes confidence intervals for the mean (`tconfint_mean()`):
  ```python
  from statsmodels.stats.weightstats import DescrStatsW

  dsw = DescrStatsW(df["weight_change"])
  ci_low, ci_high = dsw.tconfint_mean(alpha=0.05)
  ```
- **Normality Check (`sm.qqplot`):** Before relying on parametric tests, `sm.qqplot(df["weight_change"], line="s")` plots sample quantiles against a normal distribution. Straight points along the red line suggest normality; curved ends indicate skewness or heavy-tailed outliers.

---

## 2. Explaining Correlations via OLS Regression

Correlation ($r$) measures direction and strength, while **Ordinary Least Squares (OLS)** gives slopes, standard errors, $R^2$, and $p$-values:

```python
import statsmodels.formula.api as smf

simple_model = smf.ols("weight_change ~ weight2", data=df).fit()
multi_model = smf.ols("weight_change ~ weight2 + wtyrago + age", data=df).fit()
```

- **Structural Collinearity:** Because `weight_change = weight2 - wtyrago`, putting both `weight2` and `wtyrago` in the multiple regression pushes $R^2 \to 1.000$ (with slopes $\approx +1.0$ and $-1.0$), revealing a mathematical definition rather than an independent causal relationship—contrasting clearly with a weaker biological predictor such as `age`.

---

## 3. Group-Difference Confidence Intervals (`CompareMeans`)

`scipy.stats.ttest_ind` returns only the $t$-statistic and $p$-value. `CompareMeans` adds Welch degrees of freedom and a **95% confidence interval for the difference in means**:

```python
from statsmodels.stats.weightstats import CompareMeans, DescrStatsW

cm = CompareMeans(DescrStatsW(male), DescrStatsW(female))
t_stat, p_val, dof = cm.ttest_ind(usevar="unequal")
ci_low, ci_high = cm.tconfint_diff(alpha=0.05, usevar="unequal")
```

**Why it matters:** With large samples ($N > 10{,}000$), even a tiny difference (e.g., $0.3\text{ kg}$) yields a tiny $p$-value. Reporting the confidence interval distinguishes **statistical significance** ($p < 0.05$) from **practical significance** (the real-world size of the difference in kilograms).

---

## 4. Controlling False Positives (`multipletests`)

When repeating a random 50/50 split $1{,}000$ times under a true null hypothesis, roughly $5\%$ of tests still produce $p < 0.05$ purely by chance. Adjusting $p$-values prevents false discoveries:

```python
from statsmodels.stats.multitest import multipletests

reject_bh, p_bh, _, _ = multipletests(raw_p_values, alpha=0.05, method="fdr_bh")
reject_bonf, p_bonf, _, _ = multipletests(raw_p_values, alpha=0.05, method="bonferroni")
```

- **Benjamini–Hochberg (`fdr_bh`):** Controls the False Discovery Rate.
- **Bonferroni (`bonferroni`):** Controls the Family-Wise Error Rate ($\alpha / m$).
