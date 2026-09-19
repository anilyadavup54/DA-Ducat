# Excel Learning Guide

A practical quick-reference for Excel formulas, cell references, data cleaning, error handling, and everyday productivity shortcuts.

> **Course focus:** Build reliable spreadsheets by combining formulas, built-in functions, clean references, dynamic arrays, and repeatable data-cleaning techniques.

## At A Glance

| Area | What you will practice |
| --- | --- |
| Dynamic Arrays | Generate sequences and random data with `SEQUENCE` and `RANDARRAY` |
| Calculations | Write formulas, use functions, calculate totals, and work with percentages |
| Cell References | Use relative, absolute, and mixed references correctly |
| Data Cleaning | Trim spaces, change text case, split values, and remove duplicates |
| Reliability | Handle calculation errors with `IFERROR` |
| Productivity | Resize rows and columns, insert or delete cells, and paste values |

## Snapshot

### Most-used Excel tools

- `XLOOKUP` / `VLOOKUP` — search values quickly
- `SUMIFS` / `COUNTIFS` — summarize by conditions
- `IF` / `IFS` — add logic and decision-making
- `INDEX` + `MATCH` — flexible lookup alternative
- `PivotTable` — fast summary and reporting
- `TRIM` / `TEXTJOIN` / `CONCAT` — clean and combine text
- `IFERROR` — avoid ugly spreadsheet errors

### Quick real-world use

```excel
=XLOOKUP(A2, Sheet2!A:A, Sheet2!B:B, "Not Found")
=SUMIFS(C:C, A:A, "Aman", B:B, "2026")
=IFERROR(D2/E2, "No result")
```

## Contents

