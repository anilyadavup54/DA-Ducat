# DA-Ducat

Study notes and practice material from a data analytics course. The repository is organized by subject and currently combines written notes, Python exercises, a Jupyter notebook, and recorded lectures.

## Repository Contents

| Folder | Contents |
| --- | --- |
| `Excel/` | Excel formulas, cell references, keyboard shortcuts, text cleanup, error handling, and data-cleaning notes. |
| `Power BI/` | Placeholder notes for Power BI. |
| `Python/` | Python fundamentals, practice exercises, a notebook, and a student-management program. |
| `Python/Lectures/` | Recorded lecture videos from 7 and 8 September. |
| `SQL/` | Placeholder notes for SQL. |
| `Statistics/` | Placeholder notes for Statistics. |

## Python Topics

`Python/D_Notes.ipynb` contains progressive examples and exercises covering:

- Comparison, logical, membership, identity, walrus, and bitwise operators
- Strings, lists, tuples, dictionaries, nested dictionaries, and sets
- Type casting and common collection methods
- Conditional statements, ternary expressions, and `match`/`case`
- `while` and `for` loops, nested loops, and jump statements
- Number exercises including tables, factorials, prime checks, averages, and Fibonacci series
- String formatting, iterators, list comprehensions, functions, recursion, `lambda`, `map`, `filter`, and `functools.reduce`
- A student-management system project

The notebook is a collection of learning examples. Its cells are not all intended to be run as one script, and several cells require input from the user.

## Running the Python Program

The standalone student-management example is in `Python/Test.py` and uses only the Python standard library.

```bash
python Python/Test.py
```

The program can display, add, remove, and search student records. Use Python 3.10 or newer because the code uses structural pattern matching with `match`/`case`.

To work through the notebook, open `Python/D_Notes.ipynb` in VS Code or Jupyter with a Python 3 kernel, then run cells individually.

## Current Status

- Python notes and exercises are the most complete part of the repository.
- Excel notes are available but informal and still contain unfinished items.
- Power BI, SQL, and Statistics folders currently contain subject headings/placeholders and are ready for additional notes.
- No dependency or build configuration is required at present.
