# Lecture - 1 Creating, altering and dropping a database

## Creating a database

- In SSMS (graphical):  
  1) Right‑click **Databases** in Object Explorer  
  2) Click **New Database**  
  3) Enter database name → **OK**.  
- Using a query:  
  `CREATE DATABASE DatabaseName;`  

## Files created with a database

- When a database is created, 2 files are generated:  
  - **.MDF** – Data file that stores the actual data.  
  - **.LDF** – Transaction log file used to recover the database.  

## Altering (renaming) a database

- Using `ALTER DATABASE`:  
  `ALTER DATABASE OldDatabaseName MODIFY NAME = NewDatabaseName;`  
- Using system stored procedure:  
  `EXEC sp_renameDB 'OldDatabaseName', 'NewDatabaseName';`  

## Dropping a database

- Basic command:  
  `DROP DATABASE DatabaseThatYouWantToDrop;`  
- Dropping a database deletes its associated MDF and LDF files.  

## Dropping a database in use

- If the database is in use, `DROP DATABASE` fails with an error like:  
  `Cannot drop database "DatabaseName" because it is currently in use.`  
- To force drop, first set it to single user mode and rollback active work:  
  `ALTER DATABASE DatabaseName SET SINGLE_USER WITH ROLLBACK IMMEDIATE;`  
- `WITH ROLLBACK IMMEDIATE` rolls back all incomplete transactions and closes existing connections, after which you can safely run `DROP DATABASE`.  
- System databases (like `master`, `model`, `msdb`, `tempdb`) **cannot** be dropped.


## Summary table of graphical vs T‑SQL

| Operation | Graphical (SSMS) steps | T‑SQL command |
| --- | --- | --- |
| Create database | Right‑click **Databases** → **New Database** → enter name → **OK**  | `CREATE DATABASE DatabaseName;`  |
| Rename database | Right‑click database → **Rename** → type new name → Enter ] | `ALTER DATABASE OldDatabaseName MODIFY NAME = NewDatabaseName;` **or** `EXEC sp_renameDB 'OldDatabaseName','NewDatabaseName';`  |
| Drop database (not in use) | Right‑click database → **Delete** → **OK**  | `DROP DATABASE DatabaseName;`  |
| Prepare busy database for drop | (Delete dialog → option to close existing connections)  | `ALTER DATABASE DatabaseName SET SINGLE_USER WITH ROLLBACK IMMEDIATE;` then `DROP DATABASE DatabaseName;`  |


---

# Lecture 2  Creating and Working with tables

The aim is to create **tblPerson** and **tblGender** tables and enforce primary and foreign key constraints.

## Creating tables

- Tables in SQL Server can be created either graphically in SSMS or using T‑SQL queries.
- To create `tblPerson` graphically in SSMS:  
  - Right‑click **Tables** in Object Explorer → **New Table** → define Column Name, Data Type, Allow Nulls and save as `tblPerson`.

<img width="512" height="281" alt="image" src="https://github.com/user-attachments/assets/e462fb3d-6d1c-4524-8a1c-54ef2dc44ccd" />

## Creating tblGender with primary key

- `tblGender` is created using T‑SQL with an ID primary key and a Gender column:
  ```sql
  CREATE TABLE tblGender(
      ID INT NOT NULL PRIMARY KEY,
      Gender NVARCHAR(50)
  );
  ```
- The **primary key** uniquely identifies each row and does not allow null values.

## Foreign key in tblPerson

- In `tblPerson`, `GenderID` is a **foreign key** referencing the `ID` column of `tblGender`.
- A foreign key links one table to another and is used to enforce database integrity.

## Adding foreign key graphically

- Steps in SSMS to add the foreign key on `tblPerson.GenderID`:
  - Right‑click `tblPerson` → **Design**.  
  - Right‑click **GenderId** column → **Relationships**.  
  - In **Foreign Key Relationships** dialog, click **Add**.  
  - Expand **Tables and Column Specification** (click the +).  
  - Click the ellipsis (…) in that row.  
  - Choose `tblGender` as **Primary key table** and `ID` as its column.  
  - Choose `GenderId` as the foreign key column on the right.  
  - Click **OK**, close the dialog, then save the table.

  <img width="531" height="193" alt="image" src="https://github.com/user-attachments/assets/5e45fb6e-c5d7-47a8-bf3a-24b8c44268ce" />


