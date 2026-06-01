# Apache Hive & HDFS Lab Notes (Enhanced Version)

## Big Data Lab Manual

**Topics Covered:**

1. HDFS File Operations
2. Hive Partitioned Tables
3. Hive Bucketed Tables

---

# Part A: HDFS (Hadoop Distributed File System)

## Introduction

HDFS (Hadoop Distributed File System) is the primary storage system of Hadoop. It is designed to store large datasets across multiple machines while providing high throughput and fault tolerance.

### Common HDFS Commands

| Command                 | Description                     |
| ----------------------- | ------------------------------- |
| `hdfs dfs -mkdir`       | Create directory in HDFS        |
| `hdfs dfs -put`         | Upload file to HDFS             |
| `hdfs dfs -get`         | Download file from HDFS         |
| `hdfs dfs -copyToLocal` | Copy HDFS file to local machine |
| `hdfs dfs -ls`          | List files/directories          |
| `hdfs dfs -cat`         | Display file contents           |
| `hdfs dfs -mv`          | Rename or move file             |
| `hdfs dfs -chmod`       | Change file permissions         |
| `hdfs dfs -du -h`       | Display file size               |

---

## Experiment 1: Upload and Manage Student Data

### Objective

Create a text file, upload it to HDFS, assign permissions, and verify storage.

### Commands

```bash
# Create local file
echo "HDFS is designed to store large data sets efficiently." > student_data.txt

# Create HDFS directory
hdfs dfs -mkdir -p /user/student/test_data/

# Upload file
hdfs dfs -put student_data.txt /user/student/test_data/

# Change permissions
hdfs dfs -chmod 640 /user/student/test_data/student_data.txt

# View file content
hdfs dfs -cat /user/student/test_data/student_data.txt

# List directory contents
hdfs dfs -ls /user/student/test_data/
```

### Expected Outcome

* File successfully uploaded to HDFS.
* Permissions set to `rw-r-----`.
* Content displayed correctly.
* Directory listing shows uploaded file.

---

## Experiment 2: Employee Information Management

### Objective

Upload a file, rename it in HDFS, retrieve it locally, and inspect storage usage.

### Commands

```bash
echo "Big data technologies support scalable storage and processing." > employee_info.txt

hdfs dfs -mkdir -p /user/student/emp_data/

hdfs dfs -put employee_info.txt /user/student/emp_data/

hdfs dfs -mv \
/user/student/emp_data/employee_info.txt \
/user/student/emp_data/staff_info.txt

hdfs dfs -get \
/user/student/emp_data/staff_info.txt ./

hdfs dfs -cat \
/user/student/emp_data/staff_info.txt

hdfs dfs -du -h \
/user/student/emp_data/staff_info.txt
```

### Learning Outcome

Students learn:

* File renaming in HDFS
* Downloading files from HDFS
* Monitoring storage consumption

---

## Experiment 3: Library Catalog Management

### Commands

```bash
echo "Hadoop allows scalable and reliable storage for big data applications." > library_catalog.txt

hdfs dfs -mkdir -p /user/librarian/book_data/

hdfs dfs -put library_catalog.txt /user/librarian/book_data/

hdfs dfs -mv \
/user/librarian/book_data/library_catalog.txt \
/user/librarian/book_data/book_catalog.txt

hdfs dfs -get \
/user/librarian/book_data/book_catalog.txt ./

hdfs dfs -cat \
/user/librarian/book_data/book_catalog.txt

hdfs dfs -du -h \
/user/librarian/book_data/book_catalog.txt
```

---

## Experiment 4: Sales Report Processing

### Commands

```bash
printf "Product,Sales,Revenue\nWidget,150,2000\nGadget,200,3000\n" > sales_report.csv

hdfs dfs -mkdir -p /user/sales/quarterly_reports/

hdfs dfs -put sales_report.csv \
/user/sales/quarterly_reports/

hdfs dfs -mv \
/user/sales/quarterly_reports/sales_report.csv \
/user/sales/quarterly_reports/Q1_sales_report.csv

hdfs dfs -copyToLocal \
/user/sales/quarterly_reports/Q1_sales_report.csv ./

hdfs dfs -cat \
/user/sales/quarterly_reports/Q1_sales_report.csv

hdfs dfs -du -h \
/user/sales/quarterly_reports/Q1_sales_report.csv
```

---

# Part B: Apache Hive

## Introduction

Apache Hive is a data warehouse system built on Hadoop that enables querying and analyzing large datasets using SQL-like language called HiveQL.

### Advantages of Hive

* SQL-like querying
* Scalable storage
* Data warehousing support
* Integration with Hadoop ecosystem
* Suitable for batch processing

---

# Hive Partitioning

## What is Partitioning?

Partitioning divides table data into separate physical directories based on partition column values.

### Benefits

* Faster query execution
* Reduced data scanning
* Improved performance
* Efficient storage organization

### Example

Instead of scanning all records:

```sql
SELECT * FROM orders
WHERE region='North';
```

Hive scans only the `North` partition.

---

# Experiment 5: Partitioned Table – Orders

## Objective

Create a partitioned table and store data according to regions.

### Table Creation

```sql
CREATE TABLE orders (
    order_id INT,
    customer STRING,
    amount INT
)
PARTITIONED BY (region STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;
```

### Enable Dynamic Partitioning

```sql
SET hive.exec.dynamic.partition=true;
SET hive.exec.dynamic.partition.mode=nonstrict;
```

### Insert Data

