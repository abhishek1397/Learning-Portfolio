For assignment/lab submission, it is best to write **each question followed immediately by its answer**, while still grouping all **HDFS questions first** and then all **Hive questions**. This format is cleaner, examiner-friendly, and easier for viva preparation.

# HDFS and Hive Lab Notes with Questions and Answers

# PART A – HDFS (Hadoop Distributed File System)

## Introduction

HDFS (Hadoop Distributed File System) is the storage layer of Hadoop that stores large datasets across multiple machines and provides fault tolerance and high availability.

### Common HDFS Commands

| Operation         | Command                                          |
| ----------------- | ------------------------------------------------ |
| Create Directory  | `hdfs dfs -mkdir -p <path>`                      |
| Upload File       | `hdfs dfs -put <file> <path>`                    |
| Download File     | `hdfs dfs -get <hdfs-file> <local-path>`         |
| Copy to Local     | `hdfs dfs -copyToLocal <hdfs-file> <local-path>` |
| Rename File       | `hdfs dfs -mv <old-path> <new-path>`             |
| Change Permission | `hdfs dfs -chmod <permission> <file>`            |
| Display Content   | `hdfs dfs -cat <file>`                           |
| List Files        | `hdfs dfs -ls <directory>`                       |
| Check File Size   | `hdfs dfs -du -h <file>`                         |

---

# Question 1 – Student Data Operations

### Question

Write the HDFS commands for the following operations:

(a) Create a local file named `student_data.txt` containing the text:

"HDFS is designed to store large data sets efficiently."

(b) Upload the file to HDFS directory `/user/student/test_data/`

(c) Change permissions so that:

* Owner → Read & Write
* Group → Read Only
* Others → No Permission

(d) Display the file contents and list all files in the directory.

### Answer

| Task                  | Command                                                                            |
| --------------------- | ---------------------------------------------------------------------------------- |
| Create Local File     | `echo "HDFS is designed to store large data sets efficiently." > student_data.txt` |
| Create HDFS Directory | `hdfs dfs -mkdir -p /user/student/test_data/`                                      |
| Upload File           | `hdfs dfs -put student_data.txt /user/student/test_data/`                          |
| Change Permission     | `hdfs dfs -chmod 640 /user/student/test_data/student_data.txt`                     |
| Display File Content  | `hdfs dfs -cat /user/student/test_data/student_data.txt`                           |
| List Files            | `hdfs dfs -ls /user/student/test_data/`                                            |

---

# Question 2 – Employee Information Management

### Question

(a) Create a local file named `employee_info.txt` containing:

"Big data technologies support scalable storage and processing."

(b) Create `/user/student/emp_data/` and upload the file.

(c) Rename the file to `staff_info.txt`.

(d) Copy the renamed file back to the local file system.

(e) Display contents and check file size.

### Answer

| Task             | Command                                                                                       |
| ---------------- | --------------------------------------------------------------------------------------------- |
| Create File      | `echo "Big data technologies support scalable storage and processing." > employee_info.txt`   |
| Create Directory | `hdfs dfs -mkdir -p /user/student/emp_data/`                                                  |
| Upload File      | `hdfs dfs -put employee_info.txt /user/student/emp_data/`                                     |
| Rename File      | `hdfs dfs -mv /user/student/emp_data/employee_info.txt /user/student/emp_data/staff_info.txt` |
| Download File    | `hdfs dfs -get /user/student/emp_data/staff_info.txt ./`                                      |
| Display Content  | `hdfs dfs -cat /user/student/emp_data/staff_info.txt`                                         |
| Check File Size  | `hdfs dfs -du -h /user/student/emp_data/staff_info.txt`                                       |

---

# Question 3 – Library Catalog Management

### Question

1. Create a local file named `library_catalog.txt` containing:

"Hadoop allows scalable and reliable storage for big data applications."

2. Upload the file to `/user/librarian/book_data/`

3. Rename it to `book_catalog.txt`

4. Download the file back to local system

5. Display contents and verify file size

### Answer

