# Energy Rating Data Cleaner & Analytics Engine

This project builds a structured, modular data cleaning and transformation pipeline using **Pandas** and **NumPy**. It processes messy household appliance energy rating datasets from data.gov.au to expose the concrete realities of real-world "dirty" data.

## Educational Objectives
- Identifying and quantifying dirty data patterns before analysis.
- Handling non-standard missing values (`"N/A"`, `"-"`, empty strings) using `np.nan`.
- Vectorized string standardization and cleaning.
- Type coercion and safe numeric casting.
- Applying conditional transformations and outlier filtering using NumPy Boolean masks and `np.select` / `np.where`.

## Dataset Anatomy & "Messiness" Profile
The dataset demonstrates the following data issues:
- **Mixed casing and whitespaces** in the `Brand` column.
- **Sentinel missing strings** like `"N/A"` or `"-"` embedded in numeric columns.
- **Multi-value cells** like `"243.0,97.0"` inside the `CompartGrVol` column.

## Pipeline Architecture
- **Data Loader**: Safely fetches data from the web or a local mock file, applying sentinel null replacement at ingestion.
- **Data Cleaner**: Applies a sequence of 5 structured cleaning steps using Pandas and NumPy.
- **Analytics Engine**: Computes high-level summaries and correlations on the cleaned dataset.
- **Streamlit App**: Ties it all together, allowing interactive exploration of the "Before & After" states.

See [QUICKSTART.md](QUICKSTART.md) for instructions on how to run this project.
Screenshots and screencasts can be found in the `images` directory.
