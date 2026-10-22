# SQL

## SQL stands for Structured Query Language

Definition of Database: A collection of information that can be organized so it can be accessed, managed, and updated.

In a database, information is stored in tabular format. Tables are divided into rows and columns. Rows are horizontal and columns are vertical.

| id  | name  | age | salary |
| --- | ----- | --- | ------ |
| 123 | anil  | 20  | 20K    |
| 123 | amit  | 22  | 21K    |
| 123 | ankit | 25  | 34K    |
| 123 | anita | 30  | 56K    |

Each row is also called a record or tuple. Each column is also called a field, attribute, or feature.

- Database -> Schema
- Table -> Entity

### Fields -> Records -> Tables -> Database

- A collection of fields is called a record.
- A collection of records is called a table.
- A collection of tables is called a database.

### Table

A table is the structure inside a database that contains data, organized in columns.

### Columns

The name of each column in a table is used to interpret its meaning and is called an attribute.

### Row

Each row in a table represents a record and is called a tuple.

### RDBMS

RDBMS avoids the navigation model used in old DBMS and introduces the relational model. The relational model defines relationships between tables using primary keys, foreign keys, and indexes. This makes data storage and retrieval faster than the old navigational model. RDBMS is useful for efficiently managing large amounts of data and is used in large business applications.

1. Oracle
2. Microsoft SQL Server
3. MySQL
4. SQLite3
5. MariaDB
6. PostgreSQL
7. MS Access

### DBMS

DBMS allows access to the data in a database.

1. FoxPro
2. LibreOffice
3. dBase

### SQL generally operates on relational databases

### Features of SQL

- It is a non-procedural language.
- It is an English-like language.
- It can process a single record as well as a set of records at a time.
- All SQL statements define what is to be done rather than how it is to be done.
- SQL has facilities for defining database views, security, transactions, etc.

| DBMS                                        | RDBMS                                     |
| ------------------------------------------- | ----------------------------------------- |
| Data stored in files                        | Data stored in tabular form               |
| Does not support client-server architecture | Supports client-server architecture       |
| NF not possible                             | NF present                                |
| Allows one user to access at a time         | Allows multiple users                     |
| Hierarchical arrangement of data            | Data stored in rows and columns           |
| Low software and hardware requirements      | Higher software and hardware requirements |
| ACID not supported                          | Supports ACID                             |
| Data redundancy                             | Removes data redundancy                   |

### ACID

ACID stands for Atomicity, Consistency, Isolation, and Durability.

1. Atomicity means a transaction is all-or-nothing either all its operations succeed, or none are applied. If any part fails, the entire transaction is rolled back to keep the database consistent.

- Commit: If the transaction is successful, the changes are permanently applied.
- Abort/Rollback: If the transaction fails, any changes made during the transaction are discarded.

2. Consistency in transactions means that the database must remain in a valid state before and after a transaction.

- A valid state follows all defined rules, constraints, and relationships (like primary keys, foreign keys, etc.).
- If a transaction violates any of these rules, it is rolled back to prevent corrupt or invalid data.
- If a transaction deducts money from one account but doesn't add it to another (in a transfer), it violates consistency.

3. Isolation ensures that transactions run independently without affecting each other. Changes made by one transaction are not visible to others until they are committed.

It ensures that the result of concurrent transactions is the same as if they were run one after another, preventing issues like:

- _Dirty reads:_ reading uncommitted data
- _Non-repeatable reads:_ data changes between two reads
- _Phantom reads:_ new rows appear during a transaction

4. Durability ensures that once a transaction is committed, its changes are permanently saved, even if the system fails. The data is stored in non-volatile memory, so the database can recover to its last committed state without losing data.

## Basic SQL Commands

### SQL commands can be classified into 5 categories

