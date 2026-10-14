# SQL 
## It's stand for structured query language, Definition of Database:- It's a collection of information that can be organized so that it can be access, managed and updated.

### In database all info stored in tabular formet, tables are divided into row and columns horizontal line called row and vertical linecalled columns.

| id | name | age | salary |
| ----------- | ----------- | ----------- | ----------- |
| 123 | anil | 20 | 20K |
| 123 | amit | 22 | 21K |
| 123 | ankit | 25 | 34K |
| 123 | anita | 30 | 56K |

Each row are also called record sample are tuples, Each colums are also called fields attributes or features.

Database -> Schema
Table-> Entity


### Fields -> Records-> Tables-> Database
- A collection of fields are called records
- A collection of records are called Table
- A collection of Tables are called Database

### Table-> It's the strct inside database that contains data, organized in columns.
### Columns-> The name of each column in a table is used to interpret its meaning and is called an attributes.
### Row-> Each row in a table represents a record and is called a tuple.
### RDBMS -> 
RDBMS avoided the navigation model as in old DBMS and intoduced relation model. The relation model has relationship b/w tables using primary keys, foreign keys, and indexes. Thus the teaching and storing of data become faster then the old Navigational model. RDBMS is useful to efficenttly manage vast amount of data and is used in large business appliction.
1. Oracle, 
2. Ms SQL Server DB 
3. MySQl,
4. SQLite3,
5. MariaDB,
6. PostgreaSQl,
7. MS Access

### DBMS -> It's allow the access to the data in the database.
1. FoxPro
2. LibreOffice
3. dBase

### SQL generally operate on rlational databse
### Features of SQL
- It's a non prodedural language.
- It's an English-like lamguage
- It can processs a singler records as well as set of records at a time.
- All SQL statement define what is to be done rather than how it is to be done.
-  SQL has facilities for defining database views, security, transaction etc.

| DBMS | RDBMS |
| ----- | ------|
| 1. Data store in file  | 1. Data store in tabular  |
| 2. It does not support client server architercture | 2. It support CSA  |
| 3. NF not possible  | 3. NF Present  |
| 4. It allow one user to access at a time | 4. More than 1 user  |
| 5. Hierarchical arrangment of data | 5. store data in row and columns  |
| 6. Low software and hardware used | 6. Higher hardware and software used  |
| 7. ACID not support | 7. Support ACID |
| 8. Data redundancy | 8. Remove data redundancy |

### ACID-> Atomiticy, Consistency, Isolation, Durability

# Basic SQL Commands
### SQL commands can be classified into 5 Categories-
1. DDL -( CREATE, ALTER, DROP, TRUNCAT, RENAME )
2. DML -( INSERT, UPDATE, DELETE, MERGE(It not work in mysql , present in oracle SQL Server) )
3. DCL -( LOCK, GRANT, REVOKE )
4. TCL -( ROLLBACK, COMMIT, SAVEPOINT, START TRANSATION )
5. DQL -( SELECT )
6. ADMINISTRATIVE COMMANDS-> SHOW, EXPLAIN(Only MySql), DESC, USE etc...

## DATA TYPES-
1. Numeric Datatype
2. Date and time
3. String/ Charecters
4. Boolean (True/False)
5. Binary
6. Special

| Data Type |	Description	 | Range |
|---------|-----|------|
| BIGINT |	Large integer numbers 8 Byte |	-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 |
| INT |	Standard integer values 4 Byte |	-2,147,483,648 to 2,147,483,647 |
| SMALLINT |	Small integers |	-32,768 to 32,767 |
| MEDIUMINT |       |            |
| TINYINT |	Very small integers |	0 to 255 or -128 to 127 |
| DECIMAL |	Exact fixed-point numbers (e.g., for financial values) |	-10^38 + 1 to 10^38 - 1 |
| NUMERIC |	Similar to DECIMAL, used for precision data |	-10^38 + 1 to 10^38 - 1 |

### Date and time
1. Date
2. time
3. datetime
4. timestamp
5. year
6. day
7. month

### String/ Charecters
1. Char:- Fixed length data type
2. Varchar:- Variable length data type
- It store only number or alphabet or combination of it.

```sql
CREATE TABLE emp( id, int, name char(30), age int, profile varchar(30), salary float );
```

