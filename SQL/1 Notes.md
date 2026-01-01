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

# Lecture 5 Cascading referential integrity constraint

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

