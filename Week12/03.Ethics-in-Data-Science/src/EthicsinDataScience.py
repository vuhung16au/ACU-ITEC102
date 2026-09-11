"""Ethics in Data Science: Algorithmic Governance, Transparency & Australian Privacy Principles.

This module introduces first-year students to practical ethical frameworks in data science:
- The 8 Australian AI Ethics Principles and Australian Privacy Principles (APPs).
- Auditing Automated Decision-Making (ADM) algorithms for proxy discrimination and opacity.
- Implementing Human-in-the-Loop (HITL) safeguards.
- Building an Automated Ethical Impact Assessment (EIA) scoring rubric.
"""

import pandas as pd
import numpy as np


def create_retention_risk_cohort() -> pd.DataFrame:
    """Generates an algorithmic student retention & bursary decision dataset."""
    return pd.DataFrame({
        "student_id": ["ACU-801", "ACU-802", "ACU-803", "ACU-804", "ACU-805", "ACU-806"],
        "lms_login_frequency": [4, 28, 12, 2, 35, 18],             # Weekly canvas visits
        "assessment_avg": [48.5, 84.0, 62.0, 41.0, 91.5, 68.0],     # Marks out of 100
        "attendance_rate": [0.55, 0.95, 0.78, 0.42, 0.98, 0.82],   # Tutorial attendance
        "postcode_socio_decile": [2, 8, 4, 1, 9, 5],                 # Proxy for socioeconomic status (1=low, 10=high)
        "bursary_need_aud": [3500, 0, 1500, 4500, 0, 1000],
    })


def evaluate_automated_decisions(df: pd.DataFrame) -> pd.DataFrame:
    """Simulates an Automated Decision-Making (ADM) pipeline and audits risk flags."""
    print("--- 1. Evaluating Automated Decision-Making (ADM) Logic ---")
    results = df.copy()

    # Academic risk score computed from observable learning behaviours
    # Weights: Assessment (50%), LMS Activity (25%), Attendance (25%)
    results["academic_risk_score"] = (
        (100 - results["assessment_avg"]) * 0.50
        + (1.0 - (results["lms_login_frequency"] / 40.0).clip(0, 1)) * 100 * 0.25
        + (1.0 - results["attendance_rate"]) * 100 * 0.25
    ).round(1)

    # Automated decision rule (without human review)
    results["auto_flag"] = np.where(
        results["academic_risk_score"] >= 45.0,
        "High Risk - Intensive Support",
        "Low Risk - Standard",
    )

    print(results[["student_id", "assessment_avg", "attendance_rate", "academic_risk_score", "auto_flag"]])
    return results


def audit_proxy_bias(df: pd.DataFrame):
    """Checks whether non-academic proxy variables (e.g. postcode decile) correlate with flags."""
    print("\n--- 2. Auditing Potential Proxy Discrimination ---")
    print("Checking correlation between socioeconomic postcode decile and academic risk:")
    corr = df[["postcode_socio_decile", "academic_risk_score"]].corr().iloc[0, 1]
    print(f"Pearson Correlation: {corr:.3f}")

    if abs(corr) > 0.40:
        print("[ETHICAL ALERT] Postcode is strongly associated with risk score.")
        print("Using postcode in automated triage risks compounding systemic disadvantage.")
    else:
        print("[ETHICAL NOTICE] Postcode shows weak correlation with academic risk score.")
        print("Ensure postcode is excluded from algorithmic scoring to uphold APP 3 & APP 6.")


def enforce_human_in_the_loop(df: pd.DataFrame) -> pd.DataFrame:
    """Enforces human-in-the-loop (HITL) oversight for high-impact decisions."""
    print("\n--- 3. Enforcing Human-in-the-Loop (HITL) Safeguards ---")
    audited = df.copy()

    # Rule: Decisions carrying severe consequences (e.g. bursary withholding or mandatory academic probation)
    # CANNOT be fully automated under the Australian AI Ethics Principles (Principle 7: Contestability & Accountability)
    def determine_action(row):
        if row["academic_risk_score"] >= 50.0 and row["bursary_need_aud"] > 0:
            return "ESCALATE: Student Advisor Case Review Required (Do NOT auto-penalise)"
        elif row["academic_risk_score"] >= 45.0:
            return "Automated Friendly Nudge (Invite to Peer Tutoring)"
        else:
            return "No Intervention Needed"

    audited["recommended_action"] = audited.apply(determine_action, axis=1)
    print(audited[["student_id", "academic_risk_score", "bursary_need_aud", "recommended_action"]])
    return audited


def ethical_impact_assessment(project_name: str, scores: dict[str, int]) -> dict:
    """Calculates an Ethical Impact Assessment (EIA) score across 4 key dimensions."""
    print(f"\n--- 4. Ethical Impact Assessment (EIA) for '{project_name}' ---")
    max_score_per_dim = 5
    total = sum(scores.values())
    max_possible = len(scores) * max_score_per_dim
    percentage = (total / max_possible) * 100

    print("EIA Dimension Scores (0-5 scale):")
    for dimension, score in scores.items():
        status = "PASS" if score >= 3 else "FAIL / REMEDIATION REQUIRED"
        print(f"  - {dimension}: {score}/5 ({status})")

    print(f"\nOverall Ethical Score: {total}/{max_possible} ({percentage:.1f}%)")
    if percentage >= 80 and all(s >= 3 for s in scores.values()):
        recommendation = "APPROVED: Proceed with regular quarterly compliance auditing."
    else:
        recommendation = "BLOCKED: Requires mitigation plan before deployment."
    print(f"Status: {recommendation}")

    return {"project": project_name, "percentage": percentage, "recommendation": recommendation}


def run_exercises():
    """Hands-on student exercises on ethical algorithmic design."""
    print("\n--- 5. Student Practice Exercises ---")

    # Scenario: Automated Recruitment Screening Model
    hiring_eia_scores = {
        "Consent & Data Provenance (APP 3/5)": 4,
        "Demographic Parity & Fairness (Principle 3)": 2,  # Low score
        "Explainability & Transparency (Principle 5)": 2,  # Low score
        "Human Contestability & Appeal (Principle 7)": 1,  # Critical fail
    }

    print("Auditing Proposed Automated Resume Screening Tool:")
    res = ethical_impact_assessment("AI Resume Parser v1.0", hiring_eia_scores)
    print(f"Assessment Output: {res['recommendation']}")


def main():
    print("=========================================================")
    print("   Week 12 Topic 03: Ethics in Data Science")
    print("=========================================================")

    cohort = create_retention_risk_cohort()
    evaluated = evaluate_automated_decisions(cohort)
    audit_proxy_bias(evaluated)
    enforce_human_in_the_loop(evaluated)

    # University Learning Analytics EIA
    analytics_scores = {
        "Data Minimisation & Consent (APP 3)": 5,
        "Fairness & Non-Discrimination (Principle 3)": 4,
        "Algorithmic Transparency (Principle 5)": 4,
        "Human Contestability (Principle 7)": 5,
    }
    ethical_impact_assessment("ACU Early Alert Retention System", analytics_scores)
    run_exercises()

    print("\n[Done] Successfully completed Ethics in Data Science pipeline.")


if __name__ == "__main__":
    main()
