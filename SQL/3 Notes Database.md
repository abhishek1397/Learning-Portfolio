# Lecture 1  DBMS syllabus + focus areas
 


### 1️⃣ What is DBMS & Why DBMS?

* **Database**: Organized collection of related data
* **DBMS**: Software to create, store, retrieve, update, and manage databases
* **Why DBMS over File System?**

  * Reduced data redundancy
  * Improved data consistency
  * Concurrent access support
  * Better security
  * Backup & recovery
    👉 *Very common theory question*


### 2️⃣ Data Models

Focus mainly on:

* **ER Model** → conceptual / high-level design
* **Relational Model** → tables, rows, columns



### 3️⃣ ER Model (Conceptual Design)

Used before converting data into tables.

**Key components**

* **Entity / Entity Set**
* **Attributes**

  * Simple vs Composite
  * Single-valued vs Multi-valued
  * Derived
* **Relationships**

  * Degree (binary, ternary, etc.)
  * Cardinality (1:1, 1:N, M:N)
  * Participation (total / partial)

👉 Exams often ask **ER → Relational mapping**


### 4️⃣ Keys & Integrity Constraints

**Types of Keys**

* **Super Key**: Uniquely identifies a tuple
* **Candidate Key**: Minimal super key
* **Primary Key**: Chosen candidate key
* **Alternate Key**: Remaining candidate keys
* **Foreign Key**: References PK of another table

**Integrity Constraints**

* Entity Integrity → PK cannot be NULL
* Referential Integrity → FK must match PK or be NULL

### 5️⃣ Normalization

Goal: **Remove redundancy & anomalies**

**Based on Functional Dependencies**

* **1NF**: No multi-valued or repeating attributes
* **2NF**: No partial dependency (composite key case)
* **3NF**: No transitive dependency
* **BCNF**: Every determinant is a candidate key

⭐ Important exam topics:

* Lossless join decomposition
* Dependency preservation

### 6️⃣ Transactions & Concurrency

**Transaction**: Logical unit of work

**ACID Properties**

* Atomicity
* Consistency
* Isolation
* Durability

**Concurrency Control**

* Schedules: serial, non-serial
* Serializability: conflict & view
* Locking (2PL)
* Deadlock & its handling

### 7️⃣ Relational Algebra & SQL

#### Relational Algebra (GATE favorite)

* Selection (σ)
* Projection (π)
* Union, Difference
* Cartesian product
* Join
* Division

#### SQL

* **DDL**: CREATE, ALTER, DROP
* **DML**: SELECT, INSERT, UPDATE, DELETE
* **DCL**: GRANT, REVOKE
* **TCL**: COMMIT, ROLLBACK
* Joins, Subqueries, GROUP BY, HAVING

### 8️⃣ Indexing & File Organization

Purpose: **Fast data retrieval**

* Primary vs Secondary index
* Dense vs Sparse index
* Single-level vs Multi-level indexing
* **B+ Tree** (conceptual understanding enough for Lecture 1)

---