## Adding foreign key using T‑SQL

- To add the foreign key on an existing `tblPerson` table:
  ```sql
  ALTER TABLE tblPerson
  ADD CONSTRAINT tblPerson_GenderId_FK
      FOREIGN KEY (GenderId) REFERENCES tblGender(ID);
  ```
- General pattern:[4][1]
  ```sql
  ALTER TABLE ForeignKeyTable
  ADD CONSTRAINT ForeignKeyTable_ForeignKeyColumn_FK
      FOREIGN KEY (ForeignKeyColumn)
      REFERENCES PrimaryKeyTable(PrimaryKeyColumn);
  ```

## Role of foreign keys

- A foreign key in one table points to the primary key of another table, ensuring only valid, existing values are stored in the foreign key column.
- The foreign key constraint prevents inserting values into the foreign key column that do not exist in the referenced primary key table, thus maintaining referential integrity.

---

# Lecture 3 Default constraint in sql server

Default constraints insert a default value into a column when no value is specified during INSERT (including NULL).

## Adding default constraint to existing column

- General syntax:  
  ```sql
  ALTER TABLE {TABLE_NAME}
  ADD CONSTRAINT {CONSTRAINT_NAME}
  DEFAULT {DEFAULT_VALUE} FOR {EXISTING_COLUMN_NAME};
  ```

- Example on `tblPerson`:  
  ```sql
  ALTER TABLE tblPerson
  ADD CONSTRAINT DF_tblPerson_GenderId
  DEFAULT 1 FOR GenderId;
  ```

## Adding new column with default constraint

- General syntax:  
  ```sql
  ALTER TABLE {TABLE_NAME}
  ADD {COLUMN_NAME} {DATA_TYPE} {NULL | NOT NULL}
  CONSTRAINT {CONSTRAINT_NAME} DEFAULT {DEFAULT_VALUE};
  ```

## INSERT behavior with default constraint

| INSERT statement | GenderId result | Explanation |
|------------------|-----------------|-------------|
| `INSERT INTO tblPerson(ID,Name,Email) VALUES(5,'Sam','s@s.com')` | 1 | No GenderId specified → uses default value 1 |
| `INSERT INTO tblPerson(ID,Name,Email,GenderId) VALUES(6,'Dan','d@d.com',NULL)` | NULL | Explicit NULL overrides default constraint |

## Dropping a constraint

- Syntax:  
  ```sql
  ALTER TABLE {TABLE_NAME}
  DROP CONSTRAINT {CONSTRAINT_NAME};
  ```

## Summary table: Default constraint commands

| Operation | T-SQL Command |
|-----------|---------------|
| Add default to existing column | `ALTER TABLE tblPerson ADD CONSTRAINT DF_tblPerson_GenderId DEFAULT 1 FOR GenderId;` |
| Add new column with default | `ALTER TABLE tblPerson ADD EmailStatus VARCHAR(10) NOT NULL CONSTRAINT DF_EmailStatus DEFAULT 'Active';` |
| Drop constraint | `ALTER TABLE tblPerson DROP CONSTRAINT DF_tblPerson_GenderId;` |

---

# Lecture 4 Cascading referential integrity constraint

Cascading referential integrity controls what happens to related rows when a referenced key is updated or deleted.

## Core idea

- Two tables: parent (with primary key) and child (with foreign key pointing to that key).  
- If a key in the parent is changed or deleted, SQL Server can: block it, propagate it, or replace it with NULL/default in the child.

## Default behavior: No Action

- **No Action** (or RESTRICT) is the default.  
- When trying to `DELETE` or `UPDATE` a parent row that is referenced by child rows, SQL Server raises an error and rolls back the statement.  

## CASCADE

- **CASCADE** propagates the change to child rows.  
- On `DELETE`: all child rows with matching foreign key values are also deleted.  
- On `UPDATE`: all child foreign key values are updated to the new parent key value.  

