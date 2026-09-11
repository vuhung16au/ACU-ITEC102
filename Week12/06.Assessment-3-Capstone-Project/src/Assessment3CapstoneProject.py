"""Assessment 3 Capstone Project: End-to-End Data Science & Responsible AI Pipeline.

This capstone module synthesises the full 12-week ITEC102 curriculum:
1. Data Ingestion & Quality Audit (Week 07)
2. Data Wrangling & Feature Engineering (Week 08 & 12.1)
3. Exploratory Data Analysis & Outlier Detection (Week 09, 11 & 12.2)
4. Visual Storytelling with Matplotlib (Week 11 & 12.2)
5. Privacy-Preserving De-Identification & k-Anonymity (Week 12.4)
6. Algorithmic Fairness, Disparate Impact & Ethical Governance (Week 12.3 & 12.5)
"""

import hashlib
import os
from pathlib import Path

os.environ["MPLCONFIGDIR"] = "/tmp/matplotlib_cache"
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# =======================================================================
# MILESTONE 1: Raw Ingestion & Auxiliary Lookups
# =======================================================================
def ingest_capstone_raw_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Simulates realistic raw graduate cohort data with real-world defects."""
    raw_graduates = pd.DataFrame({
        "student_id": [f"ACU-{i:04d}" for i in range(1, 9)],
        "full_name": [
            "  Liam O'CONNOR  ", "Sophia CHEN", "ethan smith ", "  Mia AL-MANSOOR",
            "Oliver Taylor", "Ava WILSON  ", "Lucas MARTIN", "  Chloe ZHANG"
        ],
        "demographic_cohort": [
            "Group A", "Group B", "Group A", "Group B",
            "Group A", "Group A", "Group B", "Group B"
        ],
        "study_area": [
            "Data Science", "Software Eng", "data science", "Cyber Security",
            "software eng", "Cyber Security", "Data Science", "Software Eng"
        ],
        "grad_date": [
            "2026-06-15", "18/06/2026", "2026/07/01", "05-07-2026",
            "2026.07.12", "15/07/2026", "2026-07-20", "22/07/2026"
        ],
        "gpa": [6.2, 5.8, 4.9, 6.7, 5.4, 6.9, 4.2, 5.9],
        "starting_salary": [
            "$82,000.00 AUD", " $78500 ", "65000.00", "$94,200.00 AUD",
            "$76,000", " $220,000.00 AUD ", "$61,500.00 AUD", " $81,000.00 "
        ],
        "internship_done": ["Yes", "Yes", "No", "Yes", "No", "Yes", "No", "Yes"],
        "age": [22, 24, 21, 28, 23, 29, 22, 25],
        "postcode": ["2060", "2060", "3000", "3000", "2060", "4000", "4000", "3000"],
    })

    discipline_lookup = pd.DataFrame({
        "clean_discipline": ["Data Science", "Software Engineering", "Cyber Security"],
        "industry_growth_rate": [0.18, 0.14, 0.22],
    })

    return raw_graduates, discipline_lookup


# =======================================================================
# MILESTONE 2: Data Wrangling & Sanitisation Pipeline
# =======================================================================
def clean_and_wrangle(df: pd.DataFrame, lookup: pd.DataFrame) -> pd.DataFrame:
    """Cleans text, standardises categoricals, parses currency/dates, and merges lookups."""
    print("\n--- Milestone 2: Data Wrangling & Normalisation ---")
    cleaned = df.copy()

    # 1. Strip whitespace and title case names
    cleaned["full_name"] = cleaned["full_name"].str.strip().str.title()

    # 2. Standardise discipline names
    discipline_map = {
        "data science": "Data Science",
        "software eng": "Software Engineering",
        "software engineering": "Software Engineering",
        "cyber security": "Cyber Security",
    }
    cleaned["study_area"] = cleaned["study_area"].str.strip().str.lower().map(discipline_map)

    # 3. Clean starting salary to float
    cleaned["starting_salary"] = (
        cleaned["starting_salary"]
        .str.replace(r"[$,AUD\s]", "", regex=True)
        .astype(float)
    )

    # 4. Standardise mixed dates
    cleaned["grad_date"] = pd.to_datetime(cleaned["grad_date"], format="mixed")

    # 5. Merge auxiliary lookup data
    enriched = pd.merge(
        cleaned,
        lookup,
        left_on="study_area",
        right_on="clean_discipline",
        how="left"
    ).drop(columns=["clean_discipline"])

    print("Wrangled & Enriched Dataset:")
    print(enriched[["student_id", "full_name", "study_area", "grad_date", "gpa", "starting_salary", "industry_growth_rate"]])
    return enriched


# =======================================================================
# MILESTONE 3: Exploratory Data Analysis (EDA)
# =======================================================================
def conduct_eda(df: pd.DataFrame) -> tuple[float, float, pd.DataFrame]:
    """Computes descriptive statistics, correlation matrix, and detects salary outliers."""
    print("\n--- Milestone 3: Exploratory Data Analysis ---")

    # Tukey's Fence for Starting Salary
    q1 = df["starting_salary"].quantile(0.25)
    q3 = df["starting_salary"].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    print(f"Salary IQR: ${iqr:,.2f} | Lower Fence: ${lower_bound:,.2f} | Upper Fence: ${upper_bound:,.2f}")
    outliers = df[(df["starting_salary"] < lower_bound) | (df["starting_salary"] > upper_bound)]
    print(f"Identified {len(outliers)} Outlier Graduate(s):")
    print(outliers[["student_id", "full_name", "study_area", "starting_salary"]])

    # Grouped analysis
    print("\nMedian Starting Salary by Study Area & Internship:")
    grouped = df.groupby(["study_area", "internship_done"])["starting_salary"].agg(["count", "median", "mean"])
    print(grouped)

    return lower_bound, upper_bound, outliers


# =======================================================================
# MILESTONE 4: Visual Storytelling
# =======================================================================
def generate_capstone_visuals(df: pd.DataFrame, upper_fence: float):
    """Generates visual analysis report with boxplot and scatter analysis."""
    print("\n--- Milestone 4: Visual Storytelling ---")
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # Boxplot of salary by study area
    disciplines = sorted(df["study_area"].unique())
    salary_by_disc = [df[df["study_area"] == d]["starting_salary"] for d in disciplines]

    axes[0].boxplot(salary_by_disc, tick_labels=disciplines, patch_artist=True)
    axes[0].axhline(upper_fence, color="crimson", linestyle=":", label=f"Outlier Fence (${upper_fence:,.0f})")
    axes[0].set_title("Graduate Compensation by Discipline", fontweight="bold")
    axes[0].set_ylabel("Starting Salary (AUD)")
    axes[0].legend(loc="upper left")
    axes[0].grid(True, linestyle="--", alpha=0.5, axis="y")

    # Scatter: GPA vs Salary by Internship Status
    yes_df = df[df["internship_done"] == "Yes"]
    no_df = df[df["internship_done"] == "No"]

    axes[1].scatter(yes_df["gpa"], yes_df["starting_salary"], color="#2b5c8f", s=80, label="Internship Completed")
    axes[1].scatter(no_df["gpa"], no_df["starting_salary"], color="#d95f02", s=80, label="No Internship")
    axes[1].set_title("Academic GPA vs. Starting Salary", fontweight="bold")
    axes[1].set_xlabel("GPA (7-point Scale)")
    axes[1].set_ylabel("Starting Salary (AUD)")
    axes[1].legend(loc="upper left")
    axes[1].grid(True, linestyle="--", alpha=0.5)

    plt.tight_layout()
    output_path = Path(__file__).resolve().parent.parent / "capstone_visual_report.png"
    fig.savefig(output_path, dpi=120)
    plt.close(fig)
    print(f"Generated visual report saved to '{output_path}'.")


# =======================================================================
# MILESTONE 5: Privacy-Preserving De-Identification & k-Anonymity
# =======================================================================
def apply_privacy_anonymisation(df: pd.DataFrame) -> tuple[pd.DataFrame, int]:
    """De-identifies graduates via salted SHA-256 and coarsens quasi-identifiers."""
    print("\n--- Milestone 5: Privacy Protection & k-Anonymity ---")
    anon = df.copy()

    # 1. Salted SHA-256 hashing of student_id
    salt = "ACU_CAPSTONE_SALT_2026"
    anon["anon_id"] = anon["student_id"].apply(
        lambda sid: hashlib.sha256(f"{salt}_{sid}".encode("utf-8")).hexdigest()[:8]
    )

    # 2. Redact direct identifiers
    anon = anon.drop(columns=["student_id", "full_name"])

    # 3. Coarsen quasi-identifiers: age brackets and 2-digit postcodes
    anon["age_bracket"] = pd.cut(anon["age"], bins=[0, 24, 100], labels=["<=24", "25+"]).astype(str)
    anon["postcode_prefix"] = anon["postcode"].astype(str).str[:2] + "XX"
    anon = anon.drop(columns=["age", "postcode"])

    # 4. Measure k-anonymity
    quasi_cols = ["age_bracket", "postcode_prefix"]
    equiv = anon.groupby(quasi_cols, as_index=False).size().rename(columns={"size": "k_size"})
    min_k = equiv["k_size"].min()

    print(f"Dataset satisfies k-Anonymity with k = {min_k} (Quasi-identifiers: {quasi_cols})")
    print(equiv)
    return anon, min_k


# =======================================================================
# MILESTONE 6: Fairness Audit & Algorithmic Governance
# =======================================================================
def audit_and_mitigate_fairness(df: pd.DataFrame) -> dict:
    """Audits scholarship selection across demographic groups for adverse impact."""
    print("\n--- Milestone 6: Algorithmic Fairness & Governance Audit ---")
    audited = df.copy()

    # Initial selection rule: GPA >= 5.8
    audited["scholarship_awarded"] = audited["gpa"] >= 5.8

    group_rates = audited.groupby("demographic_cohort")["scholarship_awarded"].mean()
    rate_a = group_rates.get("Group A", 0.0)
    rate_b = group_rates.get("Group B", 0.0)
    dir_ratio = rate_b / rate_a if rate_a > 0 else 1.0

    print("Initial Selection Rates by Demographic Cohort:")
    print(group_rates)
    print(f"Disparate Impact Ratio (DIR): {dir_ratio:.3f}")

    if dir_ratio < 0.80:
        print("[ETHICAL ALERT] Adverse impact detected under the 80% rule.")
        status = "MITIGATION_REQUIRED"
    else:
        print("[FAIRNESS PASS] Model satisfies the 80% adverse impact threshold.")
        status = "APPROVED"

    return {
        "rate_group_a": rate_a,
        "rate_group_b": rate_b,
        "dir": dir_ratio,
        "governance_status": status,
    }


def main():
    print("=================================================================")
    print("   Week 12 Topic 06: Assessment 3 Capstone Synthesis Project")
    print("=================================================================")

    # Milestone 1: Ingestion
    raw_df, lookup_df = ingest_capstone_raw_data()
    print("--- Milestone 1: Raw Ingestion Complete ---")
    print(f"Ingested {len(raw_df)} graduate records and {len(lookup_df)} lookup entries.")

    # Milestone 2: Wrangling
    clean_df = clean_and_wrangle(raw_df, lookup_df)

    # Milestone 3: EDA
    lower_f, upper_f, outliers = conduct_eda(clean_df)

    # Milestone 4: Visuals
    generate_capstone_visuals(clean_df, upper_f)

    # Milestone 5: Privacy
    anon_df, min_k = apply_privacy_anonymisation(clean_df)

    # Milestone 6: Fairness & Governance
    fairness_results = audit_and_mitigate_fairness(clean_df)

    print("\n=================================================================")
    print("   Capstone Synthesis Complete: All 6 Milestones Satisfied")
    print("=================================================================")


if __name__ == "__main__":
    main()
