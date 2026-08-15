# Theory: ETL Pipelines

## 1. Extract
The extraction phase is about gathering data from various sources. This could be querying an API, downloading a CSV file, scraping HTML from a website, or reading from another database.

## 2. Transform
Real-world data is messy. In the transformation phase, we clean and standardize the data.
- **Handling Missing Values**: We drop rows with `None` or `NaN` coordinates since a charging station without a location is not useful to map.
- **Data Formatting**: Trimming unnecessary whitespace from string fields (like `name` and `address`).
- **Data Validation**: Ensuring numerical columns like `capacity` are positive integers.

We use `pandas`, an industry-standard Python library, to efficiently perform these vectorised operations over thousands of rows.

## 3. Load
The final phase is loading the clean data into a target destination, such as a Data Warehouse or a relational database like PostgreSQL. Here we use `psycopg2` to execute a raw SQL `INSERT` statement. Utilizing `execute_values` is an optimized way to bulk insert multiple records efficiently.
