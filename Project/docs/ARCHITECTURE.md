# Architecture Document

## 1. Overview

The Campus Placement Analytics Platform is a Python-based analytics system designed to transform raw placement data into actionable insights. It imports student records from a CSV file, stores them in a MySQL database, supports filtered querying, and calculates placement-related summaries such as salary trends, tier parity, and DSA-based skill comparisons.

The architecture follows a simple layered design: data ingestion, persistence, query layer, and analytics layer. This keeps the workflow modular and makes it easier to extend with dashboards, ML models, or web-based interfaces in the future.

## 2. Architectural Goals

- Support structured analysis of engineering placement data.
- Separate responsibilities for data loading, database access, and calculations.
- Enable filtered analysis using college tier, branch, CGPA, DSA score, and placement status.
- Use Python and pandas for data processing.
- Use MySQL for persistence and query execution.
- Keep the solution easy to understand and extend for learning, prototyping, and faculty/student analytics.

## 3. System Context

The system sits between the source dataset and the analytic outputs.

Actors:
- Student: analyzes personal profile vs. placement pattern
- Placement coordinator: reviews placement performance by tier / branch
- Academic administrator: inspects cohort trends and placement outcomes
- Analyst: explores dataset and builds reports

System interactions:
- Reads CSV dataset
- Creates or connects to MySQL database
- Stores cleaned data
- Builds query filters
- Returns analytics results in Python-friendly structures

## 4. High-Level Architecture

The project currently implements a three-layer structure:

1. Data Layer
   - CSV source file
   - MySQL database
   - SQLAlchemy engine and connection management

2. Processing Layer
   - Pandas-based cleaning and transformation
   - Query builder for dynamic WHERE clauses
   - Data validation and missing-value handling

3. Analytics Layer
   - Salary projections
   - Tier parity analysis
   - DSA skill band grouping
   - Comparative analytics outputs

## 5. Component Breakdown

### 5.1 Data Ingestion Module
File: `Project/Database.py`

Responsibilities:
- validate file presence,
- initialize the MySQL database,
- load CSV into MySQL using pandas,
- fill missing numeric values,
- create indexes for common filtering columns,
- expose SQL execution helpers.

Main functions:
- `ensure_database()`
- `init_db(csv_path: str = CSV_PATH)`
- `run_query(query: str, params: tuple = ())`

### 5.2 Query Builder Module
File: `Project/query_builder.py`

Responsibilities:
- generate dynamic SQL filters based on user-selected parameters,
- build WHERE conditions for tier, branch, CGPA, DSA score, and placement status,
- return the SQL clause and parameter dictionary.

Main function:
- `build_parameterized_filter(...)`

This component is designed to support reusable and parameterized SQL generation instead of embedding raw SQL all over the codebase.

### 5.3 Analytics Module
File: `Project/analytics.py`

Responsibilities:
- calculate future salary projections,
- create skill-bands using DSA problem-solving levels,
- compare package salary alignment across college tiers,
- prepare structured output for reporting.

Main function:
- `compute_future_projections()`

It returns:
- `dsa_curve`: aggregated salary data by DSA solve range
- `tier_parity`: mean salary comparison among skill bands and college tiers

## 6. Data Flow

### Import Flow
1. User provides a placement CSV file.
2. `Database.init_db()` reads the file.
3. Missing values are cleaned using median-based imputation.
4. Data is inserted into the `students` table in MySQL.
5. Indexes are created on key filtering columns.

### Query Flow
1. User specifies filters like tier and CGPA range.
2. `build_parameterized_filter()` creates the WHERE clause and parameters.
3. `run_query()` executes the SQL statement.
4. The result is returned as a Pandas DataFrame.

### Analytics Flow
1. Query result is loaded from the database.
2. `compute_future_projections()` bins DSA scores into ranges.
3. The system computes average salary by DSA range.
4. It groups data into skill categories such as foundational, intermediate, and advanced.
5. It outputs JSON-like dictionaries for later reporting or visualization.

## 7. Technology Stack

- Python 3.x
- Pandas for data wrangling and aggregation
- SQLAlchemy for DB interaction
- PyMySQL driver for MySQL
- MySQL Workbench / local MySQL instance for persistence

## 8. Database Design

The system uses a single primary table named `students`.

### Core Data Entities

#### Student
Represents one record in the placement dataset.

Fields include:
- College_Tier
- Branch
- CGPA
- DSA_Problems_Solved
- Placement_Status
- Package_LPA
- GitHub_Contributions
- Open_Source_Contribution
- LinkedIn_Activity_score

### Index Strategy
The system creates indexes on fields commonly used for filtering and grouping:
- `College_Tier`
- `Branch`
- `Placement_Status`
- `CGPA`
- `DSA_Problems_Solved`

This improves performance when running filtered queries and summary analysis.

## 9. Architectural Patterns

### 9.1 Layered Architecture
The project separates concerns into storage, query, and analytics layers. This reduces coupling and makes future changes easier.

### 9.2 Parameterized Query Design
The query builder avoids direct string interpolation where possible and binds values as parameters. This reduces SQL error risk and improves maintainability.

### 9.3 Dataframe-Based Analysis
Pandas is used for transformation and aggregation because it is simple, expressive, and suitable for exploratory analytics.

## 10. Key Design Considerations

### Scalability
The current solution is designed for a moderate-size dataset and local development. It is not yet optimized for large-scale enterprise workloads or concurrent users.

### Maintainability
The system should remain easy to read and modify for academic projects. The use of small functions and clear responsibility boundaries supports this.

### Security
Current implementation stores database credentials in code. That is acceptable for a learning project but should be replaced with environment variables or a secure secrets manager before production use.

### Data Quality
The project handles null values during import to reduce broken aggregation and invalid analysis results.

## 11. System Constraints

- Local MySQL database is required for the current workflow.
- Dataset must be available in CSV format.
- Code is optimized for scripting and analytics rather than a full web application.
- The application is not yet packaged as a deployable service.

## 12. Risks and Limitations

- Hardcoded database credentials may leak sensitive configuration.
- The query builder contains some incomplete or inconsistent logic and may need cleanup.
- The analytics layer is based on heuristic segmentation and may require domain validation.
- Current architecture does not include automated tests, CI/CD, or deployment pipelines.

## 13. Future Architecture Evolution

### Short-Term Improvements
- Add environment-based configuration management.
- Add unit tests for filtering logic and analytics outputs.
- Validate SQL logic against real dataset edge cases.

### Mid-Term Improvements
- Add a dashboard layer using Streamlit or Power BI.
- Introduce API endpoints for querying analytics.
- Support more datasets and schema validation.

### Long-Term Improvements
- Deploy to a cloud environment.
- Add ML-based placement prediction and salary forecasting.
- Introduce multi-user access, authentication, and reporting features.

## 14. Summary

The architecture is intentionally lightweight and focused on data analysis. It brings together CSV ingestion, SQL persistence, query generation, and analytical modeling in a simple and extensible structure. The system already demonstrates the core workflow required for placement analytics and provides a solid base for future dashboards and more advanced decision-support tools.
