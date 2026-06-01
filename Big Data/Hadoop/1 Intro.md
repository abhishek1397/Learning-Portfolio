# Hadoop, Hive, and Scala Notes

*Prepared from the uploaded lecture content* 

---

# Module 1: Hadoop HDFS Basics

## What is HDFS?

HDFS (Hadoop Distributed File System) is Hadoop's storage layer used to store large datasets across multiple machines.

### Common HDFS Commands

### Create Directory

```bash
hdfs dfs -mkdir /sb
```

### Upload File to HDFS

```bash
hdfs dfs -put D:\data.txt /sb
```

### Display File Content

```bash
hdfs dfs -cat /outputsb/part-r-00000
```

### Run WordCount MapReduce Program

```bash
hadoop jar C:\hadoopsetup\hadoop-3.2.4\share\hadoop\mapreduce\hadoop-mapreduce-examples-3.2.4.jar wordcount /sb/data.txt /outputsb
```

---

# Module 2: Hive Database Operations

## Database Management

### Show Existing Databases

```sql
SHOW DATABASES;
```

### Create Database

```sql
CREATE DATABASE sd;
```

### Create Database if Not Exists

```sql
CREATE DATABASE IF NOT EXISTS abc;
```

### Drop Database

```sql
DROP DATABASE abc;
```

### Drop Database Safely

```sql
DROP DATABASE IF EXISTS demo;
```

---

## Database Properties

### Create Database with Metadata

```sql
CREATE DATABASE demo
WITH DBPROPERTIES
(
'creator'='Gaurav Chawla',
'date'='2019-06-03'
);
```

### View Database Metadata

```sql
DESCRIBE DATABASE EXTENDED demo;
```

---

# Module 3: Hive Tables

## Creating Employee Table

```sql
CREATE TABLE sd.emp
(
Id INT,
ename STRING,
age INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',';
```

### Check Table Structure

```sql
DESCRIBE sd.emp;
```

---

## Loading Data

```sql
LOAD DATA LOCAL INPATH 'D:\emp_details.txt'
INTO TABLE sd.emp;
```

### View Data

```sql
SELECT * FROM sd.emp;
```

Sample Data:

```text
101, PRIYA, 28
102, RAHUL, 27
103, RAJ, 25
```

---

# Module 4: Hive Query Operations

## Conditional Filtering

### Less Than

```sql
SELECT * FROM sd.emp
WHERE age < 27;
```

### Greater Than

```sql
SELECT * FROM sd.emp
WHERE age > 27;
```

### Less Than or Equal

```sql
SELECT * FROM sd.emp
WHERE age <= 27;
```

### Greater Than or Equal

```sql
SELECT * FROM sd.emp
WHERE age >= 27;
```

### Equal To

```sql
SELECT * FROM sd.emp
WHERE age = 27;
```

### NULL Checks

```sql
SELECT * FROM sd.emp
WHERE age IS NULL;
```

```sql
SELECT * FROM sd.emp
WHERE age IS NOT NULL;
```

---

## Arithmetic Operations

### Add

```sql
SELECT ename, age+5
FROM sd.emp;
```

### Subtract

```sql
SELECT ename, age-5
FROM sd.emp;
```

### Multiply

```sql
SELECT ename, age*5
FROM sd.emp;
```

### Divide

```sql
SELECT ename, age/5
FROM sd.emp;
```

### Modulus

```sql
SELECT ename, age%5
FROM sd.emp;
```

---

# Module 5: Group By and Aggregation

## Student Table

```sql
CREATE TABLE sd.student
(
sid INT,
sname STRING,
age INT,
branch STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',';
```

### Load Data

```sql
LOAD DATA LOCAL INPATH 'D:\student.txt'
INTO TABLE sd.student;
```

Sample Data

| SID | Name | Age | Branch |
| --- | ---- | --- | ------ |
| 101 | A    | 21  | CSE    |
| 102 | B    | 22  | CSE    |
| 103 | C    | 22  | ECE    |
| 104 | D    | 21  | MEC    |

---

### Filter by Branch

```sql
SELECT *
FROM sd.student
WHERE branch='CSE';
```

### Count Students Branch-wise

```sql
SELECT branch,
COUNT(sid)
FROM sd.student
GROUP BY branch;
```

### HAVING Clause

```sql
SELECT branch,
COUNT(sid)
FROM sd.student
GROUP BY branch
HAVING COUNT(sid) > 2;
```

### Sorting

```sql
SELECT *
FROM sd.student
ORDER BY age DESC;
```

---

# Module 6: Alter Table Operations

## Create Table

```sql
CREATE TABLE ds.emp1
(
Id INT,
ename STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',';
```

### Rename Table

```sql
ALTER TABLE ds.emp1
RENAME TO ds.emp2;
```

### Add New Column

```sql
ALTER TABLE ds.emp2
ADD COLUMNS
(
father_name STRING
);
```

---

# Module 7: Bucketing in Hive

## Concept