1. DDL - CREATE, ALTER, DROP, TRUNCATE, RENAME
2. DML - INSERT, UPDATE, DELETE, MERGE (not supported in MySQL, but present in Oracle and SQL Server)
3. DCL - LOCK, GRANT, REVOKE
4. TCL - ROLLBACK, COMMIT, SAVEPOINT, START TRANSACTION
5. DQL - SELECT
6. Administrative commands - SHOW, EXPLAIN (MySQL only), DESC, USE, etc.

## Data Types

1. Numeric datatype
2. Date and time
3. String/characters
4. Boolean (True/False)
5. Binary
6. Special

| Data Type | Description                                        | Range                                                   |
| --------- | -------------------------------------------------- | ------------------------------------------------------- |
| BIGINT    | Large integer numbers (8 bytes)                    | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 |
| INT       | Standard integer values (4 bytes)                  | -2,147,483,648 to 2,147,483,647                         |
| SMALLINT  | Small integers                                     | -32,768 to 32,767                                       |
| MEDIUMINT | Medium-sized integers                              | -8,388,608 to 8,388,607                                 |
| TINYINT   | Very small integers                                | 0 to 255 or -128 to 127                                 |
| DECIMAL   | Exact fixed-point numbers (e.g., financial values) | -10^38 + 1 to 10^38 - 1                                 |
| NUMERIC   | Similar to DECIMAL, used for precision data        | -10^38 + 1 to 10^38 - 1                                 |

### Date and time

1. Date
2. Time
3. Datetime
4. Timestamp
5. Year
6. Day
7. Month

### String/characters

1. CHAR - Fixed-length data type
2. VARCHAR - Variable-length data type

- It stores only numbers, alphabets, or a combination of both.

```sql
CREATE TABLE emp (
  id INT,
  name CHAR(30),
  age INT,
  profile VARCHAR(30),
  salary FLOAT
);
```

## Operators in MySQL

In MySQL, operators are of different types.

| Type             | Example             |
| ---------------- | ------------------- |
| Arithmetic       | +, -, /, %, \*      |
| Comparison       | =, <=, >=, !=, <, > |
| Logical          | AND, OR, NOT        |
| Pattern matching | LIKE, NOT LIKE      |

### CHAR Important

In CHAR, we store data that has a fixed size in a table. Example: Gender, RTO, True/False.

```sql
CREATE TABLE emp (
  id INT,
  name VARCHAR(30),
  age INT,
  profile VARCHAR(30),
  salary FLOAT
);
```

`;` -> Delimiter

### DDL

DDL includes CREATE, ALTER, DROP, TRUNCATE, RENAME.

```sql
CREATE DATABASE IF NOT EXISTS training_db;
USE training_db;
```

### Commands

```sql
USE db_name;

-- How to find the current selected database
SELECT DATABASE();

-- How to create a new table in the selected database
CREATE TABLE table_name (
  empId INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  dept TEXT NOT NULL,
  age INTEGER,
  salary FLOAT,
  city VARCHAR(20)
);

-- How to see the structure of a table
EXPLAIN db_name;
DESC db_name;

-- How to see all tables in a database
SHOW TABLES;

-- How to insert records into a table
-- Single record
INSERT INTO EMPLOYEE VALUES (0001, 'Clark', 'Sales', 20, 4000, 'Delhi');
INSERT INTO EMPLOYEE VALUES (0002, 'Dave', 'Accounting', 20, 4000, 'Delhi');
INSERT INTO EMPLOYEE VALUES (0003, 'Ava', 'Sales', 20, 4000, 'Delhi');

-- Multiple records
INSERT INTO EMPLOYEE VALUES
  (0001, 'Clark', 'Sales', 20, 4000, 'Delhi'),
  (0002, 'Dave', 'Accounting', 20, 4000, 'Delhi'),
  (0003, 'Ava', 'Sales', 20, 4000, 'Delhi');

-- How to display all records of the EMPLOYEE table
SELECT * FROM EMPLOYEE;

-- How to view a particular column
SELECT name FROM EMPLOYEE;

-- How to insert values only in specific columns
INSERT INTO EMPLOYEE (empID, name, age) VALUES (200, 'amit', 58);

-- How to update records
UPDATE EMPLOYEE SET name = 'amit' WHERE empID = 0001;

-- How to delete records from the employee table
DELETE FROM EMPLOYEE WHERE empID = 0001;
DELETE FROM EMPLOYEE WHERE city = 'dehi';
DELETE FROM EMPLOYEE;
```