| Value	| CHAR(4) |	Storage Required | VARCHAR(4) |	Storage Required |
|-------|-------|--------|-------|-----|
| ''    |	'    ' |	4 bytes |	''   |	1 byte  |
| 'ab'  |	'ab  ' |	4 bytes |	'ab' |	3 bytes |
| 'abcd' |	'abcd' |	4 bytes |	'abcd' |	5 bytes |
| 'abcdefgh' |	'abcd' |	4 bytes |	'abcd' |	5 bytes |

### Char Imp:- In char we store those kind of data which have fixed size in table. (Ex. Gender, RTO, True/False)


```sql
CREATE TABLE emp( id, int, name varchar(30), age int, profile varchar(30), salary float );
```
; -> Delimiter

### DDL -( CREATE ALTER DROP TRUNCAT RENAME )


```sql
CREATE DATABASE IF NOT EXISTS training_db;
USE training_db;
```

### commands 

```sql
USE db_name
-- How to find out current selected DB
SELECT DATABASE();

-- How to create new table for selected DB
CREATE TABLE table_name(
  empId INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  dept TEXT NOT NULL,
  age INTEGER,
  Salary FLOAT,
  City VARCHAR(20)
);

-- How to select Stc of emp table
explain DB_name;
desc DB_name;

-- How to see all tables in DB
show TABLES;

-- How to insert records in DB
-- Single Records
INSERT INTO EMPLOYEE VALUES (0001, 'Clark', 'Sales',20,4000,'Delhi');
INSERT INTO EMPLOYEE VALUES (0002, 'Dave', 'Accounting',20,4000,'Delhi');
INSERT INTO EMPLOYEE VALUES (0003, 'Ava', 'Sales',20,4000,'Delhi');

-- Multiple Records insert
INSERT INTO EMPLOYEE VALUES (0001, 'Clark', 'Sales',20,4000,'Delhi'),(0002, 'Dave', 'Accounting',20,4000,'Delhi'),(0003, 'Ava', 'Sales',20,4000,'Delhi');

-- How to display all records of EMPLOYEE tables
SELECT * FROM EMPLOYEE;

-- How to see perticular one column
SELECT name FROM EMPLOYEE;

-- How to insert vallues only given columns
INERT INTO EMPLOYEE (empID, name, age) VALUES(200, 'amit', 58);

-- How to update records
UPDATE EMPLOYEE SET name='amit' WHERE empID=0001;

-- How to delete records from employee table
DELETE FROM EMPOLYEE WHERE empID=0001;
DELETE FROM EMPOLYEE WHERE city='dehi';
DELETE FROM EMPOLYEE;

```
# 13/10/2026


# 14/10/2026

### What is diff between truncate and delete
1. 
2. 
3. Rollback work only delete not on truncate.

### What is diff between Delete and drop
1. In drop delete table and strcture but delete only data not strcuture.

### What is diff between Truncate and drop
1. In truncate delete only table not strcture but in drop delete both.

### How to drop database
mysql> DROP DATABASE database_name;

```sql
truncate table emp;
desc emp;
drop emp;
select * emp;

```
# Operators in MYSQL
In mysql operators are in different types
1. Retrivening Records Using Arithmetical Operators:-
+, _ , / , %, *
2. Retriveing Records using Comparision Operator:-
=,<=,>=,!=,<,>
3. Retriving Reocrds using logical operators:-
AND, OR, NOT

4. Retriving Records using like & not like operator:-
LIKE, NOT LIKE ( It used for pattern matching )
 

```sql
-- How to increment 3000 salary in existing salary
UPDATE emp SET salary=salary+3000;

-- How to decrement 3000 salary in existing salary
UPDATE emp SET salary=salary-3000;
SELECT *,price*qty as 'total_sales'

-- How to multiply 3X salary in existing salary
UPDATE emp SET salary=salary*3;

-- How to Divide 1/2 salary in existing salary
UPDATE emp SET salary=salary/2;

-- Comparision Operator - It work with string and numeric
SELECT * from emp WHERE name='raj';
SELECT * from emp WHERE salary!=40000;

SELECT * FROM emp WHERE name='raj' and age=30;


```



```
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```