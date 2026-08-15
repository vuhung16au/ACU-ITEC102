# Theory: Fast Analytics

## 1. Columnar Storage (Parquet)
Traditional databases often store data row-by-row (like CSV files). This is great for adding new single records, but slow when you want to compute the average of a single column across millions of rows. Apache Parquet is a columnar storage format. It stores values of the same column contiguously, making analytical queries significantly faster and saving disk space through efficient compression.

## 2. In-Process OLAP (DuckDB)
DuckDB is an in-process SQL OLAP database management system. Instead of spinning up a large external server like PostgreSQL or MySQL, DuckDB runs directly inside the Python process (like SQLite). However, unlike SQLite, it is heavily optimized for analytical queries (OLAP) and can query Parquet files directly using SQL without importing the data first.

## 3. Interactive Web Apps (Streamlit)
Streamlit allows data scientists to turn Python scripts into interactive web apps in minutes. When a user interacts with a widget (like a dropdown), the Streamlit script re-runs from top to bottom. Because DuckDB is so fast, we can safely re-run complex SQL aggregations on large datasets during each interaction without noticeable lag.