## 13/10/2026

## 14/10/2026

### Difference between TRUNCATE and DELETE

1. DELETE removes rows from a table, while TRUNCATE removes all rows faster.
2. DELETE can be rolled back, but TRUNCATE cannot be rolled back in most cases.
3. Rollback works only with DELETE, not with TRUNCATE.

### Difference between DELETE and DROP

1. DROP deletes the table and its structure, while DELETE only removes data from the table.

### Difference between TRUNCATE and DROP

1. TRUNCATE removes table data but keeps the table structure, while DROP removes both the table and structure.

### How to drop a database

```sql
DROP DATABASE database_name;
```

```sql
TRUNCATE TABLE emp;
DESC emp;
DROP TABLE emp;
SELECT * FROM emp;
```

## Operator in MySQL

In MySQL, operators are of different types.

1. Retrieving records using arithmetic operators:
   - +, -, /, %, \*
2. Retrieving records using comparison operators:
   - =, <=, >=, !=, <, >
3. Retrieving records using logical operators:
   - AND, OR, NOT
4. Retrieving records using LIKE and NOT LIKE operators:
   - LIKE, NOT LIKE (used for pattern matching)
   - Wildcard: `%` means zero or more characters
   - Wildcard: `_` means a single character
5. Retrieving records using in 7 not in- it is used for list matching and it’s work with sting and numbers
6. Using between & not between - it is used for range matching and it work with number.
7. Using null & is not null operator- > select \*
8. Retrieving records using order by clause :- it is used for sort the records in ascending or descending order.
9. MySQL Compound Operators (+=,-=,\*=,/=)
10. LIMIT

| Operator | Description              |
| -------- | ------------------------ |
| +=       | Add equals               |
| -=       | Subtract equals          |
| \*=      | Multiply equals          |
| /=       | Divide equals            |
| %=       | Modulo equals            |
| &=       | Bitwise AND equals       |
| ^-=      | Bitwise exclusive equals |
| \*=      | Bitwise OR equals        |

```sql
-- How to increment salary by 3000
UPDATE emp SET salary = salary + 3000;

-- How to decrement salary by 3000
UPDATE emp SET salary = salary - 3000;
SELECT *, price * qty AS total_sales;

-- How to multiply salary by 3
UPDATE emp SET salary = salary * 3;

-- How to divide salary by 2
UPDATE emp SET salary = salary / 2;

-- Comparison operators work with strings and numbers
SELECT * FROM emp WHERE name = 'raj';
SELECT * FROM emp WHERE salary != 40000;

SELECT * FROM emp WHERE name = 'raj' AND age = 30;
SELECT * FROM emp WHERE age BETWEEN 30 AND 40;

```

# Practices

