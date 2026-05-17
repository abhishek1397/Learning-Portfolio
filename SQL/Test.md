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

