# Theory: NoSQL Databases

## 1. Relational vs NoSQL
Relational databases (like PostgreSQL) store data in strict, predefined tables with rows and columns. They are excellent for structured data with clear relationships. 
NoSQL databases (like MongoDB) are schema-less. They store data in flexible, JSON-like documents. This is perfect for data that is unstructured, constantly changing, or deeply nested (like spatial coordinates or dynamic tags).

## 2. Document-Oriented Storage
In MongoDB, a "table" is called a **Collection**, and a "row" is called a **Document**. Each Document can have a completely different structure. For example, one toilet location might have an `opening_hours` field, while another completely omits it. MongoDB handles this gracefully without requiring schema migrations.

## 3. Querying Nested Data
MongoDB excels at querying nested fields. In our API, we query for accessible toilets using dot notation: `{"properties.features.accessible": True}`. Doing this in a traditional SQL database often requires complex joins across multiple normalized tables.
