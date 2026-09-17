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

## Contents

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