| Task             | Command                                                                                                 |
| ---------------- | ------------------------------------------------------------------------------------------------------- |
| Create File      | `echo "Hadoop allows scalable and reliable storage for big data applications." > library_catalog.txt`   |
| Create Directory | `hdfs dfs -mkdir -p /user/librarian/book_data/`                                                         |
| Upload File      | `hdfs dfs -put library_catalog.txt /user/librarian/book_data/`                                          |
| Rename File      | `hdfs dfs -mv /user/librarian/book_data/library_catalog.txt /user/librarian/book_data/book_catalog.txt` |
| Download File    | `hdfs dfs -get /user/librarian/book_data/book_catalog.txt ./`                                           |
| Display Content  | `hdfs dfs -cat /user/librarian/book_data/book_catalog.txt`                                              |
| Verify Size      | `hdfs dfs -du -h /user/librarian/book_data/book_catalog.txt`                                            |

---

# Question 4 – Sales Report Processing

### Question

Create a local file named `sales_report.csv` containing:

Product,Sales,Revenue

Widget,150,2000

Gadget,200,3000

Upload it to HDFS, rename it as `Q1_sales_report.csv`, download it, display its contents and verify file size.

### Answer

| Task             | Command                                                                                                         |
| ---------------- | --------------------------------------------------------------------------------------------------------------- |
| Create CSV File  | `printf "Product,Sales,Revenue\nWidget,150,2000\nGadget,200,3000\n" > sales_report.csv`                         |
| Create Directory | `hdfs dfs -mkdir -p /user/sales/quarterly_reports/`                                                             |
| Upload File      | `hdfs dfs -put sales_report.csv /user/sales/quarterly_reports/`                                                 |
| Rename File      | `hdfs dfs -mv /user/sales/quarterly_reports/sales_report.csv /user/sales/quarterly_reports/Q1_sales_report.csv` |
| Download File    | `hdfs dfs -copyToLocal /user/sales/quarterly_reports/Q1_sales_report.csv ./`                                    |
| Display Content  | `hdfs dfs -cat /user/sales/quarterly_reports/Q1_sales_report.csv`                                               |
| Verify Size      | `hdfs dfs -du -h /user/sales/quarterly_reports/Q1_sales_report.csv`                                             |

---

# Question 5 – Course Information File

### Question

(a) Create a local file named `course_info.txt` containing:

"Big Data tools help process and analyze large-scale datasets."

(b) Upload it to `/user/student/course_files/`

(c) Set permissions:

* Owner → Read, Write, Execute
* Group → Read Only
* Others → No Permission

(d) Display file contents and list all files.

### Answer

| Task              | Command                                                                                  |
| ----------------- | ---------------------------------------------------------------------------------------- |
| Create File       | `echo "Big Data tools help process and analyze large-scale datasets." > course_info.txt` |
| Create Directory  | `hdfs dfs -mkdir -p /user/student/course_files/`                                         |
| Upload File       | `hdfs dfs -put course_info.txt /user/student/course_files/`                              |
| Change Permission | `hdfs dfs -chmod 740 /user/student/course_files/course_info.txt`                         |
| Display Content   | `hdfs dfs -cat /user/student/course_files/course_info.txt`                               |
| List Files        | `hdfs dfs -ls /user/student/course_files/`                                               |

---

# PART B – APACHE HIVE

## Introduction

Apache Hive is a data warehouse framework built on Hadoop that provides SQL-like querying using HiveQL.

### Partitioning

Partitioning divides table data into separate directories based on partition column values.

### Bucketing

Bucketing distributes data into a fixed number of files using a hash function.

---

# Question 6 – Orders Table (Partitioning)

### Question

Create a Hive table named `orders` with columns:

* order_id INT
* customer STRING
* amount INT

Partition the table using column `region`.

Insert records into North and South partitions and display only North records.

### Answer

```sql
CREATE TABLE orders(
order_id INT,
customer STRING,
amount INT
)
PARTITIONED BY(region STRING);
```

```sql
INSERT INTO orders PARTITION(region='North')
VALUES
(101,'Alice',5000),
(102,'Bob',3200);

INSERT INTO orders PARTITION(region='South')
VALUES
(103,'Charlie',4500),
(104,'David',1200);
```

```sql
SELECT *
FROM orders
WHERE region='North';
```

---

# Question 7 – Sales Data Table (Partitioning)

### Question

Create table `sales_data`:

* sale_id INT
* product_name STRING
* quantity INT
* price INT

Partition using city.

Insert records into Delhi and Mumbai partitions.

Display Delhi records and calculate total quantity city-wise.

### Answer

```sql
CREATE TABLE sales_data(
sale_id INT,
product_name STRING,
quantity INT,
price INT
)
PARTITIONED BY(city STRING);
```

