# Test-1 (T-SQL Level 1)

For **Level 1**, focus on basic DDL operations:

* `CREATE DATABASE`
* `CREATE TABLE`
* `ALTER TABLE`
* `DROP`
* `TRUNCATE`
* `RENAME`
* Constraints (`PRIMARY KEY`, `NOT NULL`, `UNIQUE`, `DEFAULT`)
* Data types

## Q1. Create a database named `collegeDB` and select/use that database.

**Answer:**

```sql
CREATE DATABASE collegeDB;
USE collegeDB;
```


## Q2. Create a table named `students` with the following columns:

| Column     | Data Type   | Constraint  |
| ---------- | ----------- | ----------- |
| student_id | INT         | PRIMARY KEY |
| name       | VARCHAR(50) | NOT NULL    |
| age        | INT         |             |
| department | VARCHAR(30) |             |
| email      | VARCHAR(50) | UNIQUE      |

**Answer:**

```sql
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT,
    department VARCHAR(30),
    email VARCHAR(50) UNIQUE
);
```


## Q3. Create a table named `faculty` with the following columns:

| Column       | Data Type   | Constraint  |
| ------------ | ----------- | ----------- |
| faculty_id   | INT         | PRIMARY KEY |
| faculty_name | VARCHAR(50) | NOT NULL    |
| subject      | VARCHAR(40) |             |
| salary       | FLOAT       |             |

**Answer:**

```sql
CREATE TABLE faculty (
    faculty_id INT PRIMARY KEY,
    faculty_name VARCHAR(50) NOT NULL,
    subject VARCHAR(40),
    salary FLOAT
);
```


## Q4. Add a new column `phone_number VARCHAR(15)` to the `students` table.

**Answer:**

```sql
ALTER TABLE students
ADD phone_number VARCHAR(15);
```


## Q5. Modify the `salary` column in the `faculty` table from `FLOAT` to `DECIMAL(10,2)`.

**Answer:**

```sql
ALTER TABLE faculty
ALTER COLUMN salary DECIMAL(10,2);
```


## Q6. Rename the table `faculty` to `teachers`.

**Answer:**

```sql
EXEC sp_rename 'faculty', 'teachers';
```


## Q7. Add a `DEFAULT` constraint so that `department = 'General'` in the `students` table.

**Answer:**

```sql
ALTER TABLE students
ADD CONSTRAINT default_dept
DEFAULT 'General' FOR department;
```


## Q8. Remove the column `phone_number` from the `students` table.

**Answer:**

```sql
ALTER TABLE students
DROP COLUMN phone_number;
```


## Q9. Remove all records from the `teachers` table without deleting its structure.

**Answer:**

```sql
TRUNCATE TABLE teachers;
```


## Q10. Delete the `teachers` table permanently.

**Answer:**

```sql
DROP TABLE teachers;
```

***

# Test-2 (T-SQL Level 2)

* Multiple tables
* `PRIMARY KEY`, `FOREIGN KEY`
* `UNIQUE`, `CHECK`, `DEFAULT`, `NOT NULL`
* Composite constraints
* Several `ALTER TABLE` operations
* `RENAME`, `TRUNCATE`, `DROP`
* Relationships between tables
* Slightly less direct instructions

## Q1. Create a database named `companyDB` and select/use that database.

**Answer:**

```sql
CREATE DATABASE companyDB;
USE companyDB;
```


## Q2. Create table `employees` with the following columns:

| Column     | Data Type     | Constraint      |
| ---------- | ------------- | --------------- |
| emp_id     | INT           | PRIMARY KEY     |
| emp_name   | VARCHAR(50)   | NOT NULL        |
| email      | VARCHAR(50)   | UNIQUE          |
| age        | INT           | CHECK(age >=18) |
| salary     | DECIMAL(10,2) | DEFAULT 25000   |
| department | VARCHAR(30)   |                 |

**Answer:**

