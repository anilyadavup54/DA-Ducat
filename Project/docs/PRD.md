# Product Requirements Document (PRD)

## 1. Product Overview

### Product Name
Campus Placement Analytics Platform

### Summary
This product is a data-driven analytics solution built for analyzing engineering placement outcomes across colleges, branches, CGPA ranges, DSA performance, and salary trends. It helps institutions, career services teams, and students understand placement patterns and identify the factors that influence package outcomes.

The project ingests a placement dataset, loads it into a structured database, supports filtering and query generation, and calculates analytical insights such as package projections, skill-band comparisons, and placement trends.

## 2. Problem Statement

Engineering placement data is often scattered across CSV files, spreadsheets, and manual reports. This makes it difficult for institutions and students to:

- assess which colleges and branches perform best,
- understand the relationship between CGPA, DSA skills, and salary,
- evaluate the impact of project work or open-source contribution,
- generate filtered insights for decision-making,
- compare placement outcomes across tiers and departments.

The current product addresses this by centralizing the data, standardizing the import process, and providing query-driven analytics for business and academic insight.

## 3. Goals and Objectives

### Primary Goals
- Build a clean and reusable placement analytics workflow.
- Convert raw student placement data into a queryable database.
- Support targeted filtering by college tier, branch, CGPA, DSA score, and placement status.
- Generate meaningful reports and projections for salary and skill trends.
- Provide a foundation for future dashboards and reporting tools.

### Secondary Goals
- Help students identify the skills associated with higher salary outcomes.
- Support institutional benchmarking across colleges and branches.
- Prepare data for predictive or descriptive analytics use cases.

## 4. Target Users

### 4.1 Students
Students want to understand how their CGPA, DSA score, and skill profile compare with successful placements.

### 4.2 Placement Coordinators
Placement teams need quick filters and summary analysis to evaluate outcomes by college tier and branch.

### 4.3 Academic Administrators
Administrators need trend-level insight into placement performance and student readiness across departments.

### 4.4 Data Analysts / Researchers
Analysts can extend the project with new feature engineering, segmentation, or model-based forecasting.

## 5. Core Use Cases

### Use Case 1: Load Placement Data
A user uploads a CSV containing placement records and the system validates and imports the data into a MySQL database.

### Use Case 2: Filter Candidate Pools
A user selects filters such as college tier, branch, CGPA range, minimum DSA score, and placement status, then runs a query to extract relevant student records.

### Use Case 3: Compare Salary Across Skill Bands
A user analyzes how salary changes across foundational, intermediate, and advanced DSA skill groups.

### Use Case 4: Review Package Projections
A user studies projected salary growth based on DSA skill levels and technical milestone trends.

### Use Case 5: Explore Tier-wise Placement Parity
A user compares placement outcomes across college tiers and skill groups to understand whether premium packages are more common in elite institutions or among stronger technical performers.

## 6. Functional Requirements

### FR1: Data Import
The system shall load a CSV file into a relational database.

Requirements:
- Support the placement dataset file provided in the project.
- Validate that the file exists before import.
- Read the dataset with Pandas.
- Fill missing numeric values using safe statistical defaults such as median imputation.
- Store data in a table named `students`.

### FR2: Database Initialization
The system shall create the target database if it does not already exist.

Requirements:
- Connect to the MySQL server.
- Create the database instance when missing.
- Reuse the database connection for subsequent queries.

### FR3: Query Execution
The system shall run SQL queries against the database using SQLAlchemy.

Requirements:
- Accept SQL query strings.
- Return results as a DataFrame for analysis.
- Support parameterized queries where required.

### FR4: Filtered Query Builder
The system shall construct a WHERE clause for dataset filtering based on user-selected criteria.

Supported filters:
- college tier
- branch
- CGPA range
- minimum DSA problems solved
- placement status

### FR5: Placement Analytics
The system shall analyze placement records to derive insights such as:
- average salary by DSA skill band,
- average salary by college tier,
- projected LPA growth by technical milestone band,
- skill-based placement comparisons.

### FR6: Insight Output
The system shall return analytical results in a structured format suitable for further processing in Python.

Requirements:
- Results should be serializable to JSON-like dictionaries.
- Output should include aggregated records and comparison tables.

### FR7: Reporting Support
The system shall expose result sets that can be used in reporting and dashboard creation.

## 7. Non-Functional Requirements

