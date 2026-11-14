# Hypothesis Testing with SciPy: t-values, p-values, and Random Splits

This guide explains the statistical concepts demonstrated in **Project 32 (`32.SciPy-Statistical-EDA`)** using simple language for first-year computer science students.

---

## 1. Null and Alternative Hypotheses ($H_0$ and $H_1$)

Whenever we compare two groups (for example, male vs female participants in an Australian health survey), we start by framing two competing statements:

- **Null Hypothesis ($H_0$):** There is **no real difference** between the two group averages in the wider population. Any difference we see in our sample is just random noise.
- **Alternative Hypothesis ($H_1$):** There **is a real difference** between the two group averages.

We never "prove" $H_1$ with 100% certainty; instead, we measure how surprising our data would be **if $H_0$ were true**.

---

## 2. What is the t-value (t-statistic)?

The **t-value** measures how large the difference between two group means is relative to the spread (variability) and sample size of the data:

$$t = \frac{\bar{x}_1 - \bar{x}_2}{\text{Standard Error of the Difference}}$$

- **Sign ($+$ or $-$):** Shows direction (negative if Group 1 has a lower mean than Group 2).
- **Magnitude ($|t|$):** Larger $|t|$ means a stronger signal relative to noise.
- **Dimensionless:** Because it is divided by the standard error, a t-value has no units (unlike `kg` or `kg/cm`), which helps compare evidence across variables measured on different scales.

---

## 3. What is the p-value?

The **p-value** is the probability of observing a t-statistic at least as extreme as ours **assuming $H_0$ is true**.

- **Small p-value ($p < 0.05$):** Very unlikely to happen by chance alone $\rightarrow$ **reject $H_0$** (statistically significant).
- **Large p-value ($p \ge 0.05$):** Quite plausible by random chance alone $\rightarrow$ **do not reject $H_0$**.

> **Common pitfall:** A small p-value does **not** mean a huge real-world effect. With very large samples ($N > 10{,}000$), even a small difference (e.g., $0.41\text{ kg}$ over 12 weeks) can produce $p < 0.000001$. Always report both **statistical significance** ($p$-value) and **practical significance** (the actual difference in `kg`).

---

## 4. Levene's Test and Welch's t-test in SciPy

Standard Student's t-test assumes both groups have equal variance. In real-world health surveys, that assumption often fails.

1. Check variance equality with **Levene's test**:
   ```python
   from scipy import stats

   levene_result = stats.levene(male, female)
   ```
   If `levene_result.pvalue < 0.05`, the group variances differ significantly.

2. Run **Welch's independent t-test** by setting `equal_var=False`:
   ```python
   test_result = stats.ttest_ind(male, female, equal_var=False)
   print(test_result.statistic, test_result.pvalue)
   ```
   Welch's t-test adjusts the degrees of freedom automatically so the test remains accurate even when variances and group sizes differ.

---

## 5. Why Test Random Splits (and 1,000 Monte Carlo Splits)?

Suppose we take the exact same cleaned `weight_change` column, shuffle it randomly, and split it into two equal halves (`Group 1` and `Group 2`):

- Because both halves come from the **same distribution**, $H_0$ is genuinely true!
- A single random split normally yields $p > 0.05$.
- If we repeat this random split **1,000 times**, roughly **5%** of the tests will still give $p < 0.05$ purely by chance.
- Plotting $-\log_{10}(p\text{-value})$ makes tiny p-values easy to visualise: the significance threshold $p = 0.05$ sits at $-\log_{10}(0.05) \approx 1.30$. Anything to the right of `1.30` is a **Type I error (false positive)**.
