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
