# Design Document

## 1. Purpose

This document describes the technical design of the Campus Placement Analytics Platform. It translates the product requirements into a practical design for the current implementation and highlights how the system components interact to support student placement analysis.

## 2. Design Goals

- Build a modular analytics workflow around a single placement dataset.
- Maintain separation between database access, query logic, and analytical logic.
- Keep the design simple enough for a learning project while remaining extensible.
- Make it easy to add dashboards, filters, or predictive analytics later.

## 3. Design Principles

### 3.1 Separation of Concerns
Each module owns a specific responsibility:
- `Database.py` handles persistence and ingestion.
- `query_builder.py` handles SQL filtering logic.
- `analytics.py` handles salary and skill-based analysis.

### 3.2 Reusability
Functions are written to be reusable by future scripts, notebooks, or dashboards.

### 3.3 Data-First Approach
The system uses data tables and pandas aggregation as the main computation model, rather than building a complex application framework.

### 3.4 Learnability
The design is intentionally readable and transparent so students and early developers can trace each stage of data movement.

## 4. System Overview

The application receives a raw CSV placement dataset, normalizes it, stores it in MySQL, and then performs analytical operations on the structured data.

The system is intentionally small but follows a scalable design pattern:

- Input: placement CSV
- Storage: MySQL table named `students`
- Business logic: query filters + analytics aggregation
- Output: structured Python dictionaries and DataFrames

## 5. Module Design

### 5.1 Database Module

#### Responsibilities
- initialize target database
- validate CSV route
- clean null values
- import dataset into MySQL
- create indexes
- allow SQL execution

#### Design Structure
```python
ensure_database()
init_db(csv_path)
run_query(query, params)
```

#### Notes
This module acts as the persistence boundary. It handles all direct interaction with MySQL and is the only place where raw DB connectivity is defined.

### 5.2 Query Builder Module

#### Responsibilities
- assemble dynamic WHERE clauses
- support filter arrays for tiers and branches
- bind values safely using parameter dictionaries
- include placement conditions and CGPA/DSA thresholds

#### Example Logic
The function accepts:
- `tiers`
- `branches`
- `cgpa_range`
- `min_dsa`
- `placed_only`

It builds a SQL clause and parameter map like:
```python
where_clause, params = build_parameterized_filter(...)
```

#### Design Notes
This is a small but useful abstraction that keeps filter logic out of the database module and makes reporting queries easier to build and maintain.

### 5.3 Analytics Module

#### Responsibilities
- transform data into skill bands
- compute mean package by DSA score range
- compare salary patterns by college tier
- prepare output for dashboards or JSON serialization

#### Example Computation
The system does the following:
- bins students by DSA problems solved using `pd.cut`
- calculates mean salary for each skill bucket
- projects salary inflation using a growth formula
- groups by skill band and college tier

#### Output Model
```python
return {
    "dsa_curve": [...],
    "tier_parity": [...]
}
```

This keeps the results structured and easy to pass into future visualization or API code.

## 6. Data Model Design

### 6.1 Student Record
Each row in the `students` table is a student profile and contains profile information relevant to placement analysis.

Key fields include:
- `College_Tier`
- `Branch`
- `CGPA`
- `DSA_Problems_Solved`
- `Placement_Status`
- `Package_LPA`
- `GitHub_Contributions`
- `Open_Source_Contribution`
- `LinkedIn_Activity_score`

### 6.2 Derived Dimensions
The analytics layer creates calculated dimensions such as:
- `Skill_Band`
- `bin_mid`
- `projected_lpa`

These derived values are not stored in the base table but are generated during analysis for reporting.

## 7. Interaction Design

### 7.1 Import Interaction
```text
CSV file -> pandas read_csv() -> null handling -> to_sql() -> MySQL table
```

### 7.2 Query Interaction
```text
filters -> parameterized SQL -> database -> DataFrame -> analytics
```

### 7.3 Analytics Interaction
```text
filtered data -> DSA bucketization -> salary grouping -> output objects
```

## 8. Error Handling Strategy

The current design includes basic error handling for the most important operations:

- Missing CSV file: raises `FileNotFoundError`
- Missing database: creates it first
- Invalid values: fills numeric gaps with median values
- SQL execution: returns DataFrame if query is valid, otherwise raises DB error

## 9. Security and Configuration Design

Current implementation stores configuration directly in code, including:
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`
- `DB_NAME`

This is acceptable for a learning project, but the production design should move these values to environment variables or a secure credentials store.

## 10. Scalability Design

The platform is currently built for a single local dataset and a small number of users. The design is still extensible for future growth because:

- data is centralized in a database,
- queries are parameterized,
- analytics logic is separated from DB code,
- outputs are structured and easy to expose in dashboards or APIs.

## 11. Future Design Enhancements

### 11.1 Web Dashboard
Add a UI layer using Streamlit, Flask, or FastAPI to expose charts and filter controls to non-technical users.

### 11.2 API Layer
Create endpoints for:
- loading CSV
- running filtered queries
- returning analytics summaries

### 11.3 Testing Layer
Add unit tests for:
- CSV import
- query builder accuracy
- analytics calculation correctness
- null-handling behavior

### 11.4 Cloud Deployment
Move MySQL to a managed database service and configure environment-based credentials.

## 12. Design Summary

The current design is intentionally lightweight and practical. It follows a clear flow from raw CSV to SQL storage to filtered analysis and reporting. While the system is not yet a full production application, it provides a strong foundation for placement analytics and is structured in a way that can evolve into a more advanced dashboard or service-based platform.
