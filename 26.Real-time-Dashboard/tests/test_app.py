import duckdb
import pandas as pd
import os

def test_duckdb_parquet_connection():
    """Verify DuckDB can read the Parquet file correctly."""
    assert os.path.exists('data/mock_flights.parquet'), "Mock data file missing"
    
    conn = duckdb.connect()
    conn.execute("CREATE VIEW flights AS SELECT * FROM 'data/mock_flights.parquet'")
    
    # Query total records
    count = conn.execute("SELECT count(*) FROM flights").fetchone()[0]
    assert count > 0, "No records found in parquet file"
    
    # Verify schema
    columns = [col[0] for col in conn.execute("DESCRIBE flights").fetchall()]
    assert "date" in columns
    assert "origin" in columns
    assert "destination" in columns
    assert "passengers" in columns