```sql
-- Arthimatical Operator
CREATE TABLE number(num1 int, num2 int);
INSERT INTO number VALUES(101,110),(20,20);
SELECT num1,num2,num1+num2 AS 'SUM' from number;
SELECT num1,num2,num1-num2 AS 'SUB' from number;
SELECT num1,num2,num1*num2 AS 'MULTI' from number;
SELECT num1,num2,num1/num2 AS 'DIV' from number;
SELECT num1,num2,num1%num2 AS 'MODE' from number;
SELECT num1,num2,power(num1,2) AS 'Exponet' from number;



-- CREATE A NEW TABLE
CREATE TABLE EMP(ID INT, NAME VARCHAR(20), AGE INT, SALARY FLOAT, CITY VARCHAR(20));

-- SINGLE RECORDS INSERT
-- INSERT INTO EMP VALUES(101, ANIL, 20, 23000, NOIDA)
-- INSERT INTO EMP VALUES(102, AMIT, 26, 23000, MAU)
-- INSERT INTO EMP VALUES(103, ANKIT, 30, 23000, DELHI)
-- INSERT INTO EMP VALUES(104, ANITA, 25, 23000, NOIDA)
-- INSERT INTO EMP VALUES(105, ARPIT, 22, 23000, VARANSI)
-- INSERT INTO EMP VALUES(106, ABHI, 23, 23000, JAIPUR)
-- INSERT INTO EMP VALUES(107, AJIT, 24, 23000, TUKKUGUDA);

-- INSERT MULTIPLE VALUES IN SINGLE LINE
INSERT INTO EMP VALUES
(101, ANIL, 20, 23000, NOIDA),
(102, AMIT, 26, 23000, MAU),
(103, ANKIT, 30, 23000, DELHI),
(104, ANITA, 25, 23000, NOIDA),
(105, ARPIT, 22, 23000, VARANSI),
(106, ABHI, 23, 23000, JAIPUR),
(107, AJIT, 24, 23000, TUKKUGUDA);

SELECT * FROM EMP WHERE CITY='NOIDA';
SELECT * FROM EMP WHERE AGE>=20;
SELECT NAME FROM EMP WHERE AGE!=30;

SELECT ID,NAME FROM EMP WHERE CITY='MAU' AND AGE>=20;
SELECT NAME FROM EMP WHERE ( CITY='MAU' OR CITY='VARANASI' OR CITY='DELHI') AND AGE>=20;

SELECT * FROM EMP WHERE NAME LIKE'%I';
SELECT * FROM EMP WHERE NAME LIKE'_%E';
SELECT * FROM EMP WHERE NAME LIKE'___';
SELECT * FROM EMP WHERE NAME LIKE'%A%'; -- IT'S GIVE THOES NAME WHICH IS END WITH A
SELECT * FROM EMP WHERE NAME LIKE'%A_%';
-- SELECT * FROM EMP;
```

# 19/10/2026

### Retriving reocrds using IN & NOT IN operator.

```sql
SELECT * FROM EMP WHERE CITY IN('NOIDA','DELHI');
SELECT * FROM EMP WHERE CITY NOT IN('NOIDA','DELHI');
SELECT * FROM EMP WHERE ID IN(44,33,22);
SELECT * FROM EMP WHERE ID NOT IN(44,33,22);
```

### Retriving records using between & not between operator.

```sql
SELECT * FROM EMP WHERE AGE BETWEEN 20 AND 25;
SELECT * FROM EMP WHERE AGE NOT BETWEEN 20 AND 25;
SELECT * FROM EMP WHERE SALARY BETWEEN 20000 AND 250000;
SELECT * FROM EMP WHERE SALARY NOT BETWEEN 20000 AND 250000;
```

### Retriving records using order by Clause.

```sql
SELECT * FROM EMP ORDER BY NAME;
SELECT * FROM EMP ORDER BY NAME DESC;
SELECT * FROM EMP ORDER BY AGE;
```

### Retriving rocords using IS NULL & IS NOT NULL operator.

```sql
SELECT * FROM EMP WHERE COMMISSION IS NULL;
SELECT * FROM EMP WHERE COMMISSION IS NOT NULL;
```

### Retriving records using LIMIT

```sql
-- How to find out top 3 records
SELECT * FROM EMP LIMIT 3;

-- How to find out bottom 3 records
SELECT * FROM EMP LIMIT 5,3;
SELECT * FROM EMP LIMIT 2,2;
```

## MySQL Aggregate Functions/ Multiple Row Functions/ Window Functions:-

1. SUM()
2. AVG()
3. MAX()
4. MIN()
5. COUNT() -- It's work on string and integer but sum,max.. are work only integer type.