## SET NULL

- **SET NULL** replaces the foreign key value in the child rows with `NULL`.  
- On `DELETE` or `UPDATE` of the parent row, all referencing child rows get their foreign key column set to `NULL` (column must allow NULL).  

## SET DEFAULT

- **SET DEFAULT** replaces the foreign key value in the child rows with the column’s default value.  
- On `DELETE` or `UPDATE` of the parent row, all referencing child rows get their foreign key column set to its defined default (column must have a default defined).

---

# Lecture 5 **CHECK Constraint in SQL Server**

A **CHECK constraint** is used to **limit the range of values** that can be entered into a column.
It enforces **data integrity** by allowing only values that satisfy a specified condition.
  * **Constraint** is just **boolean expression** returning: **True** or **False**

### Example Scenario

Assume we have a table `tblPerson` with an integer column `Age`.

Business rules:

* Age **cannot be less than 0**
* Age **cannot be greater than 150**

Since `Age` is an `INT`, SQL Server would normally allow negative values or very large numbers.
To restrict this, we use a **CHECK constraint**.

### CHECK Constraint in SSMS 

1. Open **SSMS** and connect to the database.
2. Expand **Tables**, right-click the target table, select **Design**.
3. Right-click inside Table Designer → **Check Constraints…**
4. Click **Add** to create a new constraint.
5. Enter the condition in **Expression** (e.g., `Age > 0 AND Age < 150`).
6. (Optional) Rename the constraint for clarity.
7. Ensure enforcement options are **Yes** (existing data, inserts, updates).
8. **Save** the table.

**Outcome:** The database enforces the rule and blocks invalid inserts or updates.

> **Note**
> If a table column already contains invalid entries, the constraint will fail to apply.  
> Delete the invalid entries first.

### Creating a CHECK Constraint

```sql
ALTER TABLE tblPerson
ADD CONSTRAINT CK_tblPerson_Age
CHECK (Age >= 0 AND Age <= 150);
```

✅ This ensures:

* Only values between **0 and 150 (inclusive)** are allowed.


### General Syntax for CHECK Constraint

```sql
ALTER TABLE {TABLE_NAME}
ADD CONSTRAINT {CONSTRAINT_NAME}
CHECK (BOOLEAN_EXPRESSION);
```

* If the **BOOLEAN_EXPRESSION evaluates to TRUE**, the value is allowed.
* If it evaluates to **FALSE**, the insert or update fails.


### CHECK Constraint and NULL Values

If the `Age` column is **nullable**:

* `NULL` values are allowed.
* When `NULL` is checked, the expression evaluates to **UNKNOWN**.
* SQL Server **allows UNKNOWN**, so the row is inserted successfully.

Example:

```sql
INSERT INTO tblPerson (Age) VALUES (NULL);
```

✔ Allowed (unless the column is defined as `NOT NULL`).


### Dropping a CHECK Constraint

```sql
ALTER TABLE tblPerson
DROP CONSTRAINT CK_tblPerson_Age;
```


### **Summary Table: CHECK Constraint Commands**

| **Operation**             | **SQL Command**                                                                 | **Purpose**                                   |
|----------------------------|----------------------------------------------------------------------------------|-----------------------------------------------|
| Create CHECK constraint    | `ALTER TABLE tblPerson ADD CONSTRAINT CK_tblPerson_Age CHECK (Age > 0 AND Age < 150);` | Restricts AGE between 0 and 150               |
| Syntax format (generic)    | `ALTER TABLE {TABLE_NAME} ADD CONSTRAINT {CONSTRAINT_NAME} CHECK ({BOOLEAN_EXPRESSION});` | Generic form for CHECK constraint creation    |
| Allow NULL values behavior | `NULL` values pass the constraint as condition evaluates to `UNKNOWN`            | Shows how SQL Server handles NULL under CHECK |
| Drop CHECK constraint      | `ALTER TABLE tblPerson DROP CONSTRAINT CK_tblPerson_Age;`                        | Removes the existing CHECK constraint         |

