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
4. Boolean
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

### DDL -( CREATE ALTER DROP TRUNCAT RENAME )


```sql
CREATE DATABASE IF NOT EXISTS training_db;
USE training_db;
```

```
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```