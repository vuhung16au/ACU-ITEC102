# Quickstart: Web Scraping and ETL

Follow these instructions to run the ETL pipeline and verify the data in PostgreSQL.

## Prerequisites
- Docker and Docker Compose installed.
- (Optional) `uv` installed to run Python tests locally.

## 1. Start the Database Environment

Run the following command to start PostgreSQL and pgAdmin:

```bash
make up
```

This will automatically create the database `etl_db` and initialize the `charging_stations` table using the scripts inside `init-scripts/`.

## 2. Run the ETL Pipeline

To extract the CSV data, transform/clean it, and load it into PostgreSQL, run:

```bash
make run-etl
```

## 3. Verify Data in pgAdmin

Once the script finishes, you can inspect the data via pgAdmin.

1. Open your browser and navigate to: [http://localhost:5050](http://localhost:5050)
2. **Login**: 
   - Email: `admin@admin.com`
   - Password: `admin`
3. Add a new server in pgAdmin:
   - **Name**: Local Postgres
   - **Connection > Host name/address**: `postgres` (or `localhost` if outside Docker)
   - **Connection > Port**: `5432`
   - **Connection > Username**: `postgres`
   - **Connection > Password**: `postgrespassword`
4. Expand `Databases` > `etl_db` > `Schemas` > `public` > `Tables`.
5. Right-click on `charging_stations` and select **View/Edit Data > All Rows** to see the clean data inserted by your ETL script!

## 4. Run Tests

To verify the `pandas` transformation logic:

```bash
make test
```

## 5. Stop the Environment

```bash
make down
```