***

# Lecture 6  **Identity Column in SQL Server**

An **IDENTITY column** in SQL Server is used to **automatically generate unique numeric values** for a column when new rows are inserted into a table.
This is commonly used for **primary key columns**.


### Creating a Table with an Identity Column

```sql
CREATE TABLE tblPerson
(
    PersonId INT IDENTITY(1,1) PRIMARY KEY,
    Name NVARCHAR(20)
);
```

* `IDENTITY(1,1)`

  * **Seed** = 1 (starting value)
  * **Increment** = 1 (increase by 1)
* Seed and increment values are **optional**
* If not specified, both default to **1**


### Inserting Data into an Identity Column Table

Since `PersonId` is an identity column, **we do not supply its value explicitly**.

```sql
INSERT INTO tblPerson VALUES ('Sam');
INSERT INTO tblPerson VALUES ('Sara');
```

Result:

* Sam → `PersonId = 1`
* Sara → `PersonId = 2`

SQL Server automatically generates the values.



### Explicitly Inserting into an Identity Column (Error Case)

```sql
INSERT INTO tblPerson VALUES (1, 'Todd');
```

❌ Error:

> An explicit value for the identity column can only be specified when a column list is used and IDENTITY_INSERT is ON.

By default, SQL Server **does not allow explicit values** for identity columns.


### Correct Way (Let SQL Server Generate the Value)

```sql
INSERT INTO tblPerson VALUES ('Todd');
```

SQL Server assigns the next available identity value automatically.


### Identity Gaps Explained

If you:

1. Insert a row
2. Delete it
3. Insert another row

SQL Server **does not reuse identity values**.

Example:

* Insert → `PersonId = 2`
* Delete row
* Next insert → `PersonId = 3`

Even though `PersonId = 2` no longer exists, SQL Server skips it.



### Filling Identity Gaps (Explicit Insert)

To explicitly insert a value into an identity column:

#### Step 1: Turn ON `IDENTITY_INSERT`

```sql
SET IDENTITY_INSERT tblPerson ON;
```

#### Step 2: Specify Column List and Value

```sql
INSERT INTO tblPerson (PersonId, Name)
VALUES (2, 'John');
```

⚠️ While `IDENTITY_INSERT` is ON:

* You **must provide** a value for the identity column
* Only **one table per session** can have `IDENTITY_INSERT` ON



### Turn OFF `IDENTITY_INSERT`

After filling the gaps:

```sql
SET IDENTITY_INSERT tblPerson OFF;
```

SQL Server resumes automatic identity value generation.


### Resetting Identity Values Using DBCC CHECKIDENT

If **all rows are deleted** and you want to reset the identity value:

```sql
DBCC CHECKIDENT (tblPerson, RESEED, 0);
```

* The next inserted row will get `PersonId = 1`
* Reseeding to `0` means the next identity value starts from `1`


## Summary Table – Commands Used

| Purpose                           | SQL Command                                                                           |
| --------------------------------- | ------------------------------------------------------------------------------------- |
| Create table with identity column | `CREATE TABLE tblPerson (PersonId INT IDENTITY(1,1) PRIMARY KEY, Name NVARCHAR(20));` |
| Insert without identity value     | `INSERT INTO tblPerson VALUES ('Sam');`                                               |
| Explicit insert error example     | `INSERT INTO tblPerson VALUES (1, 'Todd');`                                           |
| Turn ON identity insert           | `SET IDENTITY_INSERT tblPerson ON;`                                                   |
| Insert explicit identity value    | `INSERT INTO tblPerson (PersonId, Name) VALUES (2, 'John');`                          |
| Turn OFF identity insert          | `SET IDENTITY_INSERT tblPerson OFF;`                                                  |
| Reset identity column             | `DBCC CHECKIDENT (tblPerson, RESEED, 0);`                                             |

---

# Lecture 7  How to Get the Last Generated Identity Column Value in SQL Server 


In previous sections, we learned that **identity column values are automatically generated** by SQL Server.
Often, after inserting a row, we need to **retrieve the identity value** that was just created.

