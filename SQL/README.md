# SQL & MongoDB Learning Roadmap

A practical guide to relational databases, MySQL, MongoDB, and Python database connectivity.

> **Course focus:** Learn how to design, query, modify, and connect to both SQL and NoSQL databases using realistic student and course data.

## At A Glance

| Track | Topics |
| --- | --- |
| MySQL | RDBMS concepts, SQL syntax, constraints, operators, clauses, functions, procedures, joins, views, and CSV files |
| MongoDB | NoSQL concepts, documents, CRUD, operators, aggregation, methods, indexes, and relationships |
| Python Connectivity | MySQL connectors, cursors, query execution, result fetching, dates, and PyMongo |

## Contents

- [MySQL and RDBMS](#mysql-and-rdbms)
- [SQL Basics](#sql-basics)
- [Constraints](#constraints)
- [Operators and Clauses](#operators-and-clauses)
- [Stored Procedures and Functions](#stored-procedures-and-functions)
- [SQL Functions](#sql-functions)
- [Joins](#joins)
- [Views](#views)
- [CSV Files](#csv-files)
- [Python and MySQL](#python-and-mysql)
- [MongoDB](#mongodb)
- [MongoDB CRUD](#mongodb-crud)
- [MongoDB Operators and Aggregation](#mongodb-operators-and-aggregation)
- [MongoDB Methods, Indexes, and Relationships](#mongodb-methods-indexes-and-relationships)
- [Python and MongoDB](#python-and-mongodb)

## MySQL and RDBMS

A relational database stores data in related tables. SQL is the language used to define, query, and manipulate that data. MySQL is a relational database management system that executes SQL statements.

### Installation and Connection

Install MySQL Server and MySQL Workbench from the official MySQL website. Then connect from a MySQL client:

```sql
mysql -u root -p
```

Create a practice database:

```sql
CREATE DATABASE IF NOT EXISTS training_db;
USE training_db;
```

## SQL Basics

### DDL: Create, Alter, and Drop

```sql
CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    duration_months INT
);

ALTER TABLE courses ADD COLUMN level_name VARCHAR(30);

-- Remove the table only when its data is no longer needed.
-- DROP TABLE courses;
```

### DML: Insert, Update, and Delete

```sql
INSERT INTO courses (course_name, duration_months, level_name)
VALUES
    ('Python', 4, 'Beginner'),
    ('SQL', 3, 'Intermediate');

UPDATE courses
SET duration_months = 5
WHERE course_name = 'Python';

DELETE FROM courses
WHERE course_name = 'SQL';
```

### DQL: Select, Aliases, and Comments

```sql
-- Select useful columns and rename one column in the result.
SELECT course_name AS subject, duration_months AS months
FROM courses;
```

### Transactions, Savepoints, and Rollback

```sql
START TRANSACTION;

INSERT INTO courses (course_name, duration_months, level_name)
VALUES ('Power BI', 2, 'Beginner');

SAVEPOINT after_power_bi;

UPDATE courses
SET duration_months = 3
WHERE course_name = 'Power BI';

ROLLBACK TO after_power_bi;
COMMIT;
```

## Constraints

Constraints protect the quality and relationships of database records.

```sql
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(150) NOT NULL UNIQUE,
    full_name VARCHAR(100) NOT NULL,
    age INT CHECK (age >= 16),
    city VARCHAR(50) DEFAULT 'Delhi',
    course_id INT,
    CONSTRAINT fk_student_course
        FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
```

This example demonstrates `NOT NULL`, `UNIQUE`, `PRIMARY KEY`, `CHECK`, `DEFAULT`, and `FOREIGN KEY` constraints.

## Operators and Clauses

### Operators

```sql
SELECT course_name, duration_months
FROM courses
WHERE duration_months >= 3                 -- comparison operator
  AND course_name LIKE '%thon%'             -- pattern operator
  AND duration_months BETWEEN 3 AND 6       -- range operator
  AND level_name IN ('Beginner', 'Advanced'); -- membership operator

SELECT course_name, duration_months * 30 AS approximate_days
FROM courses;
```

### `WHERE`, `ORDER BY`, `LIMIT`, `GROUP BY`, and `HAVING`

```sql
SELECT city, COUNT(*) AS student_count, AVG(age) AS average_age
FROM students
WHERE age >= 18
GROUP BY city
HAVING COUNT(*) >= 1
ORDER BY student_count DESC
LIMIT 5;
```

> MySQL uses `LIMIT` to restrict rows. Some other database systems use `TOP` or `FETCH FIRST`.

## Stored Procedures and Functions

Stored procedures package reusable SQL statements. User-defined functions return a value and can be used inside expressions.

### Stored Procedure

```sql
DELIMITER //

CREATE PROCEDURE GetStudentsByCity(IN requested_city VARCHAR(50))
BEGIN
    SELECT student_id, full_name, email
    FROM students
    WHERE city = requested_city
    ORDER BY full_name;
END //

DELIMITER ;

CALL GetStudentsByCity('Delhi');
```

### User-Defined Function

```sql
DELIMITER //

CREATE FUNCTION GetAgeGroup(student_age INT)
RETURNS VARCHAR(20)
DETERMINISTIC
BEGIN
    IF student_age < 18 THEN
        RETURN 'Under 18';
    ELSE
        RETURN 'Adult';
    END IF;
END //

DELIMITER ;

SELECT full_name, GetAgeGroup(age) AS age_group
FROM students;
```

## SQL Functions

### String Functions

```sql
SELECT
    UPPER(full_name) AS uppercase_name,
    LOWER(email) AS lowercase_email,
    LENGTH(full_name) AS name_length,
    CONCAT(full_name, ' - ', city) AS student_label
FROM students;
```

### Aggregate Functions

```sql
SELECT
    COUNT(*) AS total_students,
    AVG(age) AS average_age,
    MIN(age) AS youngest,
    MAX(age) AS oldest
FROM students;
```

### Date and Time Functions

```sql
SELECT
    CURRENT_DATE() AS today,
    CURRENT_TIMESTAMP() AS current_time,
    YEAR(CURRENT_DATE()) AS current_year;
```

## Joins

Joins combine rows from related tables through matching keys.

```sql
-- INNER JOIN: only matching courses and students.
SELECT s.full_name, c.course_name
FROM students AS s
INNER JOIN courses AS c ON s.course_id = c.course_id;

-- LEFT JOIN: all courses, including courses without students.
SELECT c.course_name, s.full_name
FROM courses AS c
LEFT JOIN students AS s ON c.course_id = s.course_id;

-- RIGHT JOIN: all courses from the right-side table.
SELECT s.full_name, c.course_name
FROM students AS s
RIGHT JOIN courses AS c ON s.course_id = c.course_id;
```

MySQL does not provide a native `FULL JOIN`. Combine a left and right join with `UNION`:

```sql
SELECT s.full_name, c.course_name
FROM students AS s
LEFT JOIN courses AS c ON s.course_id = c.course_id

UNION

SELECT s.full_name, c.course_name
FROM students AS s
RIGHT JOIN courses AS c ON s.course_id = c.course_id;
```

## Views

A view is a stored query that behaves like a virtual table.

```sql
CREATE VIEW student_course_report AS
SELECT s.student_id, s.full_name, s.city, c.course_name
FROM students AS s
LEFT JOIN courses AS c ON s.course_id = c.course_id;

SELECT * FROM student_course_report;

-- Simple views may be updated when MySQL can map the change safely.
UPDATE student_course_report
SET city = 'Noida'
WHERE student_id = 1;
```

## CSV Files

Export query results from MySQL with `INTO OUTFILE` when the server has permission to write to the selected directory:

```sql
SELECT student_id, full_name, email, city
FROM students
INTO OUTFILE '/tmp/students.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';
```

Import a CSV file into a matching table:

```sql
LOAD DATA INFILE '/tmp/students.csv'
INTO TABLE students
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(student_id, full_name, email, city);
```

## Python and MySQL

Install a MySQL connector:

```bash
python -m pip install mysql-connector-python
```

The connector creates a connection, a cursor, executes SQL, fetches records, and closes resources.

```python
from datetime import date
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="training_db",
)

cursor = connection.cursor(dictionary=True)
cursor.execute(
    "SELECT full_name, city FROM students WHERE course_id = %s",
    (1,),
)

for student in cursor.fetchall():
    print(student["full_name"], student["city"])

cursor.execute(
    "INSERT INTO students (email, full_name, age, city) "
    "VALUES (%s, %s, %s, %s)",
    ("new@example.com", "New Student", 21, "Delhi"),
)
connection.commit()

print(date.today())
cursor.close()
connection.close()
```

Use parameterized queries instead of string concatenation so user input is not inserted directly into SQL statements.

# MongoDB

MongoDB is a document-oriented NoSQL database. It stores flexible, JSON-like documents inside collections rather than rows inside fixed tables.

| SQL | MongoDB |
| --- | --- |
| Database | Database |
| Table | Collection |
| Row | Document |
| Column | Field |
| Primary key | `_id` |

MongoDB can be used through the MongoDB Shell, MongoDB Compass, or a programming driver.

## MongoDB Setup and Data Model

After installing MongoDB, open the shell with:

```bash
mongosh
```

Select a database and create a collection by inserting a document:

```javascript
use training_db

db.students.insertOne({
  name: "Aman",
  age: 22,
  city: "Delhi",
  courses: ["Python", "SQL"]
})
```

## MongoDB CRUD

### Insert Documents

```javascript
db.students.insertMany([
  { name: "Anil", age: 20, city: "Noida", score: 84 },
  { name: "Ankit", age: 21, city: "Delhi", score: 91 }
])
```

### Query Documents

```javascript
// Find all students from Delhi.
db.students.find({ city: "Delhi" })

// Return only selected fields.
db.students.find(
  { age: { $gte: 20 } },
  { _id: 0, name: 1, score: 1 }
)
```

### Update Documents

```javascript
db.students.updateOne(
  { name: "Aman" },
  { $set: { score: 88 }, $addToSet: { courses: "MongoDB" } }
)
```

### Delete Documents

```javascript
db.students.deleteOne({ name: "Ankit" })
```

## MongoDB Operators and Aggregation

### Query and Projection Operators

```javascript
db.students.find({
  age: { $gte: 20, $lte: 25 },
  city: { $in: ["Delhi", "Noida"] }
}, {
  _id: 0,
  name: 1,
  age: 1
})
```

### Update Operators

```javascript
db.students.updateMany(
  { score: { $exists: true } },
  { $inc: { score: 2 }, $set: { updated: true } }
)
```

### Aggregation Pipeline Operators

```javascript
db.students.aggregate([
  { $match: { score: { $exists: true } } },
  { $group: { _id: "$city", average_score: { $avg: "$score" } } },
  { $sort: { average_score: -1 } }
])
```

## MongoDB Methods, Indexes, and Relationships

### `limit`, `sort`, and Bulk Methods

```javascript
db.students.find().sort({ score: -1 }).limit(3)

db.students.bulkWrite([
  {
    updateOne: {
      filter: { name: "Aman" },
      update: { $set: { active: true } }
    }
  },
  {
    insertOne: {
      document: { name: "Neha", age: 23, city: "Gurgaon" }
    }
  }
])
```

### Indexes

Indexes speed up searches on frequently queried fields.

```javascript
db.students.createIndex({ email: 1 }, { unique: true })
db.students.getIndexes()
db.students.dropIndex({ email: 1 })
```

### Relationships Between Documents

Embed small, closely related data:

```javascript
db.courses.insertOne({
  name: "Python",
  instructor: { name: "Priya", email: "priya@example.com" }
})
```

Reference data that is large or shared by multiple documents:

```javascript
db.students.insertOne({
  name: "Aman",
  course_ids: [ObjectId("65f000000000000000000001")]
})
```

## Python and MongoDB

Install the PyMongo driver:

```bash
python -m pip install pymongo
```

Connect to MongoDB and perform CRUD operations and a range query:

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
database = client["training_db"]
students = database["students"]

students.insert_one({
    "name": "Riya",
    "age": 24,
    "city": "Delhi",
    "score": 89,
})

for student in students.find({"age": {"$gte": 20, "$lte": 25}}):
    print(student["name"], student.get("score"))

students.update_one(
    {"name": "Riya"},
    {"$set": {"active": True}},
)
students.delete_one({"name": "Riya"})

client.close()
```

## Suggested Study Flow

1. Learn tables, documents, keys, and the difference between relational and NoSQL databases.
2. Build the MySQL schema and practice DDL, DML, constraints, operators, and clauses.
3. Query related data with functions, joins, views, procedures, and transactions.
4. Export and import CSV data, then connect to MySQL from Python.
5. Repeat the CRUD workflow in MongoDB with operators, aggregation, indexes, and relationships.
6. Build a Python application that uses either MySQL Connector or PyMongo.

## Learning Outcomes

By the end of this course, you should be able to:

- Design basic relational tables with keys and constraints.
- Write reliable SQL queries for filtering, grouping, sorting, and joining data.
- Use transactions, procedures, functions, views, and CSV workflows.
- Explain the difference between SQL and NoSQL data models.
- Perform MongoDB CRUD operations and write aggregation pipelines.
- Choose between embedded and referenced MongoDB relationships.
- Connect Python applications to MySQL and MongoDB securely.

## Source Material

- [`SYLLABUS.txt`](SYLLABUS.txt) - Original SQL and MongoDB course outline.
- [`../README.md`](../README.md) - Repository overview.
