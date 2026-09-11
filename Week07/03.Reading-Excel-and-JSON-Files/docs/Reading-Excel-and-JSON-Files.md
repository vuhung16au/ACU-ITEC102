# Reading Excel and JSON Files in Pandas

Not all datasets are delivered as plain CSV files. In industry, Excel spreadsheets and JSON files are equally prevalent.

---

## Key Concepts

### 1. Reading Microsoft Excel Spreadsheets (`pd.read_excel`)
Excel workbooks store multiple worksheets inside an XML/ZIP archive.

```python
import pandas as pd

# Load the first sheet
df = pd.read_excel("energy_stats.xlsx")

# Load a specific worksheet by name or integer index
df_nsw = pd.read_excel("energy_stats.xlsx", sheet_name="NSW")
```

#### Inspecting Available Sheets
To discover which sheets exist before loading:
```python
xl = pd.ExcelFile("energy_stats.xlsx")
print(xl.sheet_names)  # e.g. ['NSW', 'VIC', 'QLD']
```

> **Note:** Reading modern `.xlsx` files requires the `openpyxl` Python library (`uv add openpyxl` or `pip install openpyxl`).

---

### 2. Reading JSON (`pd.read_json` and `pd.json_normalize`)
JSON (JavaScript Object Notation) is the native language of REST APIs and web services.

#### Flat Record JSON
When JSON contains an array of objects:
```json
[
  {"id": 101, "neighbourhood": "Bondi", "price": 185},
  {"id": 102, "neighbourhood": "Manly", "price": 210}
]
```
Read directly:
```python
df_airbnb = pd.read_json("sydney_airbnb.json")
```

#### Nested / Hierarchical JSON
When JSON has nested sub-dictionaries:
```python
data = [{"name": "Nguyen", "location": {"city": "Sydney", "state": "NSW"}}]

# Flatten into columns: name, location.city, location.state
df_flat = pd.json_normalize(data)
```

---

## Format Comparison

| Attribute | CSV | Excel (`.xlsx`) | JSON |
|---|---|---|---|
| **Human Readability** | High (raw text) | Medium (requires app) | High (structured text) |
| **Multiple Tables** | No (1 table / file) | Yes (multiple sheets) | Yes (nested keys) |
| **Data Types Preserved** | No (all text) | Yes (numbers, dates) | Yes (bools, numbers, nulls) |
| **Parsing Speed** | Fastest | Slower | Fast |