- [Quick Function Reference](#quick-function-reference)
- [Formula and Function Basics](#formula-and-function-basics)
- [Dynamic Array Formulas](#dynamic-array-formulas)
- [Totals and Percentages](#totals-and-percentages)
- [Cell References](#cell-references)
- [Linking Worksheets](#linking-worksheets)
- [Text Cleaning and Formatting](#text-cleaning-and-formatting)
- [Error Handling](#error-handling)
- [Removing Duplicates](#removing-duplicates)
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [Practice Table](#practice-table)
- [Suggested Study Flow](#suggested-study-flow)

## Quick Function Reference

### Sample Data for Examples

Use this simple employee table for the examples below:

| Employee ID | Name | Department | Salary | Score | Joining Date | Status |
| --- | --- | --- | ---: | ---: | --- | --- |
| 101 | Aman | Sales | 35000 | 82 | 15-01-2024 | Active |
| 102 | Neha | HR | 42000 | 90 | 05-07-2023 | Active |
| 103 | Ravi | IT | 48000 | 76 | 10-02-2024 | Active |
| 104 | Pooja | Sales | 39000 | 88 | 12-12-2023 | On Leave |
| 105 | Simran | Finance | 55000 | 95 | 20-03-2024 | Active |

### Lookup & Reference

- VLOOKUP — Look up a value in the first column of a range. Example: `=VLOOKUP(102, A2:G6, 4, FALSE)` returns `42000`.
- HLOOKUP — Same as VLOOKUP but horizontal. Example: `=HLOOKUP("Salary", A1:G1, 3, FALSE)` returns the value from the Salary column in row 3.
- INDEX — Return a value at a given row/column position. Example: `=INDEX(D2:D6, 3)` returns `48000`.
- MATCH — Return the position of a value in a range. Example: `=MATCH(104, A2:A6, 0)` returns `4`.
- INDEX + MATCH — Flexible lookup combo. Example: `=INDEX(B2:B6, MATCH(105, A2:A6, 0))` returns `Simran`.
- XLOOKUP — Modern replacement for VLOOKUP/HLOOKUP. Example: `=XLOOKUP(103, A2:A6, C2:C6)` returns `IT`.
- OFFSET — Return a reference shifted from a starting point. Example: `=OFFSET(A2, 2, 3)` points to the cell 2 rows down and 3 columns right from `A2`.
- CHOOSE — Pick a value from a list by index number. Example: `=CHOOSE(2, "Aman", "Neha", "Ravi", "Pooja", "Simran")` returns `Neha`.
- INDIRECT — Convert text into a cell reference. Example: `=INDIRECT("B"&3)` returns the value in cell `B3`.

### Math & Aggregation

- SUM — Add values. Example: `=SUM(D2:D6)` returns `219000`.
- SUMIF — Sum values for one condition. Example: `=SUMIF(C2:C6, "Sales", D2:D6)` returns `74000`.
- SUMIFS — Sum with multiple conditions. Example: `=SUMIFS(D2:D6, C2:C6, "Sales", F2:F6, "Active")` returns `35000`.
- AVERAGE — Mean of values. Example: `=AVERAGE(E2:E6)` returns `86.2`.
- AVERAGEIF — Average for one condition. Example: `=AVERAGEIF(C2:C6, "IT", E2:E6)` returns `76`.
- AVERAGEIFS — Average with multiple conditions. Example: `=AVERAGEIFS(E2:E6, C2:C6, "Sales", G2:G6, "Active")` returns `85`.
- COUNT — Count numeric cells. Example: `=COUNT(E2:E6)` returns `5`.
- COUNTA — Count non-empty cells. Example: `=COUNTA(B2:B6)` returns `5`.
- COUNTIF — Count values meeting one condition. Example: `=COUNTIF(C2:C6, "Sales")` returns `2`.
- COUNTIFS — Count values with multiple conditions. Example: `=COUNTIFS(C2:C6, "Sales", G2:G6, "Active")` returns `1`.
- ROUND / ROUNDUP / ROUNDDOWN — Control decimal precision. Example: `=ROUND(85.678, 1)` returns `85.7`.
- SUBTOTAL — Aggregate while ignoring filtered rows. Example: `=SUBTOTAL(9, D2:D6)` gives total of visible values.
- PRODUCT — Multiply values. Example: `=PRODUCT(E2:E6)` multiplies all five scores.

### Logical

- IF — Conditional logic. Example: `=IF(E2>=85, "High Performer", "Needs Improvement")` returns `High Performer` for Aman.
- IFS — Evaluate multiple conditions efficiently. Example: `=IFS(E2>=90, "Excellent", E2>=80, "Good", TRUE, "Average")` returns `Good` for Aman.
- AND — True if all conditions pass. Example: `=AND(E2>=80, C2="Sales")` returns `TRUE` for Aman.
- OR — True if any condition passes. Example: `=OR(C2="HR", E2>=90)` returns `TRUE` for Neha.
- NOT — Reverse a logical value. Example: `=NOT(E2<80)` returns `TRUE` for Aman.
- IFERROR — Handle errors gracefully. Example: `=IFERROR(D2/E2, "Invalid")` avoids a divide-by-zero or invalid calculation.
- IFNA — Handle #N/A errors specifically. Example: `=IFNA(XLOOKUP(106, A2:A6, B2:B6), "Not Found")` returns `Not Found`.
- NESTED IF — Multiple layered conditions. Example: `=IF(E2>=90, "Excellent", IF(E2>=80, "Good", "Average"))` returns `Good` for Aman.

### Text Functions

- CONCATENATE / CONCAT — Join text strings. Example: `=CONCAT(B2, " - ", C2)` returns `Aman - Sales`.
- TEXTJOIN — Join text with a delimiter, skipping blanks. Example: `=TEXTJOIN(" | ", TRUE, B2:C2)` returns `Aman | Sales`.
- LEFT / RIGHT / MID — Extract text. Example: `=LEFT(B2, 3)` returns `Ama`.
- LEN — Length of text string. Example: `=LEN(B2)` returns `4` for Aman.
- TRIM — Remove extra spaces. Example: `=TRIM("  Aman   Yadav  ")` returns `Aman Yadav`.
- UPPER / LOWER / PROPER — Change text case. Example: `=UPPER(B2)` returns `AMAN`.
- SUBSTITUTE — Replace specific text. Example: `=SUBSTITUTE(B2, "A", "X")` changes Aman to Xman.
- FIND / SEARCH — Locate text within a string. Example: `=FIND("n", B2)` returns `2` for Aman.
- TEXT — Format numbers and dates as text. Example: `=TEXT(D2, "$#,##0")` returns `$35,000`.

### Date & Time

- TODAY() / NOW() — Current date and time. Example: `=TODAY()` returns the current date.
- DATE — Build a date from year/month/day. Example: `=DATE(2026, 9, 19)` returns the date `19-09-2026`.
- DATEDIF — Difference between two dates. Example: `=DATEDIF(F2, TODAY(), "Y")` returns years since joining.
- EOMONTH — Last day of a month. Example: `=EOMONTH(TODAY(), 0)` returns the end of the current month.
- NETWORKDAYS — Working days between two dates. Example: `=NETWORKDAYS(F2, TODAY())` returns working days since joining.
- WORKDAY — Date after adding working days. Example: `=WORKDAY(TODAY(), 10)` returns 10 working days from today.

### Financial

- NPV — Net present value. Example: `=NPV(10%, 1000, 1500, 2000)` calculates the present value of future cash flows.
- IRR — Internal rate of return. Example: `=IRR({-5000, 2000, 3000, 4000})` estimates the project return rate.
- PMT — Loan or EMI payment calculation. Example: `=PMT(8%/12, 12, 100000)` estimates the monthly EMI.
- FV / PV — Future value / present value. Example: `=FV(8%/12, 12, -500, 0)` calculates the future value of monthly savings.

### Data Analysis / Modern Tools

- PivotTables + GETPIVOTDATA + UNIQUE + SORT + FILTER — Dynamic arrays and data summarization. Example: `=UNIQUE(C2:C6)` returns the department names without repetition.
- GETPIVOTDATA — Pull values from a PivotTable. Example: `=GETPIVOTDATA("Salary", $A$1, "Department", "Sales")` returns the Sales total from the PivotTable.
- SORT — Sort values. Example: `=SORT(B2:B6)` sorts employee names alphabetically.
- FILTER — Filter values to match a condition. Example: `=FILTER(B2:B6, C2:C6="Sales")` returns `Aman` and `Pooja`.

> In real-world reporting work, VLOOKUP or XLOOKUP, SUMIFS, COUNTIFS, IF, IFERROR, INDEX-MATCH, and PivotTables are the most commonly used Excel tools for dashboards, finance, and operational reports.

## Formula and Function Basics

A **formula** is an expression created by the user to calculate a result. A **function** is a built-in operation that performs a common calculation.

### Formula

```excel
=B1+B2+B3
```

### Function

```excel
=SUM(E1:E5)
```

Functions are usually easier to read, copy, and maintain than long manually written formulas.

## Dynamic Array Formulas

Dynamic-array formulas can return multiple values from one formula cell. The results automatically spill into nearby empty cells.

### `SEQUENCE`

Syntax:

```excel
=SEQUENCE(rows, [columns], [start], [step])
```

Examples:

```excel
=SEQUENCE(5)
=SEQUENCE(3, 2, 10, 5)
```

The second example creates 3 rows and 2 columns beginning at 10 and increasing by 5:

```text
10  15
20  25
30  35
```

### `RANDARRAY`

Syntax:

```excel
=RANDARRAY([rows], [columns], [min], [max], [integer])
```

Examples:

```excel
=RANDARRAY(5, 1, 1, 100, TRUE)
=RANDARRAY(3, 2, 0, 1, FALSE)
```

Use `TRUE` for random integers and `FALSE` for random decimal values. Because random formulas recalculate, use **Copy > Paste Values** when you need to freeze the generated results.

## Totals and Percentages

### AutoSum

To total values in cells `E2:E10`:

```excel
=SUM(E2:E10)
```

The AutoSum button usually detects the nearby range automatically. The keyboard shortcut is:

```text
Alt + =
```

### Percentage of Total

If `B2` contains an individual value and `B10` contains the total:

```excel
=B2/$B$10
```

Format the result as a percentage and copy it down. The absolute reference keeps the total cell fixed while the individual value changes by row.

An alternative calculates the total directly:

```excel
=B2/SUM($B$2:$B$9)
```

### Percentage Change

```excel
=(C2-B2)/B2
```

This calculates the change from an old value in `B2` to a new value in `C2`.

## Cell References

Excel has three main reference types.

| Type | Example | Behavior when copied |
| --- | --- | --- |
| Relative | `C5` | Row and column both change |
| Absolute | `$C$5` | Row and column both stay fixed |
| Mixed | `C$5` or `$C5` | One part stays fixed |

### Relative Reference

```excel
=C5*D5
```

When copied one row down, it becomes `=C6*D6`.

### Absolute Reference

Use an absolute reference for a fixed tax rate or target stored in one cell:

```excel
=B2*$F$2
```

The `$F$2` reference remains fixed when copied.

### Mixed Reference

Use a mixed reference when copying across rows or columns:

```excel
=$B3*C$2
```

Here, column `B` stays fixed for the first reference, while row `2` stays fixed for the second reference.

Press `F4` while editing a reference to cycle through relative, absolute, and mixed forms.

## Linking Worksheets

To reference a value from another worksheet:

```excel
='Sales Data'!B2
```

For a range on another sheet:

```excel
=SUM('Sales Data'!E2:E10)
```

Single quotes are especially useful when a sheet name contains spaces or special characters.

## Text Cleaning and Formatting

### Remove Extra Spaces

```excel
=TRIM(A2)
```

`TRIM` removes leading and trailing spaces and reduces repeated spaces between words.

### Change Text Case

```excel
=PROPER(TRIM(A2))
=UPPER(A2)
=LOWER(A2)
```

A common cleanup formula is:

```excel
=PROPER(TRIM(A2))
```

It removes unwanted spaces and capitalizes the first letter of each word.

### Split Data into Separate Columns

For values such as `Aman Yadav` in `A2`, the modern formula approach is:

```excel
=TEXTSPLIT(A2, " ")
```

For older Excel versions, use **Data > Text to Columns**, select a delimiter such as comma or space, preview the result, and choose the destination cells.

### Combine Values from Different Columns

```excel
=A2&" "&B2
```

Or use:

```excel
=TEXTJOIN(" ", TRUE, A2:B2)
```

`TEXTJOIN` can ignore empty cells when its second argument is `TRUE`.

## Error Handling

### `IFERROR`

Return a friendly fallback when a formula produces an error:

```excel
=IFERROR(I3/H3, "NULL")
```

A more informative alternative is:

```excel
=IFERROR(I3/H3, "Not available")
```

This is useful for division by zero, missing lookups, and invalid calculations. Use it carefully: hiding every error can make data-quality problems harder to find.

### Common Error Checks

```excel
=IF(H3=0, "No denominator", I3/H3)
=IFERROR(XLOOKUP(A2, Product[ID], Product[Name]), "Not found")
```

## Removing Duplicates

To remove duplicate records through the interface:

1. Select the complete data range or table.
2. Open **Data > Remove Duplicates**.
3. Select the columns that define a duplicate.
4. Confirm the result and review the number of removed records.

For a formula-based unique list:

```excel
=UNIQUE(A2:A100)
```

To return sorted unique values:

```excel
=SORT(UNIQUE(A2:A100))
```

Keep a copy of the original data before removing duplicates when the operation cannot be undone safely.

## Keyboard Shortcuts

| Action | Shortcut |
| --- | --- |
| AutoSum | `Alt + =` |
| AutoFit row height | `Alt + H + O + A` |
| AutoFit column width | `Alt + H + O + I` |
| Insert row or column | `Ctrl + Shift + +` |
| Delete row or column | `Ctrl + -` |
| Paste special / paste values | `Ctrl + Shift + V` |
| Cycle cell reference types | `F4` while editing a reference |

### AutoFit Notes

- Select the row or column before using the AutoFit command.
- Double-click the boundary between row numbers or column letters for a quick AutoFit.
- AutoFit is useful after changing text, wrapping cells, or importing data.

## Practice Table

Create a table with these columns to practice the formulas in this guide:

| Student | Subject | Marks | Total Marks | Percentage | Result |
| --- | --- | ---: | ---: | ---: | --- |
| Aman | Python | 88 | 100 |  |  |
| Anil | SQL | 76 | 100 |  |  |
| Neha | Excel | 92 | 100 |  |  |

Example formulas for row 2:

```excel
E2 = C2/D2
F2 = IFERROR(IF(E2>=0.5, "Pass", "Needs improvement"), "Check marks")
```

Format column `E` as a percentage, then copy both formulas down the table. Add a fixed passing threshold in `H1` and use an absolute reference:

```excel
F2 = IF(E2>=$H$1, "Pass", "Needs improvement")
```

## Suggested Study Flow

1. Start with formulas, functions, AutoSum, and percentage calculations.
2. Practice relative, absolute, and mixed references by copying formulas across rows and columns.
3. Link worksheets and build a small multi-sheet report.
4. Clean imported text with `TRIM`, case functions, splitting, and duplicate removal.
5. Add `IFERROR` and validation checks to make the workbook reliable.
6. Finish with dynamic arrays such as `SEQUENCE`, `RANDARRAY`, `UNIQUE`, and `SORT`.

## Learning Outcomes

By the end of this guide, you should be able to:

- Distinguish formulas from built-in Excel functions.
- Generate sequences and random test data with dynamic arrays.
- Calculate totals, percentages, and percentage changes.
- Use relative, absolute, and mixed cell references confidently.
- Reference data across worksheets.
- Clean and split text and combine values into readable labels.
- Handle calculation errors without hiding important data problems.
- Identify and remove duplicate records safely.
- Use essential Excel shortcuts to work faster.

## Source Material

- [`excel.txt`](excel.txt) - Original Excel notes and shortcut list.
- [`../README.md`](../README.md) - Repository overview.