```sql
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50) NOT NULL,
    email VARCHAR(50) UNIQUE,
    age INT CHECK(age >= 18),
    salary DECIMAL(10,2) DEFAULT 25000,
    department VARCHAR(30)
);
```


## Q3. Create table `departments` with suitable data types.

| Column    | Constraint  |
| --------- | ----------- |
| dept_id   | PRIMARY KEY |
| dept_name | UNIQUE      |
| location  | NOT NULL    |

**Answer:**

```sql
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50) UNIQUE,
    location VARCHAR(50) NOT NULL
);
```

## Q4. Modify `employees` table by adding `dept_id` and create a foreign key relationship with `departments`.

**Answer:**

```sql
ALTER TABLE employees
ADD dept_id INT;

ALTER TABLE employees
ADD CONSTRAINT FK_employees_departments
FOREIGN KEY (dept_id)
REFERENCES departments(dept_id);
```


## Q5. Create table `projects` with the following requirements:

* project_id → PRIMARY KEY
* project_name → NOT NULL
* budget → CHECK(budget > 50000)
* start_date → DATE
* dept_id → FOREIGN KEY

**Answer:**

```sql
CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    budget DECIMAL(12,2) CHECK (budget > 50000),
    start_date DATE,
    dept_id INT,
    
    CONSTRAINT FK_projects_departments
    FOREIGN KEY (dept_id)
    REFERENCES departments(dept_id)
);
```


## Q6. Perform the following ALTER TABLE operations on `employees`:

1. Add column `joining_date DATE`
2. Modify `department VARCHAR(50)`
3. Drop column `joining_date`

**Answer:**

```sql
ALTER TABLE employees
ADD joining_date DATE;

ALTER TABLE employees
ALTER COLUMN department VARCHAR(50);

ALTER TABLE employees
DROP COLUMN joining_date;
```


## Q7. Rename:

* `projects → company_projects`
* `employees → staff`

**Answer:**

```sql
EXEC sp_rename 'projects', 'company_projects';

EXEC sp_rename 'employees', 'staff';
```


## Q8. Set `location = 'Mumbai'` as default in `departments` table.

**Answer:**

```sql
ALTER TABLE departments
ADD CONSTRAINT default_location
DEFAULT 'Mumbai' FOR location;
```


## Q9. Create table `attendance` with:

| Column          | Constraint                           |
| --------------- | ------------------------------------ |
| emp_id          | FOREIGN KEY                          |
| attendance_date | DATE                                 |
| status          | CHECK(status IN('Present','Absent')) |

Create a composite primary key using:

```text
(emp_id, attendance_date)
```

**Answer:**

```sql
CREATE TABLE attendance (
    emp_id INT,
    attendance_date DATE,
    status VARCHAR(10)
        CHECK(status IN ('Present','Absent')),

    CONSTRAINT PK_attendance
    PRIMARY KEY (emp_id, attendance_date),

    CONSTRAINT FK_attendance_staff
    FOREIGN KEY (emp_id)
    REFERENCES staff(emp_id)
);
```

## Q10. Perform the following operations:

1. Truncate `company_projects`
2. Drop `attendance`
3. Drop `company_projects`

**Answer:**

```sql
TRUNCATE TABLE company_projects;

DROP TABLE attendance;

DROP TABLE company_projects;
```

***

For **Level 3**, the task shifts from “write syntax” to **designing a schema under business constraints**. This resembles screening rounds for data engineering, database developer, or backend roles where candidates must model entities, enforce integrity, and evolve schemas.

# SQL Practical Test (DDL Only) — Level 3

### Scenario: Digital Banking System Database Design

**Company Context:** Large bank building a core banking platform
**Focus:** Schema design, constraints, relationships, integrity
**Total Marks: 50
Time: 60 minutes**

---

## Business Requirements

The bank needs a database to manage:

* Customers
* Bank Accounts
* Branches
* Loans
* Transactions
* Employees

Rules:

