# Power BI Learning Roadmap

A practical guide to building polished Power BI reports: connect and shape data, model relationships, write DAX, design interactive visuals, and publish insights through Power BI Service.

> **Course focus:** Turn raw tables into a trustworthy semantic model and an interactive report that supports exploration, comparison, and decision-making.

## At A Glance

| Stage | Focus |
| --- | --- |
| Foundations | Business Intelligence, Power BI components, Desktop, and report structure |
| Visualization | Charts, maps, filters, slicers, drill experiences, bookmarks, and tooltips |
| Service | Workspaces, dashboards, publishing, configuration, and sharing |
| Power Query | Shaping, combining, cleaning, parameters, and reusable transformations |
| Modeling and DAX | Relationships, filter context, calculated columns, measures, tables, and time intelligence |

## Contents

- [Prerequisites and Sample Model](#prerequisites-and-sample-model)
- [Introduction to Power BI](#introduction-to-power-bi)
- [Data Visualization](#data-visualization)
- [Power BI Service, Publishing, and Sharing](#power-bi-service-publishing-and-sharing)
- [Power Query: Shaping and Combining Data](#power-query-shaping-and-combining-data)
- [Data Modeling and DAX](#data-modeling-and-dax)
- [Suggested Study Flow](#suggested-study-flow)
- [Learning Outcomes](#learning-outcomes)

## Prerequisites and Sample Model

Install Power BI Desktop from the official Microsoft website. Power BI Desktop is available for Windows; use Power BI Service in a browser for publishing and sharing.

The examples below use a simple star schema:

```text
Date (1) ──── (*) Sales (*) ──── (1) Product
                  |
                  └──────── (*) Customer
```

Suggested columns:

| Table | Example columns |
| --- | --- |
| `Sales` | `OrderDate`, `ProductKey`, `CustomerKey`, `Quantity`, `UnitPrice`, `Discount` |
| `Product` | `ProductKey`, `ProductName`, `Category`, `Subcategory` |
| `Customer` | `CustomerKey`, `CustomerName`, `City`, `Region` |
| `Date` | `Date`, `Year`, `Quarter`, `Month`, `MonthNumber` |

## Introduction to Power BI

### Business Intelligence

Business Intelligence combines data, analysis, and reporting to support better decisions. Common BI tools include Power BI, Tableau, Looker, Qlik, and Excel.

Power BI is an ecosystem made up of:

- **Power BI Desktop** for data loading, Power Query, modeling, DAX, and report design.
- **Power BI Service** for workspaces, dashboards, sharing, refresh, and collaboration.
- **Power BI Mobile** for viewing and interacting with reports on mobile devices.
- **On-premises data gateway** for refreshing data sources that remain inside an organization.

### First Report Workflow

1. Open Power BI Desktop.
2. Select **Get data** and choose a source such as Excel, CSV, SQL Server, or a web connector.
3. Select **Transform data** to open Power Query Editor.
4. Set data types, clean columns, and load the result.
5. Create relationships in **Model view**.
6. Add measures and calculated columns with DAX.
7. Build report pages in **Report view**.
8. Save the `.pbix` file and publish it to a workspace.

## Data Visualization

A good visual answers a specific question. Use column or bar charts for comparisons, line charts for trends, scatter charts for relationships, maps for geography, and tables or matrices for detail.

### Common Visuals

| Business question | Recommended visual |
| --- | --- |
| Which category is largest? | Column or bar chart |
| How is sales changing over time? | Line chart |
| How is a total divided? | Donut or pie chart for a small number of categories |
| Are two measures related? | Scatter chart |
| Where are values concentrated? | Map |
| What is the stage-by-stage count? | Funnel chart |
| What are the exact values? | Table or matrix |

### Creating a Measure for Visuals

Create measures in **Modeling > New measure**, then add them to visual fields:

```DAX
Total Sales =
SUMX(
    Sales,
    Sales[Quantity] * Sales[UnitPrice] * (1 - Sales[Discount])
)

Total Orders =
DISTINCTCOUNT(Sales[OrderID])

Average Order Value =
DIVIDE([Total Sales], [Total Orders])
```

Use `Total Sales` as the value in a column chart, `Date[Month]` as the axis, and `Product[Category]` as the legend.

### Include, Exclude, and Filters

In the visual menu, use **Include** or **Exclude** to focus on selected data points. For reusable filters, use the Filter pane:

- Visual-level filters affect one visual.
- Page-level filters affect every visual on one page.
- Report-level filters affect the complete report.

A DAX equivalent for a filtered measure is:

```DAX
Online Sales =
CALCULATE(
    [Total Sales],
    Sales[Channel] = "Online"
)
```

### Maps and Geographic Data

Set geographic columns to the correct **Data category** such as City, State, Country, or Postal Code. Then place the field in a map visual.

```DAX
Sales by Region =
SUMX(
    VALUES(Customer[Region]),
    [Total Sales]
)
```

Power BI can use `Customer[City]`, `Customer[Region]`, or latitude and longitude fields to locate data. Avoid ambiguous city names by including a state or country field.

### Drill Down and Hierarchies

Create a hierarchy such as `Year > Quarter > Month` in the Fields pane, then add it to a chart axis and enable drill down.

```DAX
Year Label = FORMAT('Date'[Date], "YYYY")
Quarter Label = "Q" & FORMAT('Date'[Date], "Q")
Month Label = FORMAT('Date'[Date], "MMM")
```

Sort `Month Label` by `Date[MonthNumber]` so months appear in calendar order.

### Drill Through and Page Navigation

For a product detail page:

1. Add `Product[ProductName]` to the drill-through filters.
2. Add detail visuals to the page.
3. Right-click a product on another page and select **Drill through**.
4. Add a back button from **Insert > Buttons > Back**.

For page navigation, add a button and set **Action > Type** to **Page navigation**.

### Bookmarks and Selection Pane

Use bookmarks to save a report state, such as selected filters and visible visuals. Use the Selection pane to rename, reorder, show, or hide visuals.

A common interaction pattern is:

1. Create two visual states.
2. Show one state and hide the other in the Selection pane.
3. Capture a bookmark for each state.
4. Connect buttons to the bookmarks.

### Volume and Value Analytics

Compare quantity (volume) with revenue (value) using a combo chart:

```DAX
Units Sold = SUM(Sales[Quantity])

Revenue per Unit = DIVIDE([Total Sales], [Units Sold])
```

Place `Units Sold` on columns and `Total Sales` on the line axis. A dual-axis chart is useful when the measures have very different scales.

### Slicers and Sync Slicers

Add a slicer using fields such as `Date[Year]`, `Product[Category]`, or `Customer[Region]`. In **View > Sync slicers**, choose the report pages that should share the same selection.

A measure that responds to slicers is automatically evaluated in the current filter context:

```DAX
Selected Region Sales =
CALCULATE(
    [Total Sales],
    ALLSELECTED(Customer[Region])
)
```

### Tooltips and Custom Tooltips

Create a tooltip page, set **Page information > Tooltip** to On, and add the page to a visual's tooltip configuration.

```DAX
Sales Share =
DIVIDE(
    [Total Sales],
    CALCULATE([Total Sales], ALL(Product[Category]))
)
```

Format `Sales Share` as a percentage and show it in the custom tooltip.

### Tables, Matrices, and Conditional Formatting

Use a table for a flat list and a matrix for nested row and column groups.

```DAX
Status Color =
SWITCH(
    TRUE(),
    [Total Sales] >= 100000, "#16803C",
    [Total Sales] >= 50000, "#D97706",
    "#B42318"
)
```

Apply conditional formatting to a value, background, font color, data bar, or icon rule. Keep the color meaning consistent across report pages.

## Power BI Service, Publishing, and Sharing

### Publish a Report

1. Sign in to Power BI Desktop.
2. Select **Publish**.
3. Choose a workspace.
4. Open the report in Power BI Service and confirm that visuals, filters, and relationships work.
5. Configure credentials and scheduled refresh under the semantic model settings.

### Workspaces and Dashboards

A workspace is a collaborative container for reports, semantic models, dashboards, and dataflows. A dashboard is a single-page collection of pinned tiles, while a report can contain multiple interactive pages.

Recommended workspace roles:

| Role | Typical responsibility |
| --- | --- |
| Admin | Manage workspace settings and access |
| Member | Publish and collaborate on content |
| Contributor | Create and update content |
| Viewer | Consume shared reports and dashboards |

### Dashboard and Theme Configuration

Use **View > Themes** in Desktop to apply a consistent visual language. A theme can also be stored as JSON:

```json
{
  "name": "Analytics Blue",
  "dataColors": ["#155EEF", "#12B76A", "#F79009", "#D92D20"],
  "background": "#FFFFFF",
  "foreground": "#101828",
  "tableAccent": "#155EEF"
}
```

In Power BI Service, pin useful report visuals to a dashboard and configure dashboard tiles for quick monitoring.

### Sharing Safely

Before sharing, verify workspace permissions, row-level security, sensitivity labels, and whether recipients need access to the underlying semantic model. Prefer sharing through managed workspaces or apps instead of sending unrestricted files.

## Power Query: Shaping and Combining Data

Power Query uses the M language. Transformations are applied as repeatable steps before data reaches the model.

### Power Query Structure and Data Types

A basic query uses a `let` expression followed by an `in` expression:

```powerquery
let
    Source = Excel.Workbook(File.Contents("C:\Data\sales.xlsx"), null, true),
    SalesSheet = Source{[Item="Sales", Kind="Sheet"]}[Data],
    PromotedHeaders = Table.PromoteHeaders(SalesSheet, [PromoteAllScalars=true]),
    TypedColumns = Table.TransformColumnTypes(
        PromotedHeaders,
        {{"OrderDate", type date}, {"Quantity", Int64.Type}, {"UnitPrice", type number}}
    )
in
    TypedColumns
```

Use clear names for queries and steps, and apply data types as early as practical.

### Parameters

Parameters make file paths, dates, and environments configurable:

```powerquery
let
    Source = Csv.Document(
        File.Contents(FilePathParameter),
        [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]
    )
in
    Source
```

### Merge and Append

Merge joins tables horizontally using matching columns. Append stacks tables vertically.

```powerquery
let
    Merged = Table.NestedJoin(
        Sales,
        {"ProductKey"},
        Products,
        {"ProductKey"},
        "ProductDetails",
        JoinKind.LeftOuter
    ),
    Expanded = Table.ExpandTableColumn(
        Merged,
        "ProductDetails",
        {"ProductName", "Category"},
        {"ProductName", "Category"}
    ),
    Combined = Table.Combine({Expanded, HistoricalSales})
in
    Combined
```

### Group By and Aggregation

```powerquery
let
    Grouped = Table.Group(
        Sales,
        {"Category"},
        {{"TotalSales", each List.Sum([SalesAmount]), type number},
         {"OrderCount", each Table.RowCount(_), Int64.Type}}
    )
in
    Grouped
```

### Duplicate and Reference Queries

Use **Duplicate** when you need an independent copy. Use **Reference** when a new query should inherit the result of another query and remain connected to its steps.

```powerquery
let
    Source = Sales,
    CleanCopy = Table.SelectRows(Source, each [SalesAmount] > 0)
in
    CleanCopy
```

### Fill, Replace, and Split Columns

```powerquery
let
    Filled = Table.FillDown(Sales, {"Region"}),
    Replaced = Table.ReplaceValue(
        Filled,
        "N/A",
        null,
        Replacer.ReplaceValue,
        {"CustomerName"}
    ),
    Split = Table.SplitColumn(
        Replaced,
        "CustomerName",
        Splitter.SplitTextByDelimiter(" ", QuoteStyle.Csv),
        {"FirstName", "LastName"}
    )
in
    Split
```

### Pivot, Unpivot, Custom, and Conditional Columns

```powerquery
let
    Unpivoted = Table.UnpivotOtherColumns(
        MonthlySales,
        {"ProductName"},
        "Month",
        "SalesAmount"
    ),
    WithCustomColumn = Table.AddColumn(
        Unpivoted,
        "SalesBand",
        each if [SalesAmount] >= 100000 then "High" else "Standard",
        type text
    )
in
    WithCustomColumn
```

To pivot data in the interface, select a column and choose **Transform > Pivot Column**. Use **Unpivot Columns** when month or category values are stored as separate columns.

### Sorting, Row Counts, Reverse Rows, and Headers

```powerquery
let
    RowCount = Table.RowCount(Sales),
    Reversed = Table.ReverseRows(Sales),
    Sorted = Table.Sort(Reversed, {{"OrderDate", Order.Descending}}),
    Headers = Table.PromoteHeaders(Sorted, [PromoteAllScalars=true])
in
    Headers
```

## Data Modeling and DAX

### Relationships, Cardinality, and Filter Direction

Create relationships in Model view. A typical model uses:

- One-to-many cardinality from dimension tables to fact tables.
- Single-direction filtering from dimensions to facts.
- A dedicated Date table related to the date column in the fact table.

```DAX
Date =
ADDCOLUMNS(
    CALENDAR(DATE(2025, 1, 1), DATE(2026, 12, 31)),
    "Year", YEAR([Date]),
    "Quarter", "Q" & FORMAT([Date], "Q"),
    "Month", FORMAT([Date], "MMM"),
    "MonthNumber", MONTH([Date])
)
```

Mark this table as a date table and sort `Date[Month]` by `Date[MonthNumber]`.

### Active and Inactive Relationships

Use an inactive relationship when a fact table contains multiple date roles, such as order date and ship date.

```DAX
Sales by Ship Date =
CALCULATE(
    [Total Sales],
    USERELATIONSHIP(Sales[ShipDate], 'Date'[Date])
)
```

### DAX Syntax and Context

DAX evaluates expressions in row context and filter context. `CALCULATE` changes filter context.

```DAX
Total Cost =
SUMX(Sales, Sales[Quantity] * Sales[UnitCost])

Total Profit =
[Total Sales] - [Total Cost]

Profit Margin =
DIVIDE([Total Profit], [Total Sales])
```

### Calculated Columns

A calculated column is evaluated row by row and stored in the model:

```DAX
Sales[Line Amount] =
Sales[Quantity] * Sales[UnitPrice] * (1 - Sales[Discount])
```

### Measures

Measures are evaluated when a visual queries them, so they respond to filters and slicers:

```DAX
Total Sales = SUM(Sales[Line Amount])

Sales This Year =
CALCULATE(
    [Total Sales],
    'Date'[Year] = MAX('Date'[Year])
)

Sales vs Previous Year =
[Total Sales] - [Sales Previous Year]
```

### Calculated Tables

```DAX
Top Products =
TOPN(
    10,
    SUMMARIZE(
        Product,
        Product[ProductKey],
        Product[ProductName],
        "Product Sales", [Total Sales]
    ),
    [Product Sales],
    DESC
)
```

### DAX Function Families

```DAX
-- Table functions
Active Products = FILTER(Product, Product[IsActive] = TRUE())

-- Information functions
Has Product = ISINSCOPE(Product[ProductName])

-- Logical functions
Performance Label = IF([Profit Margin] >= 0.2, "Healthy", "Review")

-- Text functions
Product Label = Product[Category] & " - " & Product[ProductName]

-- Iterator function
Weighted Discount =
AVERAGEX(Sales, Sales[Discount] * Sales[Quantity])
```

### Time Intelligence: YTD, QTD, and MTD

Time-intelligence functions require a continuous, marked Date table.

```DAX
Sales YTD =
TOTALYTD([Total Sales], 'Date'[Date])

Sales QTD =
TOTALQTD([Total Sales], 'Date'[Date])

Sales MTD =
TOTALMTD([Total Sales], 'Date'[Date])

Sales Previous Year =
CALCULATE(
    [Total Sales],
    SAMEPERIODLASTYEAR('Date'[Date])
)
```

### Cumulative Values

```DAX
Cumulative Sales =
CALCULATE(
    [Total Sales],
    FILTER(
        ALLSELECTED('Date'[Date]),
        'Date'[Date] <= MAX('Date'[Date])
    )
)
```

### Ranking and Rank Over Groups

```DAX
Product Rank =
RANKX(
    ALL(Product[ProductName]),
    [Total Sales],
    ,
    DESC,
    DENSE
)

Category Product Rank =
RANKX(
    ALLEXCEPT(Product, Product[Category]),
    [Total Sales],
    ,
    DESC,
    DENSE
)
```

## Suggested Study Flow

1. Learn the Power BI Desktop interface and the difference between reports, dashboards, and semantic models.
2. Load a small dataset and practice Power Query data types, renaming, filtering, splitting, and replacing values.
3. Build a star schema with dimension and fact tables and verify relationship direction and cardinality.
4. Create measures for totals, percentages, rankings, and time intelligence.
5. Design a report with charts, slicers, drill-through, bookmarks, tooltips, and conditional formatting.
6. Publish to a workspace, configure refresh, apply permissions, and share a controlled report or app.

## Learning Outcomes

By the end of this course, you should be able to:

- Explain the main Power BI components and a standard report workflow.
- Choose suitable visuals and format them for clear analysis.
- Build interactive pages with filters, slicers, drill paths, bookmarks, and tooltips.
- Shape and combine data with Power Query and reusable M steps.
- Design relationships with appropriate cardinality and filter direction.
- Write DAX calculated columns, measures, calculated tables, rankings, and time-intelligence calculations.
- Publish, configure, and share reports responsibly through Power BI Service.

## Source Material

- [`SYLLABUS.txt`](SYLLABUS.txt) - Original Power BI course outline.
- [`../README.md`](../README.md) - Repository overview.
