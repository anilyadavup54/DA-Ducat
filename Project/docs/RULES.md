# Project Rules

## 1. Purpose
This file defines the working rules for the Campus Placement Analytics project. These rules are intended to keep the project maintainable, consistent, and understandable as it grows.

## 2. Core Principles

### 2.1 Keep responsibilities separated
- `Database.py` handles database creation, import, and querying.
- `query_builder.py` handles SQL filter construction.
- `analytics.py` handles calculations and generated insights.
- Documentation files describe product intent, architecture, and team memory.

Do not mix database setup logic with analytical calculations in the same function.

### 2.2 Prefer clarity over cleverness
Code should be easy to read and follow. Use descriptive variable names and straightforward logic instead of compact but difficult-to-understand patterns.

### 2.3 Validate assumptions before building on them
Before using a column name, field, or derived metric, confirm that it exists in the dataset or in the database schema. Do not rely on guesswork.

### 2.4 Handle missing data explicitly
Missing values should not be silently ignored. Use a defined filling or filtering strategy explaining how blank values are treated.

### 2.5 Use parameterized SQL
Filter values should be passed as parameters where possible to avoid broken SQL strings and reduce injection risk.

## 3. Coding Rules

### 3.1 Naming conventions
- Use descriptive, lowercase names for Python variables and functions.
- Avoid cryptic abbreviations unless they are standard domain terms.
- Keep functions focused on a single job.

### 3.2 File responsibilities
- Do not place ingestion code in the analytics module.
- Do not place query logic inside the data import module.
- Do not hardcode business logic across multiple modules when it can be centralized.

### 3.3 Data handling rules
- Always verify file existence before import.
- Always check important column names before analysis.
- Always document assumptions about the data source.

## 4. Documentation Rules

- Every major feature should be described in the docs.
- Keep PRD, architecture, design, memory, and rules aligned with the project reality.
- If a design decision changes, update the relevant documentation with the change.

## 5. Security Rules
- Do not store production secrets in source files.
- Replace hardcoded MySQL credentials before deployment.
- Use environment variables or a secrets manager in any future production environment.

## 6. Quality Rules
- Use simple, testable logic.
- Prefer small functions over large monolithic ones.
- Review outputs for accuracy before treating them as final analysis.
- If a business metric is derived, document how it was calculated.

## 7. Design Constraints
- The project remains a learning and prototype platform unless new requirements say otherwise.
- Local MySQL is the default storage model for now.
- Analytics should remain understandable to students and early developers.

## 8. Contribution Rules
- New functions should match the project’s modular architecture.
- New features should be documented in the relevant design or memory files.
- Changes that affect the dataset schema or import flow must be reflected in the architecture and memory notes.

## 9. Decision Rules
When a decision is unclear:
1. check the project docs,
2. confirm the current code behavior,
3. apply the least-complex solution,
4. document the decision and its tradeoff.

## 10. Final Rule
The project should stay practical, understandable, and reusable. The goal is not just to write code, but to build a clear analytics workflow that can be extended by future learners and contributors.