Bucketing distributes rows into fixed files (buckets) using a hash function.

### Benefits

* Faster joins
* Efficient sampling
* Better query optimization
* Even data distribution

---

## Enable Bucketing

```sql
SET hive.enforce.bucketing=true;
```

---

## Source Table

```sql
CREATE TABLE sd.emp_demo
(
Id INT,
Name STRING,
Salary FLOAT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',';
```

Load Data:

```sql
LOAD DATA LOCAL INPATH 'D:\emp.txt'
INTO TABLE sd.emp_demo;
```

---

## Bucketed Table

```sql
CREATE TABLE sd.empbucket1
(
Id INT,
Name STRING,
Salary FLOAT
)
CLUSTERED BY(Id)
INTO 3 BUCKETS
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',';
```

### Insert Data

```sql
INSERT OVERWRITE TABLE sd.empbucket1
SELECT * FROM sd.emp_demo;
```

---

# Module 8: Partitioning in Hive

## Concept

Partitioning physically divides table data based on column values.

### Benefits

* Faster query execution
* Reduced data scanning
* Better storage organization

---

## Create Base Table

```sql
CREATE TABLE sd.states
(
state STRING,
city STRING,
pop BIGINT
);
```

---

## Load Data

```sql
LOAD DATA LOCAL INPATH 'D:\usstates.txt'
INTO TABLE sd.states;
```

---

## Create Partitioned Table

```sql
CREATE TABLE sd.part
(
city STRING,
pop BIGINT
)
PARTITIONED BY
(
state STRING
);
```

---

## Insert Data into Partitions

```sql
INSERT OVERWRITE TABLE sd.part
PARTITION(state)
SELECT city,
       pop,
       state
FROM sd.states;
```

---

## Check Partition Directories

```bash
hadoop fs -ls /user/hive/warehouse/part/
```

---

## Dynamic Partitioning

```sql
SET hive.exec.dynamic.partition.mode=nonstrict;
```

---

# Module 9: Exam-Oriented Scenarios

## HDFS Data Management Workflow

### Create Directory

```bash
hdfs dfs -mkdir /company/logs/2026/march
```

### Upload File

```bash
hdfs dfs -put weblogsmarch13.txt /company/logs/2026/march
```

### Verify Upload

```bash
hdfs dfs -ls /company/logs/2026/march
```

### Display First 20 Lines

```bash
hdfs dfs -cat /company/logs/2026/march/weblogsmarch13.txt | head -20
```

### Create Backup Directory

```bash
hdfs dfs -mkdir /company/logsbackup
```

### Copy File

```bash
hdfs dfs -cp \
/company/logs/2026/march/weblogsmarch13.txt \
/company/logsbackup
```

### Check Disk Usage

```bash
hdfs dfs -du -h /company/logs
```

### Delete Backup File

```bash
hdfs dfs -rm \
/company/logsbackup/weblogsmarch13.txt
```

---

# Module 10: Hive Interview Concepts

## Partitioning vs Bucketing

| Feature             | Partitioning         | Bucketing        |
| ------------------- | -------------------- | ---------------- |
| Data Split Based On | Column Values        | Hash Function    |
| Number of Divisions | Variable             | Fixed            |
| Query Optimization  | Very High            | Moderate         |
| Best Use Case       | Filtering            | Joins & Sampling |
| Storage Structure   | Separate Directories | Separate Files   |

### Example

Partition by:

```text
State
Month
```

Bucket by:

```text
Passenger_ID
Customer_ID
Employee_ID
```

---

# Module 11: Scala Basics

## Immutable Variable (val)

```scala
val a:Int = 10
```

Cannot be modified.

```scala
val mess:String = "hello"
mess = "unbox"
```

Output:

```text
error: reassignment to val
```

---

## Mutable Variable (var)

```scala
var mess:String = "hello"
mess = "unbox"
```

Allowed because `var` is mutable.

---

## Print

```scala
print("hello")
print("3")
print("hi ?")
```

Output:

```text
hello3hi ?
```

---

## Println

```scala
println("hello")
println("3")
println("hi ?")
```

Output:

```text
hello
3
hi ?
```

---

## String Concatenation

```scala
print("hello" + "world" + "01")
```

Output:

```text
helloworld01
```

---

# Quick Revision Sheet

### HDFS Commands

```bash
mkdir
put
get
cat
cp
mv
rm
du
ls
```

### Hive DDL

```sql
CREATE DATABASE
DROP DATABASE
CREATE TABLE
ALTER TABLE
DESCRIBE
LOAD DATA
```

### Hive DQL

```sql
SELECT
WHERE
GROUP BY
HAVING
ORDER BY
```

### Hive Optimization

```text
Partitioning → Faster Filtering
Bucketing → Faster Joins & Sampling
```

### Scala Keywords

```scala
val  -> Immutable
var  -> Mutable
print
println
```

These notes cover the complete Hadoop HDFS → Hive DDL/DML → Partitioning → Bucketing → Scala basics sequence present in the uploaded material. 