1. A customer can have multiple accounts.
2. Every account belongs to one branch.
3. Transactions occur on accounts.
4. Loans are assigned to customers.
5. Employees work at branches.
6. Balance cannot be negative.
7. Loan amount must exceed ₹10,000.
8. Transaction type only:

   * Deposit
   * Withdrawal
   * Transfer

Design database structures accordingly.

---

# Q1. Create Database (2 Marks)

Create database:

```text
BankingSystemDB
```

Use the database.

**Marks: 2**

---

# Q2. Create Branch Table (5 Marks)

Create:

```text
branches
```

Requirements:

| Column      | Constraint           |
| ----------- | -------------------- |
| branch_id   | PRIMARY KEY          |
| branch_name | UNIQUE               |
| city        | NOT NULL             |
| IFSC_code   | UNIQUE               |
| created_at  | DEFAULT current date |

Choose suitable data types.

**Marks: 5**

---

# Q3. Create Customer Table (6 Marks)

Create:

```text
customers
```

Requirements:

* customer_id → Primary Key
* full_name → NOT NULL
* email → UNIQUE
* phone → UNIQUE
* dob → DATE
* created_at → Default timestamp

**Marks: 6**

---

# Q4. Create Accounts Table (8 Marks)

Create:

```text
accounts
```

Requirements:

| Column       | Constraint              |
| ------------ | ----------------------- |
| account_no   | PRIMARY KEY             |
| customer_id  | FOREIGN KEY             |
| branch_id    | FOREIGN KEY             |
| account_type | CHECK(Savings, Current) |
| balance      | CHECK(balance >=0)      |
| status       | DEFAULT 'Active'        |

**Marks: 8**

---

# Q5. Create Transactions Table (8 Marks)

Create:

```text
transactions
```

Requirements:

* transaction_id → PK
* account_no → FK
* transaction_type

Allowed values:

```text
Deposit
Withdrawal
Transfer
```

* amount > 0
* transaction_date default current timestamp

Apply all constraints.

**Marks: 8**

---

# Q6. Create Loans Table (6 Marks)

Requirements:

Create:

```text
loans
```

Rules:

* loan_id → PK
* customer_id → FK
* amount > 10000
* interest_rate between 5 and 20
* issue_date

**Marks: 6**

---

# Q7. Create Employees Table (5 Marks)

Requirements:

Each employee works in one branch.

Fields:

* emp_id
* emp_name
* designation
* salary > 20000
* branch_id FK

Apply constraints.

**Marks: 5**

---

# Q8. Schema Evolution Challenge (5 Marks)

Perform:

1. Add:

```text
aadhaar_no VARCHAR(12)
```

to customers.

2. Make it:

```text
UNIQUE
```

3. Add:

```text
email_verified BOOLEAN DEFAULT FALSE
```

4. Rename:

```text
employees → bank_employees
```

**Marks: 5**

---

# Q9. Composite Constraint Design (3 Marks)

Create:

```text
account_access
```

Requirements:

Store:

```text
customer_id
account_no
permission_type
```

Create a **composite primary key** using:

```text
(customer_id, account_no)
```

**Marks: 3**

---

# Q10. Maintenance Operations (2 Marks)

Perform:

1. Truncate:

```text
transactions
```

2. Drop:

```text
account_access
```

**Marks: 2**

---

# Bonus Question (+5 Marks)

Implement **ON DELETE CASCADE** or **ON UPDATE CASCADE** where appropriate and justify why.

Example:

Deleting a customer should affect:

```text
accounts
loans
transactions
```

Explain your design choice.

---

## Evaluation Rubric (similar to screening)

| Skill                   | Weight |
| ----------------------- | ------ |
| Correct syntax          | 20%    |
| Constraint design       | 25%    |
| Relationship modeling   | 25%    |
| Schema evolution        | 15%    |
| Data integrity thinking | 15%    |

---

This is closer to **entry-level data engineering / backend SQL screening**. Higher levels (L4–L5) introduce **multi-tenant architectures, audit tables, partitioning strategy, indexing assumptions, temporal tables, and regulatory constraints**.


***


