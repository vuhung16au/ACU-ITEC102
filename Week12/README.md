# Week 12: Real-World Data Wrangling, Ethics, and Capstone Project

Welcome to Week 12 of ACU-ITEC102. This concluding week brings together the complete data science toolchain developed throughout the semester—integrating **data cleaning**, **exploratory data analysis (EDA)**, **data ethics**, **privacy preservation (anonymisation)**, **algorithmic fairness auditing**, and the **Assessment 3 Capstone Project**.

---

## Learning Outcomes
By completing this week's materials, you will be able to:
1. **Execute End-to-End Data Wrangling**: Clean messy, real-world data combining string parsing, regular expressions, date parsing, and table merging.
2. **Conduct Structured EDA**: Apply the 5-step Exploratory Data Analysis framework to diagnose distributions, correlations, and business insights.
3. **Apply Ethical Frameworks**: Evaluate data science solutions against the Australian Privacy Principles (APPs), the Privacy Act 1988, and the ACS Code of Professional Conduct.
4. **Implement Data Anonymisation**: Protect personal data using salted cryptographic hashing (SHA-256), attribute generalisation/coarsening, and $k$-anonymity verification.
5. **Audit Algorithmic Fairness**: Quantify disparate impact using the 80% rule, detect demographic parity discrepancies, and implement mitigation strategies.
6. **Deliver Capstone Synthesis**: Build a complete, cohesive end-to-end data pipeline combining ingestion, analysis, visualisation, and governance.

---

## Topic Navigation

| Topic | Focus Area | Key Concepts & Methods |
| :--- | :--- | :--- |
| [01. Real-World Data Wrangling](01.Real-World-Data-Wrangling/) | End-to-end dirty data ingestion, string parsing, dates, merging | `str.strip()`, `str.replace()`, `pd.to_datetime()`, `pd.merge()` |
| [02. Exploratory Data Analysis](02.Exploratory-Data-Analysis/) | 5-step EDA framework, correlation matrix, outlier bounds | `.info()`, `.describe()`, `.corr()`, IQR outlier fences |
| [03. Ethics in Data Science](03.Ethics-in-Data-Science/) | Privacy Act 1988, APPs, automated decision-making (ADM), impact audit | Ethical Impact Assessment (EIA), stakeholder harm analysis |
| [04. Privacy in Action: Anonymisation](04.Privacy-in-Action-Anonymisation/) | De-identification, salted SHA-256 hashing, binning, $k$-anonymity | `hashlib.sha256()`, age/postcode coarsening, $k$-anonymity checks |
| [05. Addressing Fairness and Bias](05.Addressing-Fairness-and-Bias/) | Algorithmic bias, demographic parity, Disparate Impact (80% rule) | Disparate Impact Ratio, selection rate comparisons, thresholding |
| [06. Assessment 3 Capstone Project](06.Assessment-3-Capstone-Project/) | Complete capstone pipeline synthesis (Wrangling + EDA + Visuals + Ethics) | End-to-end Python pipeline and capstone project rubric |

---

## Folder Structure

Each topic folder is structured consistently:
```text
Topic-Folder/
├── notebooks/       # Interactive Jupyter notebooks with step-by-step guidance & exercises
├── src/             # Clean, runnable Python scripts containing all demonstrations
├── docs/            # Conceptual summaries and syntax reference guides
├── Makefile         # Commands to run scripts or launch Jupyter Lab
├── README.md        # Topic-level learning objectives and instructions
└── QUICKSTART.md    # Step-by-step setup and execution guide
```

---

## Recommended Learning Flow
1. Work through Topics `01` to `05` to master technical wrangling, EDA, privacy, and fairness auditing.
2. Complete Topic `06` (Assessment 3 Capstone Project) as your comprehensive capstone portfolio demonstration.
