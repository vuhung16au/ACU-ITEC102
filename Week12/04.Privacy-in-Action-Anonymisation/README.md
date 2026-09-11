# Privacy in Action: Anonymisation & De-Identification

This module explores practical data de-identification and privacy-preserving techniques under the Australian Privacy Principles (APPs) and the Office of the Australian Information Commissioner (OAIC) guidance.

---

## Learning Objectives
- Differentiate between **Direct Identifiers**, **Quasi-Identifiers**, and **Sensitive Attributes**.
- Pseudonymise primary identifiers using salted cryptographic hashing (`hashlib.sha256`).
- Generalise and coarsen quasi-identifiers through numerical binning and geographic prefixing.
- Measure, audit, and satisfy $k$-anonymity to prevent re-identification linkage attacks.

---

## Folder Structure
- `docs/`: Conceptual documentation on linkage attacks, salting, and $k$-anonymity theory.
- `notebooks/`:
  - `01_04.Privacy-in-Action-Anonymisation.ipynb`: Interactive Jupyter notebook demonstrating hashing, coarsening, and $k$-anonymity audits.
- `src/`:
  - `PrivacyinActionAnonymisation.py`: Production-grade Python script executing the de-identification pipeline.
- `QUICKSTART.md`: Commands to run scripts and launch notebooks.
- `Makefile`: Convenience commands (`make run`, `make test`, `make clean`).
