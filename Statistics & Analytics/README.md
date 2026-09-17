# Statistics & Analytics Roadmap

A practical learning guide for understanding data, measuring variation, exploring patterns, cleaning datasets, and communicating results with Python.

> **Course focus:** Move from statistical foundations to a complete analytics workflow using NumPy, Pandas, Matplotlib, and Seaborn.

## At A Glance

| Stage | What you will learn |
| --- | --- |
| Statistics | Samples, averages, quartiles, variance, standard deviation, and outliers |
| Distributions | Normal, uniform, exponential, skewed, and random data |
| NumPy | Arrays, indexing, slicing, and vector or matrix operations |
| Pandas | Series, DataFrames, loading data, EDA, cleaning, dates, and encoding |
| Visualization | Plots that reveal relationships, distributions, categories, and outliers |

## Contents

- [Setup](#setup)
- [Statistical Foundations](#statistical-foundations)
- [Data Distributions](#data-distributions)
- [NumPy](#numpy)
- [Pandas](#pandas)
- [Loading Datasets](#loading-datasets)
- [Accessing Data](#accessing-data)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Data Manipulation and Cleaning](#data-manipulation-and-cleaning)
- [Categorical Encoding](#categorical-encoding)
- [Date and Time](#date-and-time)
- [Visualization](#visualization)
- [Suggested Study Flow](#suggested-study-flow)

## Setup

Install the packages used in this guide:

```bash
python -m pip install numpy pandas matplotlib seaborn scikit-learn openpyxl lxml
```

Import the standard analytics stack:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

## Statistical Foundations

### Population and Sample

A **population** is the complete group being studied. A **sample** is a smaller group selected from that population.

```python
population = np.array([10, 12, 15, 18, 20, 22, 25, 28])
sample = population[[0, 2, 4, 6]]

print("Population mean:", population.mean())
print("Sample mean:", sample.mean())
```

### Measures of Central Tendency

```python
from statistics import harmonic_mean, geometric_mean, mean, median, mode

values = [10, 12, 12, 15, 18, 20]

print("Arithmetic mean:", mean(values))
print("Harmonic mean:", harmonic_mean(values))
print("Geometric mean:", geometric_mean(values))
print("Median:", median(values))
print("Mode:", mode(values))
```

### Quartiles

Quartiles divide ordered data into four parts. The interquartile range (IQR) is $Q_3 - Q_1$.

```python
values = np.array([10, 12, 12, 15, 18, 20, 22, 25, 60])
q1, q2, q3 = np.percentile(values, [25, 50, 75])
iqr = q3 - q1

print({"Q1": q1, "Q2": q2, "Q3": q3, "IQR": iqr})
```

### Variance and Standard Deviation

Variance measures average squared distance from the mean. Standard deviation is the square root of variance.

```python
values = np.array([10, 12, 15, 18, 20])

print("Population variance:", np.var(values))
print("Population standard deviation:", np.std(values))
print("Sample variance:", np.var(values, ddof=1))
print("Sample standard deviation:", np.std(values, ddof=1))
```

### Detecting Outliers

The IQR rule marks values below $Q_1 - 1.5 \times IQR$ or above $Q_3 + 1.5 \times IQR$ as potential outliers.

```python
values = pd.Series([10, 12, 12, 15, 18, 20, 22, 25, 60])
q1, q3 = values.quantile([0.25, 0.75])
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outliers = values[(values < lower) | (values > upper)]
print("Outliers:", outliers.tolist())
```

## Data Distributions

A distribution describes how values are spread across a dataset.

```python
rng = np.random.default_rng(42)

normal_data = rng.normal(loc=50, scale=10, size=1000)
uniform_data = rng.uniform(low=0, high=1, size=1000)
exponential_data = rng.exponential(scale=2, size=1000)
right_skewed_data = rng.lognormal(mean=0, sigma=0.8, size=1000)
random_data = rng.random(1000)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
axes[0].hist(normal_data, bins=30, color="steelblue")
axes[0].set_title("Normal")
axes[1].hist(uniform_data, bins=30, color="seagreen")
axes[1].set_title("Uniform")
axes[2].hist(exponential_data, bins=30, color="darkorange")
axes[2].set_title("Exponential")
plt.tight_layout()
plt.show()
```

A left-skewed distribution can be created by reflecting right-skewed data:

```python
left_skewed_data = right_skewed_data.max() - right_skewed_data
```

### Central Limit Theorem

The Central Limit Theorem says that the means of sufficiently large random samples tend toward a normal distribution, even when the original data is not normal.

```python
rng = np.random.default_rng(42)
population = rng.exponential(scale=2, size=100_000)
sample_means = [
    rng.choice(population, size=30, replace=False).mean()
    for _ in range(1000)
]

plt.hist(sample_means, bins=30, color="mediumpurple")
plt.title("Distribution of Sample Means")
plt.xlabel("Sample mean")
plt.ylabel("Frequency")
plt.show()
```

## NumPy

NumPy arrays are more efficient than regular Python lists for numerical operations and support vectorized calculations.

### Lists, Arrays, and Vector Operations

```python
numbers = [1, 2, 3, 4]
array = np.array(numbers)

print(array * 2)       # Vectorized multiplication
print(array + 10)      # Add to every element
print(array.mean())
```

### Matrix Operations

```python
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

print("Element-wise product:\n", matrix_a * matrix_b)
print("Matrix product:\n", matrix_a @ matrix_b)
print("Transpose:\n", matrix_a.T)
```

### Array Indexing and Slicing

```python
array = np.arange(1, 13).reshape(3, 4)

print(array[0, 1])     # First row, second column
print(array[:, 1])     # Every row, second column
print(array[1:, 2:])   # Rows after the first, columns after the second
```

## Pandas

Pandas provides labeled `Series` objects and two-dimensional `DataFrame` objects for working with structured data.

```python
scores = pd.Series([88, 76, 92], index=["Aman", "Anil", "Neha"])

students = pd.DataFrame({
    "name": ["Aman", "Anil", "Neha", "Riya", "Kabir"],
    "city": ["Delhi", "Noida", "Delhi", "Gurgaon", "Noida"],
    "course": ["Python", "SQL", "Python", "SQL", "Python"],
    "score": [88, 76, 92, 81, 69],
    "joined_on": ["2026-01-10", "2026-01-12", "2026-02-05", "2026-02-08", "2026-02-15"],
})

print(scores)
print(students)
```

## Loading Datasets

### CSV and Excel

```python
csv_data = pd.read_csv("students.csv")
excel_data = pd.read_excel("students.xlsx", sheet_name="Sheet1")
```

### HTML Tables

```python
html_tables = pd.read_html("https://example.com/table-page")
first_table = html_tables[0]
```

### Database Tables

```python
from sqlalchemy import create_engine

engine = create_engine("sqlite:///training.db")
database_data = pd.read_sql("SELECT * FROM students", engine)
```

## Accessing Data

`at` and `iat` access one value. `loc` and `iloc` select labeled or positional rows and columns.

```python
print(students.head(3))
print(students.tail(2))
print(students.at[0, "name"])
print(students.iat[0, 0])
print(students.loc[students["city"] == "Delhi", ["name", "score"]])
print(students.iloc[:3, :2])
```

## Exploratory Data Analysis

### `describe()`

```python
print(students.describe(numeric_only=True))
print(students.describe(include="object"))
```

### `groupby()` and `crosstab()`

```python
print(students.groupby("course")["score"].agg(["count", "mean", "max"]))
print(pd.crosstab(students["city"], students["course"]))
```

### Boolean Slicing and `query()`

```python
high_scorers = students[students["score"] >= 80]
python_students = students.query("course == 'Python' and score >= 80")

print(high_scorers)
print(python_students)
```

## Data Manipulation and Cleaning

### `map()` and `apply()`

```python
students["result"] = students["score"].map(
    lambda score: "Pass" if score >= 50 else "Needs improvement"
)
students["score_percent"] = students["score"].apply(lambda score: f"{score}%")
```

### Combining DataFrames

```python
contact_data = pd.DataFrame({
    "name": ["Aman", "Anil", "Neha", "Riya", "Kabir"],
    "email": ["aman@example.com", "anil@example.com", "neha@example.com", "riya@example.com", "kabir@example.com"],
})

combined = pd.merge(students, contact_data, on="name", how="left")
extra_students = students.iloc[:2]
all_students = pd.concat([students, extra_students], ignore_index=True)
```

### Adding, Removing, and Sorting

```python
students["passed"] = students["score"] >= 50
students = students.drop(columns=["score_percent"])
students = students.sort_values("score", ascending=False)
```

### Missing Values

```python
students.loc[1, "city"] = np.nan
students["city"] = students["city"].fillna("Unknown")
students = students.dropna(subset=["name", "score"])
```

### Duplicates and Data Errors

```python
students = students.drop_duplicates()
students["score"] = pd.to_numeric(students["score"], errors="coerce")
students["course"] = students["course"].str.strip().str.title()
students = students[students["score"].between(0, 100)]
```

## Categorical Encoding

Encoding converts categorical values into numerical values for analysis or machine learning.

### Label Encoding

```python
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
students["course_label"] = encoder.fit_transform(students["course"])
print(students[["course", "course_label"]])
```

### One-Hot Encoding

```python
encoded_students = pd.get_dummies(
    students,
    columns=["city", "course"],
    dtype=int,
)
print(encoded_students.head())
```

## Date and Time

```python
students["joined_on"] = pd.to_datetime(students["joined_on"])
students["join_year"] = students["joined_on"].dt.year
students["join_month"] = students["joined_on"].dt.month_name()
students["days_enrolled"] = (pd.Timestamp.today().normalize() - students["joined_on"]).dt.days

recent_students = students[students["joined_on"] >= "2026-02-01"]
print(recent_students)
```

## Visualization

Use Matplotlib for flexible plotting and Seaborn for attractive statistical visualizations.

### Scatter Plot and Line Plot

```python
sns.scatterplot(data=students, x="score", y="days_enrolled", hue="course")
plt.title("Score and Enrollment Duration")
plt.show()

trend = students.groupby("joined_on", as_index=False)["score"].mean()
sns.lineplot(data=trend, x="joined_on", y="score", marker="o")
plt.xticks(rotation=45)
plt.title("Average Score Over Time")
plt.tight_layout()
plt.show()
```

### Bar Plot and Histogram

```python
sns.barplot(data=students, x="course", y="score", errorbar=None)
plt.title("Average Score by Course")
plt.show()

sns.histplot(data=students, x="score", bins=5, kde=True)
plt.title("Score Distribution")
plt.show()
```

### Pie Chart

```python
course_counts = students["course"].value_counts()
course_counts.plot.pie(autopct="%1.1f%%", ylabel="", title="Students by Course")
plt.show()
```

### Joint Plot and Pair Plot

```python
sns.jointplot(data=students, x="score", y="days_enrolled", kind="scatter")
plt.show()

sns.pairplot(students, vars=["score", "days_enrolled"], hue="course")
plt.show()
```

### Heatmap

```python
correlations = students[["score", "days_enrolled"]].corr()
sns.heatmap(correlations, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation Heatmap")
plt.show()
```

### Boxplot for Outlier Detection

```python
sns.boxplot(data=students, x="course", y="score")
plt.title("Score Outliers by Course")
plt.show()
```

## Suggested Study Flow

1. Learn samples, populations, averages, quartiles, variation, and outliers.
2. Generate and visualize common distributions, then understand the Central Limit Theorem.
3. Practice NumPy arrays before moving to labeled Pandas data.
4. Load datasets and explore them with selection, summaries, grouping, and cross-tabulation.
5. Clean missing, duplicated, invalid, and incorrectly typed data.
6. Encode categorical columns and extract useful date features.
7. Tell the story of the dataset with appropriate plots and a short written conclusion.

## Learning Outcomes

By the end of this course, you should be able to:

- Summarize data with meaningful statistical measures.
- Recognize common distributions and explain sampling behavior.
- Perform numerical operations with NumPy arrays.
- Load, inspect, transform, and clean real-world datasets with Pandas.
- Encode categorical data and work with date and time columns.
- Select visualizations that communicate distributions, relationships, and outliers.
- Complete a reproducible exploratory data analysis workflow.

## Source Material

- [`SYLLABUS.txt`](SYLLABUS.txt) - Original Statistics & Analytics course outline.
- [`../README.md`](../README.md) - Repository overview.
