# Project Tasks

## 1. Current Project Status
The project is in a working prototype stage. Core functionality is present for dataset ingestion, database loading, query-based filtering, and basic analytics generation.

## 2. Immediate Tasks

### Task 1: Validate the database import workflow
- Confirm the MySQL configuration works with the local environment.
- Ensure the CSV path points to the correct dataset file.
- Verify that all required columns exist before import.
- Check that `init_db()` successfully creates the `students` table.

### Task 2: Review and fix query builder reliability
- Validate the generated SQL conditions for each filter.
- Check whether `College_Tier` and `Branch` placeholders are correctly built.
- Verify that the query builder returns valid SQL and parameters for all valid inputs.
- Fix inconsistent naming or placeholder errors in the generated query.

### Task 3: Validate analytics correctness
- Confirm that salary aggregation uses the correct data columns.
- Check whether skill bands are calculated logically from `DSA_Problems_Solved`.
- Ensure `tier_parity` and `dsa_curve` outputs match expected data patterns.
- Verify any formulas or projections remain interpretable and documented.

### Task 4: Improve project configuration
- Move database credentials to environment variables.
- Add a setup guide for local MySQL configuration.
- Document the required directory and dataset paths.

## 3. Short-Term Enhancements

### Task 5: Add basic testing
- Create tests for CSV import and DB initialization.
- Add tests for filter-building logic.
- Add tests for salary aggregation and skill-band calculations.

### Task 6: Improve data quality handling
- Document all missing-value conventions.
- Identify whether categorical values should be normalized.
- Decide whether date and status columns require cleaning before reporting.

### Task 7: Make the output easier to consume
- Serialize analytics outputs as clear JSON-ready structures.
- Add reporting examples for common user queries.
- Standardize output field names across analytics functions.

## 4. Mid-Term Goals

### Task 8: Build a dashboard or notebook workflow
- Create a simple analytical dashboard for placement insights.
- Add charts for salary distribution, department performance, and DSA trends.
- Provide a user-friendly filter interface.

### Task 9: Add API or web layer
- Expose analysis results through Python REST endpoints or a minimal web application.
- Allow users to query filtered outputs without running scripts manually.

### Task 10: Expand business logic
- Add salary comparison by college tier and branch.
- Add placement-rate calculations by skill profile.
- Add historical trend or cohort segmentation features.

## 5. Long-Term Roadmap

### Task 11: Production hardening
- Add secure configuration management.
- Introduce deployment readiness for database and application layers.
- Add monitoring and error reporting.

### Task 12: Advanced analytics
- Add predictive models for placement probability.
- Compare projected salary bands with actual outcomes.
- Use machine learning for better forecasting and recommendations.

### Task 13: Institutional reporting
- Produce downloadable reports for students and placement teams.
- Add exported summaries for departments and colleges.
- Support decision-making based on trend analysis.

## 6. Definition of Completion
The project can be considered ready for broader use when:
- the CSV import workflow is reliable,
- all key filters produce valid SQL results,
- analytics outputs are validated on real data,
- documentation and configuration are consistent,
- and the application can be run by a new user without hidden setup assumptions.

## 7. Suggested Execution Order
1. Fix query generation and database setup.
2. Validate analytics outputs.
3. Add tests and data-quality checks.
4. Build a basic dashboard or notebook UI.
5. Add production-oriented configuration and scaling improvements.
