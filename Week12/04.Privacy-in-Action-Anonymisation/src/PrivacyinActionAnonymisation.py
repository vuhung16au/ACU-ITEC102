"""Privacy in Action: De-Identification, Cryptographic Hashing & k-Anonymity.

This module teaches first-year data science students practical privacy-preserving
techniques in compliance with the Australian Privacy Principles (APPs) and OAIC guidelines:
- Distinguishing direct identifiers, quasi-identifiers, and sensitive attributes.
- Pseudonymising identifiers via salted SHA-256 cryptographic hashing.
- Generalising / coarsening quasi-identifiers (age binning, postcode truncation).
- Measuring and verifying k-anonymity across equivalence classes.
"""

import hashlib
import pandas as pd
import numpy as np


def create_raw_health_counselling_records() -> pd.DataFrame:
    """Generates an identified dataset of student counselling & health service visits."""
    return pd.DataFrame({
        "student_id": ["S1001", "S1002", "S1003", "S1004", "S1005", "S1006", "S1007", "S1008"],
        "full_name": ["Alice Nguyen", "Bob Chen", "Charlie Smith", "Diana Miller",
                      "Evan Davis", "Fiona Taylor", "George Wilson", "Hannah Brown"],
        "age": [19, 19, 24, 25, 22, 23, 31, 35],
        "gender": ["Female", "Female", "Male", "Female", "Male", "Female", "Male", "Female"],
        "postcode": ["2060", "2060", "3000", "3000", "2060", "2060", "4000", "4000"],
        "counselling_reason": [
            "Exam Stress", "Exam Stress", "Anxiety", "Financial Crisis",
            "Anxiety", "Exam Stress", "Depression", "Workload Stress"
        ]
    })


def inspect_privacy_risk(df: pd.DataFrame):
    """Categorises columns into Direct, Quasi-, and Sensitive attributes."""
    print("--- 1. Categorising Personal Privacy Attributes ---")
    print("Raw Identified Records:")
    print(df[["student_id", "full_name", "age", "gender", "postcode", "counselling_reason"]])

    print("\nPrivacy Classification:")
    print("  • Direct Identifiers (PII): 'student_id', 'full_name' -> MUST BE REDACTED OR HASHED")
    print("  • Quasi-Identifiers: 'age', 'gender', 'postcode' -> CAN ENABLE RE-IDENTIFICATION")
    print("  • Sensitive Attributes: 'counselling_reason' -> MUST BE PROTECTED")


def pseudonymise_with_salted_hash(df: pd.DataFrame, salt: str = "ACU_SECURE_2026_SALT") -> pd.DataFrame:
    """Replaces direct identifiers with a one-way salted SHA-256 cryptographic token."""
    print("\n--- 2. Cryptographic Salted Pseudonymisation ---")
    anonymised = df.copy()

    def hash_identifier(val: str) -> str:
        salted_str = f"{salt}_{val}"
        return hashlib.sha256(salted_str.encode("utf-8")).hexdigest()[:10]

    # Generate persistent pseudonym and drop raw name
    anonymised["pseudo_id"] = anonymised["student_id"].apply(hash_identifier)
    anonymised = anonymised.drop(columns=["student_id", "full_name"])

    print("Direct identifiers stripped and replaced with salted tokens:")
    print(anonymised[["pseudo_id", "age", "gender", "postcode", "counselling_reason"]])
    return anonymised


def generalise_quasi_identifiers(df: pd.DataFrame) -> pd.DataFrame:
    """Coarsens age into brackets and truncates postcodes to regional prefixes."""
    print("\n--- 3. Generalisation & Coarsening of Quasi-Identifiers ---")
    coarsened = df.copy()

    # Bin age into life stage brackets: <20, 20-29, 30+
    coarsened["age_bracket"] = pd.cut(
        coarsened["age"],
        bins=[0, 19, 29, 120],
        labels=["<=19", "20-29", "30+"],
        right=True
    ).astype(str)

    # Coarsen postcode to 2-digit state region prefix
    coarsened["postcode_prefix"] = coarsened["postcode"].astype(str).str[:2] + "XX"

    # Drop fine-grained quasi-identifiers
    coarsened = coarsened.drop(columns=["age", "postcode"])

    print("Coarsened Quasi-Identifiers Table:")
    print(coarsened[["pseudo_id", "age_bracket", "gender", "postcode_prefix", "counselling_reason"]])
    return coarsened


def evaluate_k_anonymity(df: pd.DataFrame, quasi_cols: list[str], target_k: int = 2) -> tuple[int, pd.DataFrame]:
    """Computes k-anonymity: the minimum group size across all quasi-identifier combinations."""
    print(f"\n--- 4. Evaluating k-Anonymity on Quasi-Identifiers: {quasi_cols} ---")

    grouped = df.groupby(quasi_cols, as_index=False).size().rename(columns={"size": "equivalence_group_size"})
    min_k = grouped["equivalence_group_size"].min()

    print("Equivalence Classes (Frequency of Quasi-Identifier Profiles):")
    print(grouped)
    print(f"\nCalculated Minimum k: {min_k}")

    if min_k >= target_k:
        print(f"[PRIVACY PASS] Dataset satisfies {min_k}-anonymity (Target k >= {target_k}).")
    else:
        print(f"[PRIVACY WARNING] Dataset achieves only {min_k}-anonymity. Target was k >= {target_k}.")
        vulnerable = grouped[grouped["equivalence_group_size"] < target_k]
        print("Vulnerable profile(s) requiring further suppression or aggregation:")
        print(vulnerable)

    return min_k, grouped


def run_exercises():
    """Hands-on student practice exercises."""
    print("\n--- 5. Student Practice Exercises ---")
    raw_patient_log = pd.DataFrame({
        "patient_name": ["John D", "Sarah M", "Ken P", "Laura K"],
        "age": [22, 28, 45, 48],
        "postcode": ["3000", "3000", "2000", "2000"],
        "diagnosis": ["Flu", "Asthma", "Diabetes", "Hypertension"]
    })
    print("Raw Clinic Dataset:")
    print(raw_patient_log)

    # 1. Drop patient_name
    anon = raw_patient_log.drop(columns=["patient_name"])

    # 2. Generalise age into broad categories: 18-35, 36-60
    anon["age_group"] = pd.cut(anon["age"], bins=[18, 35, 60], labels=["18-35", "36-60"]).astype(str)
    anon = anon.drop(columns=["age"])

    # 3. Check k-anonymity
    print("\nAnonymised Clinic Dataset:")
    print(anon)
    k, _ = evaluate_k_anonymity(anon, quasi_cols=["age_group", "postcode"], target_k=2)
    print(f"Exercise Result: Minimum k = {k}")


def main():
    print("=========================================================")
    print("   Week 12 Topic 04: Privacy in Action - Anonymisation")
    print("=========================================================")

    raw_data = create_raw_health_counselling_records()
    inspect_privacy_risk(raw_data)
    pseudo_df = pseudonymise_with_salted_hash(raw_data)
    coarsened_df = generalise_quasi_identifiers(pseudo_df)
    evaluate_k_anonymity(coarsened_df, quasi_cols=["age_bracket", "gender", "postcode_prefix"], target_k=2)
    run_exercises()

    print("\n[Done] Successfully completed Privacy in Action pipeline.")


if __name__ == "__main__":
    main()
