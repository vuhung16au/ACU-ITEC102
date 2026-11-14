# 32. SciPy Statistical EDA & Hypothesis Testing

An educational enrichment project for **ACU ITEC102** demonstrating a complete **Exploratory Data Analysis (EDA)** pipeline in Python with **`scipy.stats`** and **`seaborn`**.

Using a reproducible, synthetic **Australian National Health & Wellness Survey** dataset (12,000 participants across Sydney, Melbourne, Brisbane, Perth, Adelaide, Canberra, Hobart, and Darwin), this project walks step-by-step from raw dirty data to rigorous statistical testing, random split simulations, correlation matrices, and clear result interpretations.

---

## Learning Outcomes

By working through this project, you will learn how to:

1. **Generate and clean survey data** (`pandas` + `numpy`) by handling missing values, removing sentinel outliers (`999`, `-10`), and engineering derived features (`weight_change`, `weight_height_ratio`).
2. **Test equal-variance assumptions** using Levene's test (`scipy.stats.levene`).
3. **Compare two independent groups** using Welch's t-test (`scipy.stats.ttest_ind(..., equal_var=False)`) and interpret the **t-statistic** and **p-value**.
4. **Understand Type I errors (false positives)** by running a single random 50/50 split and a **1,000-iteration Monte Carlo random split** experiment, visualising $-\log_{10}(p\text{-value})$.
5. **Compare metrics across different units** (`kg` vs `kg/cm`) without falling into raw-magnitude traps.
6. **Build and test correlation matrices** using `scipy.stats.pearsonr` and `scipy.stats.spearmanr` (getting both $r$/$\rho$ and exact $p$-values).
7. **Visualise distributions and statistical findings** cleanly with **`seaborn`** (`histplot`, `boxplot`, `violinplot`, `heatmap`, `regplot`).

---

## Project Structure

```text
32.SciPy-Statistical-EDA/
├── .python-version                      # Pinned to Python 3.14
├── Makefile                             # setup, run, test, clean targets
├── pyproject.toml                       # uv / PEP 621 project configuration
├── main.py                              # End-to-end EDA & SciPy pipeline script
├── README.md                            # Project overview (this file)
├── QUICKSTART.md                        # Step-by-step setup & usage guide
├── docs/
│   ├── 01_hypothesis_testing_explained.md
│   └── 02_eda_and_correlation.md
├── images/                              # Generated Seaborn charts & screenshots
│   ├── README.md
│   ├── 01_weight_change_by_sex.png
│   ├── 02_random_splits_neg_log10_p.png
│   ├── 03_weight_height_ratio_by_sex.png
│   └── 04_correlation_matrix_heatmap.png
├── data/                                # Generated raw & cleaned CSV datasets
├── src/
│   ├── data_generator.py                # Synthetic Australian survey generator
│   ├── eda_cleaner.py                   # EDA inspection, filtering & feature engineering
│   ├── stats_analysis.py                # SciPy statistical tests & interpretations
│   └── visualizer.py                    # Seaborn plotting functions
└── tests/
    └── test_pipeline.py                 # Automated unit & end-to-end tests
```

---

## Pipeline Walkthrough & Key Results

Running `main.py` executes eight structured stages (with `SEED = 42`):

1. **Synthetic Data Generation:** Creates `12,000` Australian participant records with ~2.5% injected missing values and sentinel outliers.
2. **EDA & Cleaning:** Drops `203` rows with missing fields and `103` out-of-range rows, leaving `11,694` clean records. Computes `weight_change = weight2 - weight1` and `weight_height_ratio = weight2 / htm3`.
3. **Male vs Female Weight Change (Welch's t-test):**
   - Male (`sex == 1`, $n = 4{,}542$): mean $= -1.0290\text{ kg}$, std $= 4.5145\text{ kg}$
   - Female (`sex == 2`, $n = 7{,}152$): mean $= -0.6233\text{ kg}$, std $= 3.9765\text{ kg}$
   - Levene's test $p = 5.73 \times 10^{-19} < 0.05$ $\rightarrow$ variances differ, justifying Welch's t-test.
   - Welch's $t = -4.9573$, $p = 7.28 \times 10^{-7} < 0.05$ $\rightarrow$ **reject $H_0$**.
4. **Single Random 50/50 Split:** Splits the cleaned `weight_change` values randomly into two groups of `5,847` participants. Welch's t-test gives $t = -0.9543$, $p = 0.3400 \ge 0.05$ $\rightarrow$ **do not reject $H_0$**, as expected when comparing two halves of the same population.
5. **1,000 Random Splits (Monte Carlo):** Repeats the 50/50 split 1,000 times and plots $-\log_{10}(p\text{-value})$. Roughly **6.1%** (close to the theoretical **5%**) of random splits still fall below $p = 0.05$ purely by chance, illustrating the Type I error rate.
6. **Unit Comparison (`weight_height_ratio`):** Compares `weight2 / htm3` (`kg/cm`) between males ($0.4848$) and females ($0.4224$). Demonstrates why raw mean differences in different units (`0.4057 kg` vs `0.0624 kg/cm`) cannot be compared directly, while dimensionless $t$-statistics and $p$-values can.
7. **Correlation Matrix & SciPy p-values:** Computes pairwise Pearson $r$ and Spearman $\rho$ correlations across 8 numeric variables, highlighting strong links (`weight1` vs `weight2`: $r = +0.962$; `weekly_exercise_hrs` vs `daily_steps`: $r = +0.871$) and negative association (`weekly_exercise_hrs` vs `weight_change`: $r = -0.182$, $p = 1.93 \times 10^{-87}$).
8. **Seaborn Visualisations:** Generates four annotated PNG charts saved in the `images/` directory (screenshots and plots can be viewed in `images/`).

---

## Further Reading

- [Hypothesis Testing Explained](docs/01_hypothesis_testing_explained.md)
- [EDA Pipeline & Correlation Matrices](docs/02_eda_and_correlation.md)
- [Quick Statistics Cheat Sheet (Formulas & Key Terms)](docs/03_statistical_terms_cheat_sheet.md)
- [Quickstart Guide](QUICKSTART.md)
