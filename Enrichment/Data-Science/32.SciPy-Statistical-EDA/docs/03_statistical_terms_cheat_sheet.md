# Quick Statistics Cheat Sheet (Formulas & Key Terms)

A brief refresher on the core statistical terms and mathematical formulas used in **Project 32 (`32.SciPy-Statistical-EDA`)**.

---

## 1. Hypotheses ($H_0$ and $H_1$) and Significance Level ($\alpha$)

| Term | Meaning | Typical Value / Rule |
| :--- | :--- | :--- |
| **Null Hypothesis ($H_0$)** | Assumes **no true difference** or **no relationship** ($\mu_1 = \mu_2$ or $r = 0$). | Baseline assumption tested against the data. |
| **Alternative Hypothesis ($H_1$)** | Assumes a **real difference** or **relationship** ($\mu_1 \neq \mu_2$ or $r \neq 0$). | Supported when $H_0$ is rejected. |
| **Significance Level ($\alpha$)** | Maximum acceptable probability of a **Type I error** (false positive: rejecting $H_0$ when $H_0$ is actually true). | Commonly $\alpha = 0.05$ ($5\%$). |

---

## 2. Sample Mean ($\bar{x}$) and Standard Deviation ($s$)

For $n$ observations $x_1, x_2, \dots, x_n$:

$$\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i \qquad \qquad s = \sqrt{\frac{1}{n - 1} \sum_{i=1}^{n} (x_i - \bar{x})^2}$$

- $\bar{x}$ describes the **centre** (average); $s$ describes the **spread** around the mean ($s^2$ is the sample variance).

---

## 3. Welch's $t$-statistic ($t$-value)

Used in `scipy.stats.ttest_ind(a, b, equal_var=False)` to compare two independent group means when variances may differ:

$$t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}$$

With Welch–Satterthwaite approximate degrees of freedom:

$$\nu \approx \frac{\left(\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}\right)^2}{\frac{(s_1^2 / n_1)^2}{n_1 - 1} + \frac{(s_2^2 / n_2)^2}{n_2 - 1}}$$

- **What it tells you:** How many standard errors apart the two means are.
- **Sign ($+/-$):** Shows which group mean is larger; **larger $|t|$** means stronger evidence against $H_0$.
- **Unit-free:** Unlike raw differences ($\text{kg}$ vs $\text{kg/cm}$), $t$ has no units.

---

## 4. The $p$-value

The probability of observing a test statistic at least as extreme as $|t_{\text{obs}}|$ **assuming $H_0$ is true** (two-sided test):

$$p = P\left(|T| \ge |t_{\text{obs}}| \;\middle|\; H_0\right) = 2 \cdot \left(1 - F_\nu(|t_{\text{obs}}|)\right)$$

where $F_\nu$ is the cumulative distribution function (CDF) of Student's $t$-distribution with $\nu$ degrees of freedom.

- **Decision rule:** If $p < \alpha$ (e.g. $p < 0.05$), **reject $H_0$**. Otherwise, **do not reject $H_0$**.
- **Reminder:** $p$-value is **not** the probability that $H_0$ is true, nor does it measure practical effect size.

---

## 5. Negative Log p-value ($-\log_{10}(p)$)

Used in our 1,000 random-split histogram so very small $p$-values are easy to compare visually:

$$y = -\log_{10}(p)$$

- $p = 0.05 \implies -\log_{10}(0.05) \approx 1.301$
- $p = 0.001 \implies -\log_{10}(0.001) = 3.0$
- Higher $-\log_{10}(p)$ means a smaller $p$-value (stronger apparent evidence against $H_0$).

---

## 6. Levene's Test ($W$-statistic)

Used via `scipy.stats.levene(a, b)` to check whether two (or more) groups have equal variances ($H_0: \sigma_1^2 = \sigma_2^2$).

Let $z_{ij} = |x_{ij} - \tilde{x}_i|$ be the absolute deviation from group $i$'s median $\tilde{x}_i$ (Brown–Forsythe default in SciPy):

$$W = \frac{(N - k)}{(k - 1)} \cdot \frac{\sum_{i=1}^{k} n_i (\bar{z}_i - \bar{z})^2}{\sum_{i=1}^{k} \sum_{j=1}^{n_i} (z_{ij} - \bar{z}_i)^2}$$

- If Levene's $p < 0.05$, variances differ significantly $\rightarrow$ use **Welch's $t$-test** (`equal_var=False`).

---

## 7. Correlation Coefficients: Pearson ($r$) and Spearman ($\rho$)

- **Pearson's $r$** (`scipy.stats.pearsonr`) measures **linear** association ($-1 \le r \le +1$):

  $$r = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n} (x_i - \bar{x})^2} \sqrt{\sum_{i=1}^{n} (y_i - \bar{y})^2}}$$

- **Spearman's $\rho$** (`scipy.stats.spearmanr`) applies Pearson's formula to the **ranks** $R(x_i), R(y_i)$, measuring **monotonic** relationships (robust to outliers). When all ranks are distinct:

  $$\rho = 1 - \frac{6 \sum_{i=1}^{n} d_i^2}{n(n^2 - 1)}, \qquad d_i = R(x_i) - R(y_i)$$

- **Significance test for correlation ($H_0: r = 0$):**

  $$t = \frac{r\sqrt{n - 2}}{\sqrt{1 - r^2}}, \qquad \text{df} = n - 2$$