SQL Server provides **three main ways** to get the last generated identity value:

1. `SCOPE_IDENTITY()`
2. `@@IDENTITY`
3. `IDENT_CURRENT('TableName')`



### Example Queries

```sql
SELECT SCOPE_IDENTITY();
SELECT @@IDENTITY;
SELECT IDENT_CURRENT('tblPerson');
```

Although these functions look similar, they behave **very differently**.


## Understanding the Differences

### 1. SCOPE_IDENTITY()

* Returns the **last identity value**
* Generated in the **same session (connection)**
* Generated in the **same scope**
  (same stored procedure, function, or batch)

✅ This is the **recommended and safest** way to get the last identity value.


### 2. @@IDENTITY

* Returns the **last identity value**
* Generated in the **same session**
* **Across any scope**

⚠️ This can return **unexpected values** if triggers are involved.



### 3. IDENT_CURRENT('TableName')

* Returns the **last identity value for a specific table**
* Across **any session**
* Across **any scope**

⚠️ Not safe for concurrent inserts because another user may insert a row at the same time.



## Trigger Example (Why Differences Matter)

Assume:

* `tblPerson1` has an identity column
* `tblPerson2` has an identity column
* A **trigger on tblPerson1** inserts a row into `tblPerson2`

When you insert into `tblPerson1`:

* `SCOPE_IDENTITY()` → identity value from **tblPerson1**
* `@@IDENTITY` → identity value from **tblPerson2** (trigger-generated)
* `IDENT_CURRENT('tblPerson1')` → last identity for tblPerson1 (any session)

This is why `@@IDENTITY` can be **dangerous** in real-world applications.



## In Brief

* **SCOPE_IDENTITY()**
  → Same session, same scope ✅ (Best choice)

* **@@IDENTITY**
  → Same session, all scopes ⚠️

* **IDENT_CURRENT('TableName')**
  → Any session, any scope ⚠️



## Summary Table – Commands Used

| Method         | SQL Command                          | Scope      | Session      | Recommended |
| -------------- | ------------------------------------ | ---------- | ------------ | ----------- |
| SCOPE_IDENTITY | `SELECT SCOPE_IDENTITY();`           | Same scope | Same session | ✅ Yes       |
| @@IDENTITY     | `SELECT @@IDENTITY;`                 | Any scope  | Same session | ❌ No        |
| IDENT_CURRENT  | `SELECT IDENT_CURRENT('tblPerson');` | Any scope  | Any session  | ❌ No        |

### Key Takeaways

* Always use **`SCOPE_IDENTITY()`** after INSERT statements
* Avoid **`@@IDENTITY`** when triggers exist
* `IDENT_CURRENT()` is useful for monitoring, not for inserts
* Correct identity retrieval prevents **data mismatch bugs**

---

# Lecture 8  Unique Key Constraint 

### What is a UNIQUE constraint?

* A **UNIQUE constraint** enforces **uniqueness** in a column.
* It **does not allow duplicate values** in the specified column.
* It can be applied:

  * Using **SQL Server Management Studio (SSMS) Designer**
  * Using a **SQL query**



### Adding a UNIQUE constraint using SSMS Designer

Steps:

1. Right-click the table → **Design**
2. Right-click the column → **Indexes/Keys…**
3. Click **Add**
4. In **Columns**, select the column to be unique
5. In **Type**, choose **Unique Key**
6. Click **Close** and **Save** the table



### Adding a UNIQUE constraint using SQL Query

```sql
ALTER TABLE Table_Name
ADD CONSTRAINT Constraint_Name UNIQUE (Column_Name);
```

```sql
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    CONSTRAINT UC_Person UNIQUE (ID,LastName)
);
```



### UNIQUE Key vs PRIMARY Key

Both constraints enforce **uniqueness**, but they are used differently.

#### When to use UNIQUE key instead of PRIMARY key?

* A table can have **only one PRIMARY KEY**
* A table can have **multiple UNIQUE keys**
* Use UNIQUE key when you want **uniqueness on additional columns**



### Differences between PRIMARY KEY and UNIQUE KEY