### Performance
- The system should handle moderately sized datasets efficiently.
- Indexing should be added to commonly filtered fields such as college tier, branch, placement status, CGPA, and DSA score.

### Reliability
- The system should fail gracefully if the source CSV is missing or the database is unavailable.
- Null handling should be included before writing the data to the database.

### Maintainability
- Code should be readable and modular.
- Database logic, query generation, and analytics logic should remain separated by responsibility.

### Security
- Database credentials should be managed securely rather than hardcoded in production environments.
- Confidential credentials should not be committed directly to source control.

## 8. Data Model

### Primary Table: students
The core table contains student-level information such as:

- Student identifier
- College tier
- Branch
- CGPA
- DSA problems solved
- Placement status
- Package LPA
- GitHub contribution
- LinkedIn activity score
- Open-source contribution
- Other relevant profile fields from the dataset

### Key Analytical Fields
- `College_Tier`
- `Branch`
- `CGPA`
- `DSA_Problems_Solved`
- `Placement_Status`
- `Package_LPA`
- `GitHub_Contributions`
- `Open_Source_Contribution`
- `LinkedIn_Activity_score`

## 9. Business Rules

1. Students are included in analytics only if they have valid records in the imported dataset.
2. Filters should support multi-valued input such as multiple branches or multiple tiers.
3. Placement status can be used to restrict analysis to only placed students or all students.
4. DSA skill bands should be calculated from the distribution of solved problems.
5. Salary projection should be derived from the skill band and market growth assumptions.

## 10. User Experience Requirements

- The workflow should feel simple: import data, run filters, then view analytical summaries.
- Results should be clear enough for both technical and non-technical users.
- Queries and outputs should be consistent across repeated runs.

## 11. Acceptance Criteria

### Acceptance Criteria 1: CSV Import
Given a valid CSV dataset, when the user runs the import process, then the data is loaded into the `students` table without errors.

### Acceptance Criteria 2: Missing Values Handling
Given missing numeric values in the dataset, when the import process runs, then those values are filled using a defined fallback strategy.

### Acceptance Criteria 3: Filtered Query Generation
Given a set of filters such as tier and CGPA range, when the user generates the query, then the system returns only matching records.

### Acceptance Criteria 4: Placement Insight Generation
Given a dataset with placement records, when the analytics function runs, then it produces package trends, skill-band summaries, and tier parity outputs.

### Acceptance Criteria 5: Database Indexing
Given the dataset has been imported, when the system initializes the database, then indexes are created for the main filtering fields.

## 12. Assumptions and Constraints

- The project uses a local MySQL environment for storage.
- The dataset is a campus placement CSV file for Indian engineering institutions.
- The current solution targets desktop-based analytics workflows and Python processing.
- Production deployment and secure credential management are not yet fully implemented.

## 13. Risks and Challenges

- Hardcoded database credentials create security risk.
- Some SQL query logic and parameter binding may require cleanup for correctness.
- Data quality issues in the source CSV may affect analysis quality.
- Current filter logic and query builder require validation against real-world dataset behavior.

## 14. Future Enhancements

- Add a dashboard UI with charts and filters.
- Support cloud-hosted databases and deployed analytics services.
- Add predictive modeling for salary and placement probability.
- Introduce role-based access and authentication.
- Export reports in CSV, Excel, and PDF format.
- Create automated tests for import, filter, and aggregation logic.

## 15. Release Scope

### Current Scope
- CSV import
- MySQL database initialization
- Query building and filtering
- Placement analytics summary
- Salary and skill-band projections

### Out of Scope for Initial Release
- Real-time dashboards
- AI-based recommendation engine
- Multi-user web app
- Full enterprise deployment architecture

## 16. Definition of Done

The project is considered complete when:

- the CSV dataset successfully loads into the database,
- core filters return expected student subsets,
- salary and skill-band analytics are generated,
- results are structured and reusable for downstream reporting,
- the codebase is documented enough for future team members to extend it.

## 17. Appendix: Example Product Flow

1. User places the placement dataset file in the project directory.
2. The system reads the CSV and cleans missing values.
3. Data is written to the `students` table in MySQL.
4. User chooses filters such as `College_Tier`, `Branch`, and `CGPA` range.
5. Query builder constructs a SQL WHERE clause.
6. The system runs the query and returns the filtered dataset.
7. The analytics layer computes DSA salary bands, tier parity, and projections.
8. The output is used for reporting, benchmarking, and decision support.
