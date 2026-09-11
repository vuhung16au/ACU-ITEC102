"""Real-World Data Wrangling: Building an End-to-End Cleaning Pipeline.

This module teaches first-year data science students how to take messy, real-world
data with mixed types, whitespace defects, non-standard dates, and currency strings,
and transform it into a clean, analysis-ready dataset.
"""

import pandas as pd
import numpy as np


def create_raw_messy_admissions_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Creates a realistic raw DataFrame containing typical real-world data entry defects."""
    dirty_admissions = pd.DataFrame({
        "applicant_id": ["ACU-0101", "ACU-0102", "ACU-0103", "ACU-0104", "ACU-0105", "ACU-0106"],
        "full_name": ["  Liam NGUYEN  ", "Emma Watson", "oliver brown ", "  Sophia VU", "Noah Taylor", "Ava Wilson  "],
        "campus": ["syd", "Melbourne", "  SYDNEY  ", "bne", "  melb  ", "Brisbane"],
        "applied_date": ["2026-01-15", "18/01/2026", "2026/01/22", "25-01-2026", "2026.02.01", "05/02/2026"],
        "enrolment_deposit": ["$1,500.00 AUD", "$1500", " $2,250.50 ", "1500.00", "$0.00 AUD", " $1,800.00 "],
        "scholarship_award": ["VC Award", None, "STEM Grant", None, None, "Alumni Grant"],
        "residency": ["Domestic", "International", None, "Domestic", "International", "Domestic"],
    })

    campus_subsidy_lookup = pd.DataFrame({
        "standard_campus": ["North Sydney", "Melbourne", "Brisbane"],
        "subsidy_rate": [0.15, 0.12, 0.18],
    })

    return dirty_admissions, campus_subsidy_lookup


def audit_raw_data(df: pd.DataFrame):
    """Audits data quality defects and structural issues in the raw dataset."""
    print("\n--- 1. Raw Dirty Admissions Ingestion ---")
    print(df)
    print("\nData Types & Null Counts:")
    print(df.dtypes)
    print("\nMissing Values per Column:")
    print(df.isna().sum())


def clean_text_and_categoricals(df: pd.DataFrame) -> pd.DataFrame:
    """Sanitises text casing, strips whitespace, and standardises campus codes."""
    print("\n--- 2. Cleaning Text and Categorical Columns ---")
    cleaned = df.copy()

    # Clean names: strip whitespace and apply proper title casing
    cleaned["full_name"] = cleaned["full_name"].str.strip().str.title()

    # Standardise campus names
    campus_mapping = {
        "syd": "North Sydney",
        "sydney": "North Sydney",
        "melb": "Melbourne",
        "melbourne": "Melbourne",
        "bne": "Brisbane",
        "brisbane": "Brisbane",
    }
    cleaned["campus"] = cleaned["campus"].str.strip().str.lower().map(campus_mapping)

    print("Sanitised Names and Standardised Campuses:")
    print(cleaned[["applicant_id", "full_name", "campus"]])
    return cleaned


def clean_financials_and_dates(df: pd.DataFrame) -> pd.DataFrame:
    """Parses mixed date strings into datetime and strips currency symbols to floats."""
    print("\n--- 3. Parsing Financial Currency and Inconsistent Dates ---")
    cleaned = df.copy()

    # Clean enrolment deposit: remove '$', ',', ' AUD', and whitespace, then cast to float
    cleaned["enrolment_deposit"] = (
        cleaned["enrolment_deposit"]
        .str.replace(r"[$,AUD\s]", "", regex=True)
        .astype(float)
    )

    # Standardise mixed date formats to proper datetime64[ns]
    cleaned["applied_date"] = pd.to_datetime(cleaned["applied_date"], format="mixed")

    # Handle missing values
    cleaned["scholarship_award"] = cleaned["scholarship_award"].fillna("No Scholarship")
    cleaned["residency"] = cleaned["residency"].fillna("Domestic")

    print(cleaned[["applicant_id", "applied_date", "enrolment_deposit", "scholarship_award", "residency"]])
    print(f"\nApplied Date dtype: {cleaned['applied_date'].dtype}")
    print(f"Deposit dtype: {cleaned['enrolment_deposit'].dtype}")
    return cleaned


def merge_and_enrich(cleaned_df: pd.DataFrame, lookup_df: pd.DataFrame) -> pd.DataFrame:
    """Merges auxiliary campus lookup data and calculates net tuition figures."""
    print("\n--- 4. Merging Auxiliary Tables & Calculating Net Fees ---")

    enriched = pd.merge(
        cleaned_df,
        lookup_df,
        left_on="campus",
        right_on="standard_campus",
        how="left",
    ).drop(columns=["standard_campus"])

    # Feature Engineering: Effective deposit after campus subsidy
    enriched["subsidy_kaud"] = (enriched["enrolment_deposit"] * enriched["subsidy_rate"]).round(2)
    enriched["net_deposit"] = (enriched["enrolment_deposit"] - enriched["subsidy_kaud"]).round(2)

    print(enriched[["applicant_id", "full_name", "campus", "enrolment_deposit", "subsidy_rate", "net_deposit"]])
    return enriched


def run_exercises():
    """Hands-on practice exercises for students."""
    print("\n--- 5. Student Practice Exercises ---")

    # Dirty patient billing records
    dirty_billing = pd.DataFrame({
        "patient_id": ["P-1", "P-2", "P-3"],
        "billed_amount": [" $450.50 ", "$1,200.00 AUD", " 320.00 "],
        "admission_date": ["2026/03/10", "12-03-2026", "2026.03.15"],
    })

    print("Raw Billing Dataset:")
    print(dirty_billing)

    # Exercise 1: Clean currency strings to floats
    cleaned_billing = dirty_billing.copy()
    cleaned_billing["billed_amount"] = (
        cleaned_billing["billed_amount"]
        .str.replace(r"[$,AUD\s]", "", regex=True)
        .astype(float)
    )

    # Exercise 2: Parse mixed dates
    cleaned_billing["admission_date"] = pd.to_datetime(cleaned_billing["admission_date"], format="mixed")

    print("\nCleaned Billing Dataset:")
    print(cleaned_billing)
    print(f"Billed amount dtype: {cleaned_billing['billed_amount'].dtype}")
    print(f"Admission date dtype: {cleaned_billing['admission_date'].dtype}")


def main():
    print("=========================================================")
    print("   Week 12 Topic 01: Real-World Data Wrangling Pipeline")
    print("=========================================================")

    raw_df, lookup_df = create_raw_messy_admissions_data()
    audit_raw_data(raw_df)
    clean_text_df = clean_text_and_categoricals(raw_df)
    clean_finance_df = clean_financials_and_dates(clean_text_df)
    merge_and_enrich(clean_finance_df, lookup_df)
    run_exercises()

    print("\n[Done] Successfully completed Real-World Data Wrangling pipeline.")


if __name__ == "__main__":
    main()
