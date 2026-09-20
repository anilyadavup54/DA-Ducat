# DA-Ducat

Course notes, exercises, and data-analytics projects collected while studying data science and analytics.

## Repository Structure

| Path | Contents |
| --- | --- |
| `Excel/` | Excel formulas, references, shortcuts, text cleanup, error handling, and data-cleaning notes. |
| `Power BI/` | Power BI study notes and syllabus material. |
| `Python/` | Python notes, exercises, a Jupyter notebook, and a student-management example. |
| `SQL/` | SQL study notes and syllabus material. |
| `Statistics & Analytics/` | Statistics and analytics notes, syllabus material, and a notebook. |
| `ML/` | Machine-learning study material. |
| `Deep Learning & Neural Networks/` | Deep-learning notes and syllabus material. |
| `Project/` | Campus placement analytics prototype and its supporting documentation. |

## Python Learning Material

`Python/D_Notes.ipynb` contains examples and exercises covering:

- Operators, strings, collections, type casting, and common methods
- Conditional statements, `match`/`case`, loops, and jump statements
- Number problems such as factorials, prime checks, averages, and Fibonacci series
- Formatting, iterators, comprehensions, functions, recursion, `lambda`, `map`, `filter`, and `reduce`
- A student-management system

Run the standalone student-management example with Python 3.10 or newer:

```bash
python Python/Test.py
```

Open the notebook in VS Code or Jupyter and run cells individually. Some cells are interactive and are not designed to run as one script.

## Campus Placement Analytics

The `Project/` directory contains a Python and MySQL prototype for analyzing engineering placement outcomes. It works with `Project/indian_engineering_placement_2026.csv` and is organized into:

- `Database.py`: creates the database, cleans CSV data, loads the `students` table, and runs queries.
- `query_builder.py`: builds parameterized filters for tiers, branches, CGPA, DSA scores, and placement status.
- `analytics.py`: calculates DSA-based salary curves and college-tier comparisons.
- `docs/`: project requirements, architecture, design notes, rules, memory, and task tracking.

### Project Prerequisites

- Python 3.10 or newer
- MySQL running locally
- Python packages: `pandas`, `numpy`, `SQLAlchemy`, and `PyMySQL`

Install the packages in the active Python environment:

```bash
python -m pip install pandas numpy SQLAlchemy PyMySQL
```

Before running the database workflow, update the MySQL settings and CSV path at the top of `Project/Database.py`. The current file contains development credentials and a machine-specific Windows path, so do not use those values in production or commit real credentials.

To load the dataset:

```bash
cd Project
python Database.py
```

The analytics module expects the `students` table to exist and is intended to be imported after the database has been initialized.

## Current Status

- Python and Excel materials are the most developed study sections.
- The placement analytics prototype has a documented ingestion, query, and analytics design, but it still requires local MySQL configuration and further testing before production use.
- The remaining subject folders contain ongoing notes and syllabus material.