```sql
INSERT INTO EMP(ID,AGE,SALARY,CITY) VALUES(99,23000,HYD);
SELECT SUM(SALARY) FROM EMP;
SELECT SUM(SALARY) AS 'Total_Salary' FROM EMP;

SELECT MAX(AGE) FROM EMP;
SELECT MIN(AGE) FROM EMP;

SELECT AVG(AGE) FROM EMP;   ---2345.9956734999
SELECT ROUND(AVG(AGE),2) FROM EMP;  ----2345.99

SELECT COUNT(*) AS 'Count' FROM EMP;
SELECT COUNT(ID) FROM EMP;  --
SELECT COUNT(NAME) FROM EMP: -- Not count null records.

-- Used ALL aggregate Function
SELECT SUM(SALARY) AS 'SUM',
MAX(AGE) AS 'MAX',
MIN(AGE) AS 'MIN',
ROUND(AVG(AGE),2) AS 'AVG',
COUNT(*) AS 'Count' FROM EMP;
```

# 21/10/2026

```sql
-- ANSWER 1
CREATE TABLE EMP2(ID INT, NAME VARCHAR(20), DOB DATE, DOJ DATE, BDAY INT, JDAY INT);
INSERT INTO EMP2 VALUES
(101, 'AMIT', 20/03/2005, 21/01/2026, NULL, NULL),
(102, 'ANITA', 20/04/2005, 21/01/2026, NULL, NULL),
(103, 'ANKITA', 20/05/2005, 21/01/2026, NULL, NULL),
(104, 'ANIL', 20/06/2005, 21/01/2026, NULL, NULL);

  -- Insert Bday and Jday of emp
UPDATE EMP2 SET BDAY=DATE DIFF(NOW(), DOB), JDAY=DATE DIFF(NOW(),DOJ);

-- ANSWER 2
CREATE TABLE EMP3(
  ID int,
  NAME VARCHAR(20),
  DTM DATETIME,
  Dy INT,
  Mt INT,
  Yr INT,
  Hr TIME,
  Mi TIME,
  Se TIME,
  DYNM VARCHAR(30)
  );

SET @now = NOW();

INSERT INTO EMP3 VALUES (
101,'AMIT',@now,DAY(@now),MONTH(@now),YEAR(@now),TIME(@now),MINUTE(@now),SECOND(@now),NULL),
(102,'ANIL',@now,DAY(@now),MONTH(@now),YEAR(@now),TIME(@now),MINUTE(@now),SECOND(@now),NULL),
(103,'ANKIT',@now,DAY(@now),MONTH(@now),YEAR(@now),TIME(@now),MINUTE(@now),SECOND(@now),NULL);


-- How To Find total no of columns in a table
SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='EMP3' AND TABLE_SCHEMA='Company';

-- Count total no of tables in database
SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME='DB_NAME';

```
# 22/10/2026

## 
```sql


SELECT SUBSTRING(NAME,2,2) AS 'Substring' FROM EMP;
SELECT LENGTH(NAME) AS 'Len' FROM EMP;
SELECT REVERSE(CITY) AS 'Rev' FROM EMP;
-- SELECT * FROM EMP;
SELECT CONCAT(NAME,SALARY) AS 'CONCAT' FROM EMP;
SELECT CONCAT(NAME,' ',SALARY) AS 'CONCAT' FROM EMP; --It's give space between name and salary
CREATE TABLE EMP_NEW AS SELECT ID, UPPER(NAME) AS 'NM' LEFT(NAME,3) AS 'LEFT', CONCAT(AGE,' ', SALARY) AS 'AG-SAL', RIGHT(CITY,3) AS 'ROGHT', LENGTH(CITY) AS 'LEN', REVERSE(CITY) AS 'REV', 

-- HOW TO CONVERT TITLE NAME OF EVERY EMPLOYEE
SELECT ID, CONCAT(UPPER(LEFT(NAME,1)),LOWER(SUBSTRING(NAME,2))) AS 'NAME' , AGE, SALARY, CONCAT(UPPER(LEFT(CITY,1)),LOWER(SUBSTRING(CITY,2))) AS 'CITY' FROM EMP;



```