| Feature          | PRIMARY KEY              | UNIQUE KEY                     |
| ---------------- | ------------------------ | ------------------------------ |
| Number per table | Only one                 | More than one allowed          |
| Null values      | ❌ Not allowed            | ✅ One NULL allowed             |
| Purpose          | Main identifier of a row | Enforces additional uniqueness |



### Dropping a UNIQUE constraint

#### Method 1: Using SSMS

* Right-click the constraint → **Delete**

#### Method 2: Using SQL Query

```sql
ALTER TABLE tblPerson
DROP CONSTRAINT UQ_tblPerson_Email;
```


## Summary Table: Commands Used

| Purpose               | SQL Command                                                                  |
| --------------------- | ---------------------------------------------------------------------------- |
| Add UNIQUE constraint | `ALTER TABLE Table_Name ADD CONSTRAINT Constraint_Name UNIQUE (Column_Name)` |
| Drop constraint       | `ALTER TABLE Table_Name DROP CONSTRAINT Constraint_Name`                     |

---


# Lecture 9  **Select Statement** 


## SELECT Statement – Part 10 (Notes)

### What is a SELECT statement?

* The **SELECT** statement is used to **retrieve data** from a table.
* It specifies:

  * **Which columns** to fetch
  * **From which table**



### Basic SELECT Statement Syntax

```sql
SELECT Column_List
FROM Table_Name;
```

* `Column_List` → one or more column names separated by commas
* `Table_Name` → the table from which data is retrieved



### Selecting All Columns

* You can use `*` to select **all columns** from a table.

```sql
SELECT *
FROM Table_Name;
```



### Important Note on Performance ⚠️

* Although `SELECT *` is valid:

  * It retrieves **all columns**, even unnecessary ones
  * Can reduce **performance**, especially on large tables
* **Best practice:** Always specify the required columns explicitly

Example:

```sql
SELECT FirstName, LastName, Email
FROM Table_Name;
```



## Summary Table: SELECT Commands

| Purpose                 | SQL Command                          |
| ----------------------- | ------------------------------------ |
| Select specific columns | `SELECT Column_List FROM Table_Name` |
| Select all columns      | `SELECT * FROM Table_Name`           |
| Recommended approach    | Use column list instead of `*`       |

---

#  Lecture 10  **GROUP BY**

### Aggregate Functions in SQL Server

Aggregate functions perform calculations on multiple rows and return a **single summary value**.

Common aggregate functions:

1. `COUNT()`
2. `SUM()`
3. `AVG()`
4. `MIN()`
5. `MAX()`


### What is the GROUP BY clause?

* The **GROUP BY** clause groups rows that have the **same values** in one or more columns.
* It is **always used with aggregate functions**.
* It converts detailed rows into **summary rows**.

