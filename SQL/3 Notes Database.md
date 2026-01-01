# Lecture 1

DBMS Lec-1 video mainly outlines the complete DBMS syllabus and the major topic buckets you must cover.

## Overall DBMS Syllabus

- DBMS basic concepts: data, information, database, DBMS, advantages over file system.[1]
- Data models: especially Entity–Relationship (ER) model and Relational model.[1]
- Relational Algebra and SQL (DDL, DML, DCL, TCL) including queries for GATE/NET level.[1]
- Keys and constraints: primary, candidate, super, foreign key, and various integrity constraints.[1]
- Normalization: 1NF, 2NF, 3NF, BCNF (and sometimes higher forms) with decomposition.[1]
- Transaction management: ACID properties, schedule types, concurrency control, locking, deadlock.[1]
- Indexing and file organization concepts for performance.[1]


## Basic DBMS Intro (What & Why)

- Database: organized collection of related data; DBMS: software to create, store, retrieve, and manage databases.[1]
- Focus in exams: why DBMS is preferred over traditional file systems (less redundancy, better consistency, concurrent access, security, backup & recovery).[1]


## ER Model (High-Level Design)

- ER model is used for conceptual design of a database before converting to tables.[1]
- Core elements to study:
  - Entity and entity set  
  - Attributes (simple, composite, single/multi-valued, derived)  
  - Relationships (degree, cardinality) and participation  
  - ER diagrams and their mapping to relational schema  

## Keys and Constraints

- Key topics highlighted:
  - Super key: any attribute set that uniquely identifies a tuple.  
  - Candidate key: minimal super key.[1]
  - Primary key: chosen candidate key to uniquely identify tuples.[1]
  - Alternate key: remaining candidate keys.  
  - Foreign key: attribute that refers to primary key of another relation.  
- Also remember: entity integrity and referential integrity constraints for exams.[1]

## Normalization (Schema Refinement)

- Purpose: remove redundancy, avoid update anomalies, and improve consistency.[1]
- Syllabus focus:
  - Functional dependency basics  
  - 1NF: remove multi-valued/ repeating groups  
  - 2NF: remove partial dependency (w.r.t. composite key)  
  - 3NF: remove transitive dependency  
  - BCNF: every determinant is a candidate key  
- Also note: lossless-join and dependency-preserving decompositions are common exam questions.[1]

## Transactions & Concurrency Control

- Transaction: logical unit of work; ACID properties (Atomicity, Consistency, Isolation, Durability).[1]
- Concurrency topics to prepare:
  - Schedules: serial, non-serial, conflict/ view serializable  
  - Concurrency control: locking (2PL), timestamp ordering, deadlock and its handling  
  - Recovery basics: log-based recovery, checkpoint idea (usually overview level in first lecture)  

## SQL and Relational Algebra

- Two major query formalisms in syllabus:[1]
  - Relational Algebra: selection, projection, union, set-difference, Cartesian product, rename, joins, division (classic GATE area).  
  - SQL:
    - DDL: CREATE, ALTER, DROP  
    - DML: SELECT, INSERT, UPDATE, DELETE  
    - Constraints with CREATE TABLE  
    - Joins, subqueries, aggregation, GROUP BY, HAVING  
    - Basic view of DCL/TCL (GRANT, REVOKE, COMMIT, ROLLBACK)  

## Indexing and File Organization

- Need: speed up data retrieval and support efficient query processing.[1]
- Coverage expected:
  - Primary vs secondary index  
  - Dense vs sparse index  
  - Single-level vs multi-level indexing  
  - Basic idea of B+ tree indexing (at least conceptual).  

[1](https://www.youtube.com/watch?v=kBdlM6hNDAE)