```sql
INSERT INTO sales_data PARTITION(city='Delhi')
VALUES
(1,'Laptop',5,85000),
(2,'Headphones',12,7000);

INSERT INTO sales_data PARTITION(city='Mumbai')
VALUES
(3,'Mobile',8,45000),
(4,'Keyboard',15,1200);
```

```sql
SELECT *
FROM sales_data
WHERE city='Delhi';
```

```sql
SELECT city,
SUM(quantity) AS total_quantity
FROM sales_data
GROUP BY city;
```

---

# Question 8 – Sales Data Table (Alternative Version)

### Question

Create a partitioned table with:

* sale_id INT
* product STRING
* quantity INT

Partition by city.

Display Delhi records and all records.

### Answer

```sql
CREATE TABLE sales_data(
sale_id INT,
product STRING,
quantity INT
)
PARTITIONED BY(city STRING);
```

```sql
INSERT INTO sales_data PARTITION(city='Delhi')
VALUES
(1,'Laptop',5),
(2,'Mouse',10);

INSERT INTO sales_data PARTITION(city='Mumbai')
VALUES
(3,'Mobile',8),
(4,'Keyboard',15);
```

```sql
SELECT *
FROM sales_data
WHERE city='Delhi';
```

```sql
SELECT *
FROM sales_data;
```

---

# Question 9 – Department Employees (Bucketing)

### Question

Create table `department_employees` using 3 buckets on emp_id and insert at least 8 records.

### Answer

```sql
CREATE TABLE department_employees(
emp_id INT,
name STRING,
salary INT,
department STRING
)
CLUSTERED BY(emp_id)
INTO 3 BUCKETS;
```

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

```sql
SELECT *
FROM department_employees
ORDER BY emp_id;
```

---

# Question 10 – Student Marks (Bucketing)

### Question

Create a bucketed table with 4 buckets on student_id, insert 8 records, display marks greater than 75 and show subject-wise average.

### Answer

```sql
CREATE TABLE student_marks(
student_id INT,
student_name STRING,
marks INT,
subject STRING
)
CLUSTERED BY(student_id)
INTO 4 BUCKETS;
```

```sql
INSERT INTO student_marks VALUES
(101,'Rahul',82,'Math'),
(102,'Priya',91,'Science'),
(103,'Aman',68,'Math'),
(104,'Neha',88,'English'),
(105,'Karan',76,'Science'),
(106,'Simran',95,'Math'),
(107,'Riya',72,'English'),
(108,'Vikram',80,'Science');
```

```sql
SELECT *
FROM student_marks
WHERE marks > 75;
```

```sql
SELECT subject,
AVG(marks) AS average_marks
FROM student_marks
GROUP BY subject;
```

---

# Question 11 – Movie Rentals (Bucketing)

### Question

Create a bucketed table with 4 buckets on rental_id, insert the given 8 records, display rentals greater than 300 and show city-wise total rental price.

### Answer

```sql
CREATE TABLE movie_rentals(
rental_id INT,
movie_title STRING,
rental_price INT,
customer_city STRING
)
CLUSTERED BY(rental_id)
INTO 4 BUCKETS;
```

```sql
INSERT INTO movie_rentals VALUES
(301,'Inception',300,'San Francisco'),
(302,'The Dark Knight',350,'Los Angeles'),
(303,'The Matrix',250,'Chicago'),
(304,'Interstellar',400,'New York'),
(305,'Avatar',450,'San Francisco'),
(306,'The Godfather',500,'Los Angeles'),
(307,'Titanic',150,'Chicago'),
(308,'The Shawshank Redemption',200,'New York');
```

```sql
SELECT *
FROM movie_rentals
WHERE rental_price > 300;
```

```sql
SELECT customer_city,
SUM(rental_price) AS total_rental_price
FROM movie_rentals
GROUP BY customer_city;
```

---

# Question 12 – Employee Data (Bucketing)

### Question

Create a bucketed table using 4 buckets on emp_id, insert at least 6 records and display all records.

### Answer

```sql
CREATE TABLE employee_data(
emp_id INT,
emp_name STRING,
department STRING,
salary INT
)
CLUSTERED BY(emp_id)
INTO 4 BUCKETS;
```

```sql
INSERT INTO employee_data VALUES
(101,'Aman','IT',65000),
(102,'Riya','HR',55000),
(103,'Karan','Finance',70000),
(104,'Neha','Marketing',60000),
(105,'Raj','IT',75000),
(106,'Simran','HR',58000);
```

```sql
SELECT *
FROM employee_data;
```