![Table](https://github.com/user-attachments/assets/3e4b3dcd-55a1-49a3-b276-9ef4bae01789)

### Example 1: Total Salaries by City

#### Requirement

Get the **total salary paid in each city**.

#### Query

```sql
SELECT City, SUM(Salary) AS TotalSalary
FROM tblEmployee
GROUP BY City;
```
![](https://github.com/user-attachments/assets/53b52b3b-f2c6-49fd-b489-d9c03b838280)

#### Explanation

* `SUM(Salary)` adds all salaries
* `GROUP BY City` groups employees belonging to the same city



### Important Note ⚠️

If you omit the `GROUP BY` clause, SQL Server throws an error:

> Column is invalid in the select list because it is not contained in either an aggregate function or the GROUP BY clause.



### Example 2: Total Salaries by City and Gender

#### Requirement

Get **total salaries** grouped by **City and Gender**.

#### Query

```sql
SELECT City, Gender, SUM(Salary) AS TotalSalary
FROM tblEmployee
GROUP BY City, Gender;
```

![](https://github.com/user-attachments/assets/ec93b911-c194-4418-a9c8-e00c9366aa22)

#### Key Point

* You can **group by multiple columns**
* Grouping happens first by `City`, then by `Gender`



### Example 3: Total Salaries and Employee Count by City and Gender

#### Requirement

Get:

* Total salaries
* Total number of employees
  Grouped by **City and Gender**

#### Query

```sql
SELECT City, Gender,
       SUM(Salary) AS TotalSalary,
       COUNT(ID) AS TotalEmployees
FROM tblEmployee
GROUP BY City, Gender;
```
![](https://github.com/user-attachments/assets/8d7a330f-3801-4ea1-8cb8-4b731313abd4)


## Filtering Data in GROUP BY Queries

### WHERE vs HAVING

| Clause | Filters | When applied       |
| ------ | ------- | ------------------ |
| WHERE  | Rows    | Before aggregation |
| HAVING | Groups  | After aggregation  |



### Filtering Rows using WHERE (Before Aggregation)

```sql
SELECT City, SUM(Salary) AS TotalSalary
FROM tblEmployee
WHERE City = 'London'
GROUP BY City;
```



### Filtering Groups using HAVING (After Aggregation)

```sql
SELECT City, SUM(Salary) AS TotalSalary
FROM tblEmployee
GROUP BY City
HAVING City = 'London';
```



### Performance Note 💡

* SQL Server optimizer chooses the most efficient execution plan
* **Best practice:**

  * Use `WHERE` to eliminate unnecessary rows **as early as possible**
  * Use `HAVING` only when filtering on aggregate results


## Summary Table: GROUP BY Commands

| Purpose                      | SQL Command            |
| ---------------------------- | ---------------------- |
| Group rows                   | `GROUP BY Column_Name` |
| Group by multiple columns    | `GROUP BY Col1, Col2`  |
| Aggregate sum                | `SUM(Column)`          |
| Count rows                   | `COUNT(Column)`        |
| Filter rows before grouping  | `WHERE condition`      |
| Filter groups after grouping | `HAVING condition`     |

---

# Lecture 11  Joins in SQL Server


### What are Joins?

* **Joins** are used to retrieve data from **two or more related tables**
* Tables are usually related using **foreign key constraints**
* Joins combine rows based on a **join condition**



### Types of Joins in SQL Server

1. **CROSS JOIN**
2. **INNER JOIN**
3. **OUTER JOIN**

   * LEFT JOIN (LEFT OUTER JOIN)
   * RIGHT JOIN (RIGHT OUTER JOIN)
   * FULL JOIN (FULL OUTER JOIN)



## Tables Used in Examples

### tblDepartment

* ID (Primary Key)
* DepartmentName
* Location
* DepartmentHead

![](https://github.com/user-attachments/assets/568be32d-07dd-4f5c-af16-6a0c6b0e6ba3)

### tblEmployee

* ID (Primary Key)
* Name
* Gender
* Salary
* DepartmentId (Foreign Key → tblDepartment.ID)

![](https://github.com/user-attachments/assets/dc8353cb-1300-4ea3-932c-339b0052bef3)


#### Create tblDepartment table

```sql
Create table tblDepartment  (
  ID int primary key,
  DepartmentName nvarchar(50),
  Location nvarchar(50),
  DepartmentHead nvarchar(50)   )
  Go

Insert into tblDepartment values (1, 'IT', 'London', 'Rick')
Insert into tblDepartment values (2, 'Payroll', 'Delhi', 'Ron')
Insert into tblDepartment values (3, 'HR', 'New York', 'Christie')
Insert into tblDepartment values (4, 'Other Department', 'Sydney', 'Cindrella')
Go
```

#### Create tblEmployee table

```sql
Create table tblEmployee (
  ID int primary key,
  Name nvarchar(50),
  Gender nvarchar(50),
  Salary int,
  DepartmentId int foreign key references tblDepartment(Id))
Go

Insert into tblEmployee values (1, 'Tom', 'Male', 4000, 1)
Insert into tblEmployee values (2, 'Pam', 'Female', 3000, 3)
Insert into tblEmployee values (3, 'John', 'Male', 3500, 1)
Insert into tblEmployee values (4, 'Sam', 'Male', 4500, 2)
Insert into tblEmployee values (5, 'Todd', 'Male', 2800, 2)
Insert into tblEmployee values (6, 'Ben', 'Male', 7000, 1)
Insert into tblEmployee values (7, 'Sara', 'Female', 4800, 3)
Insert into tblEmployee values (8, 'Valarie', 'Female', 5500, 1)
Insert into tblEmployee values (9, 'James', 'Male', 6500, NULL)
Insert into tblEmployee values (10, 'Russell', 'Male', 8800, NULL)

Go
```

## General Syntax for Joins

```sql
SELECT ColumnList
FROM LeftTable
JOIN_TYPE RightTable
ON JoinCondition;
```



## CROSS JOIN

### Description

* Produces a **Cartesian product**
* Each row from the first table is combined with **every row** from the second table
* **Does NOT use ON clause**

### Example

```sql
SELECT Name, Gender, Salary, DepartmentName
FROM tblEmployee
CROSS JOIN tblDepartment;
```

### Result

* If tblEmployee has **10 rows**
* And tblDepartment has **4 rows**
* Output = **40 rows**



## INNER JOIN (JOIN)

### Description

* Returns **only matching rows** from both tables
* Non-matching rows are **excluded**
* `JOIN` and `INNER JOIN` mean the same
* **Best practice:** Use `INNER JOIN` for clarity

### Example

```sql
SELECT Name, Gender, Salary, DepartmentName
FROM tblEmployee
INNER JOIN tblDepartment
ON tblEmployee.DepartmentId = tblDepartment.Id;
```

### Key Point

* Employees with `NULL` DepartmentId (e.g., James, Russell) are **excluded**
* Only **8 rows returned**

![](https://github.com/user-attachments/assets/0f18ef8b-3f8f-43c9-8468-7014a270eab3)


## LEFT JOIN (LEFT OUTER JOIN)

### Description

* Returns:

  * All matching rows
  * Plus **non-matching rows from the LEFT table**
* `OUTER` keyword is optional

### Example

```sql
SELECT Name, Gender, Salary, DepartmentName
FROM tblEmployee
LEFT JOIN tblDepartment
ON tblEmployee.DepartmentId = tblDepartment.Id;
```

### Key Point

* Includes **James and Russell**
* Missing department values appear as **NULL**

![](https://github.com/user-attachments/assets/7495baa0-17ce-485f-9fa6-a01be76d503c)


## RIGHT JOIN (RIGHT OUTER JOIN)

### Description

* Returns:

  * All matching rows
  * Plus **non-matching rows from the RIGHT table**
* `OUTER` keyword is optional

### Example

```sql
SELECT Name, Gender, Salary, DepartmentName
FROM tblEmployee
RIGHT JOIN tblDepartment
ON tblEmployee.DepartmentId = tblDepartment.Id;
```
![](https://github.com/user-attachments/assets/c539ee4d-e678-4206-84c6-666a9b596ca9)


## FULL JOIN (FULL OUTER JOIN)

### Description

* Returns **all rows from both tables**
* Includes:

  * Matching rows
  * Non-matching rows from both sides
* `OUTER` keyword is optional

### Example

```sql
SELECT Name, Gender, Salary, DepartmentName
FROM tblEmployee
FULL JOIN tblDepartment
ON tblEmployee.DepartmentId = tblDepartment.Id;
```

![](https://github.com/user-attachments/assets/7c0b8549-50dd-4984-af75-32e7443cd25e)



### Joins Summary Table

| Join Type  | Purpose                                                |
| ---------- | ------------------------------------------------------ |
| CROSS JOIN | Returns Cartesian product of both tables               |
| INNER JOIN | Returns only matching rows                             |
| LEFT JOIN  | All matching rows + non-matching rows from left table  |
| RIGHT JOIN | All matching rows + non-matching rows from right table |
| FULL JOIN  | All rows from both tables, including non-matching      |

![](https://github.com/user-attachments/assets/9243c629-e3f5-49df-85b3-134c6cb65ea1)

### Real-World Tip 💡

* **INNER JOIN** and **LEFT JOIN** are used most frequently
* Prefer **LEFT JOIN** when you don’t want to lose data from the main table

---

# Lecture 12

