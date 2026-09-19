# Project Memory

## Overview
This project is a placement analytics and data-insights workflow for engineering students. It ingests a CSV dataset, loads it into a MySQL database, supports filtered SQL queries, and computes placement-related analytics such as salary trends, DSA proficiency bands, and tier-wise comparisons.

## Current Project Scope
- Data ingestion from a local CSV file
- Database creation and MySQL indexing
- Query-building for college tier, branch, CGPA, DSA, and placement filters
- Analytical reporting for salary and skill patterns
- Python-based data processing with pandas and SQLAlchemy

## Key Learnings

### 1. Data ingestion is the foundation
The system depends on a valid CSV and a working MySQL configuration. If the dataset is missing or if the database connection is misconfigured, downstream analysis fails.

### 2. Query logic must be parameterized
The filter builder in `Project/query_builder.py` should remain the place where SQL conditions are assembled. This reduces the risk of broken SQL statements and makes the project easier to extend.

### 3. Analytics should stay separate from storage logic
The analytics code in `Project/analytics.py` should not directly handle database credentials or import logic. This separation keeps the pipeline cleaner and easier to test.

### 4. DSA-based grouping is a useful business lens
Using DSA problem counts to create skill bands gives the analytics more practical value than only looking at raw package numbers. It makes salary patterns easier to interpret.

### 5. Missing data must be handled intentionally
The ingestion module fills missing numeric values with a median strategy. This is a reasonable default for a learning project, but it should be revisited if data quality requirements become stricter.

## Known Issues / Risks
- Database credentials are currently hardcoded in `Project/Database.py`.
- Some query-building logic may require validation against the actual CSV schema.
- The project is still a local, script-based workflow rather than a production-ready application.
- The analytics abstraction should be tested against real data before being used for reporting decisions.

## Recommended Next Improvements
- Move DB credentials to environment variables.
- Add unit tests for import, filter logic, and analytics calculation outcomes.
- Validate SQL column names against the dataset schema before execution.
- Add a dashboard layer for quick reporting.
- Document the exact field definitions from the dataset for future contributors.

## Working Assumptions
- The project uses MySQL locally for persistence.
- The data file is a campus placement dataset for Indian engineering students.
- The target audience includes students, placement coordinators, and academic analysts.
- The solution is currently a prototype and learning project rather than a fully productionized system.

## Important Context
The repository is a study and project workspace covering Excel, Python, SQL, statistics, and analytics topics. The `Project/` folder is the main data-analytics implementation and should be treated as the core product area for placement analysis work.
