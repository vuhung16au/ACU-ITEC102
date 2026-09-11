"""Addressing Fairness and Bias: Auditing Algorithmic Equity & Disparate Impact.

This module introduces first-year data science students to algorithmic fairness:
- Quantifying algorithmic bias using Demographic Parity and Disparate Impact Ratio (DIR).
- Applying the EEOC / 80% (Four-Fifths) Adverse Impact Rule.
- Understanding historical, representation, and proxy biases.
- Implementing post-processing threshold adjustments to mitigate bias.
"""

import pandas as pd
import numpy as np


def create_scholarship_applicant_data() -> pd.DataFrame:
    """Creates a simulated cohort of university scholarship applicants with historical bias."""
    np.random.seed(102)
    n = 100

    # Two demographic groups: Group A (Privileged / Historical Majority, 60%), Group B (Unprivileged, 40%)
    groups = np.random.choice(["Group A", "Group B"], size=n, p=[0.60, 0.40])

    # Raw potential / merit is equally distributed between groups
    merit_score = np.random.normal(loc=75, scale=10, size=n).clip(45, 99).round(1)

    # Historical systemic bias: Group A applicants have higher extracurricular prestige points
    # due to historic access to elite coaching programs
    prestige_boost = np.where(groups == "Group A", 6.5, 0.0)
    composite_score = (merit_score + prestige_boost).round(1)

    df = pd.DataFrame({
        "applicant_id": [f"APP-{3000 + i}" for i in range(n)],
        "demographic_group": groups,
        "true_merit": merit_score,
        "composite_score": composite_score,
    })
    return df


def evaluate_naive_selection(df: pd.DataFrame, cutoff: float = 80.0) -> pd.DataFrame:
    """Applies a single naive threshold without fairness auditing."""
    print("--- 1. Naive Model Selection (Single Uniform Cutoff) ---")
    results = df.copy()
    results["awarded"] = results["composite_score"] >= cutoff

    print(f"Selection Cutoff: Composite Score >= {cutoff}")
    print(f"Total Scholarships Awarded: {results['awarded'].sum()} / {len(results)}")
    return results


def audit_fairness_and_disparate_impact(df: pd.DataFrame) -> tuple[float, float, float]:
    """Calculates Group Acceptance Rates and the Disparate Impact Ratio (DIR)."""
    print("\n--- 2. Quantitative Fairness Audit (The 80% Rule) ---")

    # Group-level selection rates
    group_summary = df.groupby("demographic_group")["awarded"].agg(["count", "sum", "mean"])
    group_summary.columns = ["Total Applicants", "Awarded Count", "Acceptance Rate"]
    group_summary["Acceptance Rate (%)"] = (group_summary["Acceptance Rate"] * 100).round(1)
    print(group_summary)

    rate_a = group_summary.loc["Group A", "Acceptance Rate"]
    rate_b = group_summary.loc["Group B", "Acceptance Rate"]

    # Disparate Impact Ratio (DIR) = Unprivileged Rate / Privileged Rate
    dir_ratio = rate_b / rate_a if rate_a > 0 else 1.0

    print(f"\nGroup A (Privileged) Rate: {rate_a * 100:.1f}%")
    print(f"Group B (Unprivileged) Rate: {rate_b * 100:.1f}%")
    print(f"Disparate Impact Ratio (DIR): {dir_ratio:.3f}")

    if dir_ratio < 0.80:
        print("[FAIRNESS VIOLATION] Adverse Impact Detected (DIR < 0.80) under the 80% Rule.")
        print("Group B applicants face systemic disadvantage despite equal true merit distributions.")
    else:
        print("[FAIRNESS PASS] Disparate Impact Ratio satisfies equity standard (DIR >= 0.80).")

    return rate_a, rate_b, dir_ratio


def mitigate_bias_threshold_adjustment(df: pd.DataFrame) -> pd.DataFrame:
    """Mitigates bias via post-processing group-calibrated decision thresholds."""
    print("\n--- 3. Bias Mitigation: Group Threshold Calibration ---")
    mitigated = df.copy()

    # Calibrate thresholds to equalize opportunity and account for prestige boost
    # Group A: 80.0, Group B: 74.0 (adjusting for the 6.5 pt prestige disparity)
    def fair_selection(row):
        if row["demographic_group"] == "Group A":
            return row["composite_score"] >= 80.0
        else:
            return row["composite_score"] >= 74.0

    mitigated["awarded"] = mitigated.apply(fair_selection, axis=1)

    print("Post-Mitigation Group Acceptance Rates:")
    post_summary = mitigated.groupby("demographic_group")["awarded"].agg(["count", "sum", "mean"])
    post_summary.columns = ["Total Applicants", "Awarded Count", "Acceptance Rate"]
    post_summary["Acceptance Rate (%)"] = (post_summary["Acceptance Rate"] * 100).round(1)
    print(post_summary)

    new_rate_a = post_summary.loc["Group A", "Acceptance Rate"]
    new_rate_b = post_summary.loc["Group B", "Acceptance Rate"]
    new_dir = new_rate_b / new_rate_a

    print(f"\nNew Disparate Impact Ratio (DIR): {new_dir:.3f}")
    if new_dir >= 0.80:
        print("[FAIRNESS RESTORED] Mitigation successful: Adverse impact eliminated.")
    return mitigated


def run_exercises():
    """Hands-on student exercises on fairness metrics."""
    print("\n--- 4. Student Practice Exercises ---")

    # Tech internship screening scenario
    hiring_df = pd.DataFrame({
        "candidate_id": [f"C{i}" for i in range(1, 11)],
        "gender": ["Male", "Male", "Male", "Male", "Male", "Female", "Female", "Female", "Female", "Female"],
        "interview_score": [85, 78, 92, 88, 70, 79, 74, 86, 68, 72]
    })
    print("Internship Applicant Interview Scores:")
    print(hiring_df)

    # Initial naive cutoff: interview_score >= 80
    hiring_df["hired"] = hiring_df["interview_score"] >= 80
    hiring_rates = hiring_df.groupby("gender")["hired"].mean()
    print("\nHiring Rates by Gender (Cutoff >= 80):")
    print(hiring_rates)

    rate_m = hiring_rates["Male"]
    rate_f = hiring_rates["Female"]
    hiring_dir = rate_f / rate_m if rate_m > 0 else 1.0
    print(f"Disparate Impact Ratio: {hiring_dir:.2f}")
    if hiring_dir < 0.80:
        print("Adverse impact present. Female acceptance rate is below 80% of male rate.")


def main():
    print("=========================================================")
    print("   Week 12 Topic 05: Addressing Fairness and Bias")
    print("=========================================================")

    applicants = create_scholarship_applicant_data()
    naive_results = evaluate_naive_selection(applicants, cutoff=80.0)
    audit_fairness_and_disparate_impact(naive_results)
    mitigate_bias_threshold_adjustment(applicants)
    run_exercises()

    print("\n[Done] Successfully completed Fairness and Bias pipeline.")


if __name__ == "__main__":
    main()
