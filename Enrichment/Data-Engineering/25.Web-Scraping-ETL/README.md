# Project 25: Web Scraping and ETL

This project demonstrates the fundamentals of building an Extract, Transform, Load (ETL) data pipeline using Python. You will extract data, clean and format it with `pandas`, and finally load it into a relational PostgreSQL database using raw SQL queries with `psycopg2`.

## Learning Objectives
1. Understand the core concepts of an ETL pipeline.
2. Practice data manipulation and cleaning using `pandas`.
3. Learn how to connect to a PostgreSQL database and execute raw SQL `INSERT` statements using `psycopg2`.
4. Gain experience using a Web UI (`pgAdmin`) to inspect relational databases.

## Data Source
- **Real Data**: The target dataset is the "Electric Vehicle Charging Stations" from [data.gov.au](https://data.gov.au/).
- **Fallback**: A local synthetic CSV dataset (`data/mock_charging_stations.csv`) is provided. This dataset intentionally contains missing coordinates and messy data strings to simulate a realistic data cleaning scenario.

## See Also
- [QUICKSTART.md](QUICKSTART.md): Instructions on how to run and test the project.
- [docs/theory.md](docs/theory.md): Brief theoretical concepts on ETL and Data Pipelines.
- `images/`: Contains screenshots of the working project, including pgAdmin interface.