```sql
INSERT INTO TABLE orders
PARTITION(region='North')
VALUES
(101,'Alice',5000),
(102,'Bob',3200);

INSERT INTO TABLE orders
PARTITION(region='South')
VALUES
(103,'Charlie',4500),
(104,'David',1200);
```

### Query Data

```sql
SELECT *
FROM orders
WHERE region='North';
```

### Directory Structure

```text
orders/
├── region=North
└── region=South
```

---

# Experiment 6: Partitioned Table – Sales Data

## Create Table

```sql
CREATE TABLE sales_data (
    sale_id INT,
    product_name STRING,
    quantity INT,
    price INT
)
PARTITIONED BY (city STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',';
```

## Insert Data

### Delhi Partition

```sql
INSERT INTO TABLE sales_data
PARTITION(city='Delhi')
VALUES
(1,'Laptop',5,85000),
(2,'Headphones',12,7000),
(5,'Mouse',20,1500);
```

### Mumbai Partition

```sql
INSERT INTO TABLE sales_data
PARTITION(city='Mumbai')
VALUES
(3,'Mobile',8,45000),
(4,'Table',3,18000);
```

## Queries

### Display Delhi Records

```sql
SELECT *
FROM sales_data
WHERE city='Delhi';
```

### Total Quantity Sold by City

```sql
SELECT city,
       SUM(quantity) AS total_quantity
FROM sales_data
GROUP BY city;
```

### Display Entire Table

```sql
SELECT *
FROM sales_data;
```

---

# Hive Bucketing

## What is Bucketing?

Bucketing divides data into a fixed number of files using a hash function on a specified column.

### Formula

```text
Bucket Number = HASH(Column Value) % Number of Buckets
```

### Benefits

* Faster joins
* Efficient data sampling
* Better query optimization
* Balanced data distribution

---

## Enable Bucketing

```sql
SET hive.enforce.bucketing=true;
```

---

# Experiment 7: Bucketed Table – Department Employees

## Create Table

```sql
CREATE TABLE department_employees (
    emp_id INT,
    name STRING,
    salary INT,
    department STRING
)
CLUSTERED BY(emp_id)
INTO 3 BUCKETS
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',';
```

## Insert Data

```sql
INSERT INTO department_employees VALUES
(1,'Aman',65000,'IT'),
(2,'Riya',72000,'HR'),
(3,'Karan',48000,'Finance'),
(4,'Simran',55000,'IT'),
(5,'Neha',90000,'Admin'),
(6,'Raj',42000,'HR'),
(7,'Amit',81000,'Finance'),
(8,'Vikram',60000,'IT');
```

## Query

```sql
SELECT *
FROM department_employees
ORDER BY emp_id;
```

---

# Experiment 8: Bucketed Table – Student Marks

## Create Table

```sql
CREATE TABLE student_marks (
    student_id INT,
    student_name STRING,
    marks INT,
    subject STRING
)
CLUSTERED BY(student_id)
INTO 4 BUCKETS
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',';
```

## Query 1: Marks Above 75

```sql
SELECT *
FROM student_marks
WHERE marks > 75;
```

## Query 2: Subject-wise Average

```sql
SELECT subject,
       AVG(marks) AS average_marks
FROM student_marks
GROUP BY subject;
```

---

# Experiment 9: Bucketed Table – Movie Rentals

## Create Table

```sql
CREATE TABLE movie_rentals (
    rental_id INT,
    movie_title STRING,
    rental_price INT,
    customer_city STRING
)
CLUSTERED BY(rental_id)
INTO 4 BUCKETS
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',';
```

## Query 1

```sql
SELECT *
FROM movie_rentals
WHERE rental_price > 300;
```

## Query 2

```sql
SELECT customer_city,
       SUM(rental_price) AS total_revenue
FROM movie_rentals
GROUP BY customer_city;
```

---

# Experiment 10: Bucketed Table – Employee Data

## Create Table

```sql
CREATE TABLE employee_data (
    emp_id INT,
    emp_name STRING,
    department STRING,
    salary INT
)
CLUSTERED BY(emp_id)
INTO 4 BUCKETS
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',';
```

## Display All Records

```sql
SELECT *
FROM employee_data;
```

---

# Viva Questions

### Q1. What is HDFS?

HDFS is Hadoop's distributed storage system used for storing large-scale data across multiple machines.

### Q2. What is Apache Hive?

Hive is a data warehouse tool that provides SQL-like querying on Hadoop data.

### Q3. What is Partitioning?

Partitioning separates table data into directories based on partition column values.

### Q4. What is Bucketing?

Bucketing distributes data into fixed buckets using a hash function.

### Q5. Difference Between Partitioning and Bucketing?

| Partitioning                 | Bucketing                   |
| ---------------------------- | --------------------------- |
| Based on column values       | Based on hash function      |
| Creates directories          | Creates files               |
| Reduces scan range           | Improves joins and sampling |
| Dynamic number of partitions | Fixed number of buckets     |

---

# Summary

After completing these experiments, students will be able to:

✅ Perform file operations in HDFS

✅ Manage permissions and storage in Hadoop

✅ Create and query partitioned Hive tables

✅ Create and query bucketed Hive tables

✅ Use HiveQL for filtering, aggregation, and analysis

✅ Understand performance optimization using Partitioning and Bucketing

**Key Concepts Covered:** HDFS, HiveQL, Partitioning, Bucketing, Data Warehousing, Big Data Storage, Query Optimization.
