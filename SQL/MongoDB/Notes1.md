# 📘 MongoDB CLI Notes

## 🔹 Basic CLI Commands

```bash
net start MongoDB     # Start MongoDB service
net stop MongoDB      # Stop MongoDB service
Ctrl + L              # Clear terminal
```

---

## 🔹 Database Operations

```js
show dbs                      // List all databases
use <database_name>           // Create (if not exists) & switch to database

// Delete database
use <database_name>
db.dropDatabase()
```

---

## 🔹 Collections

```js
show collections              // List all collections in current DB
```

* A **collection** in MongoDB is similar to a table in relational databases.
* A **document** (record) is a JSON-like object:

```js
{ name: "Ankit", age: 13 }
```

---

## 🔹 CRUD Operations Overview

| Operation | Methods                                       |
| --------- | --------------------------------------------- |
| Create    | `insertOne()`, `insertMany()`                 |
| Read      | `find()`, `findOne()`                         |
| Update    | `updateOne()`, `updateMany()`, `replaceOne()` |
| Delete    | `deleteOne()`, `deleteMany()`                 |

---

# 🔹 CREATE

```js
use students

db.students.insertOne({ name: "Ankit", age: 13 })

db.students.insertMany([
  { name: "Vijay", age: 23 },
  { name: "Nitin", age: 34 }
])
```

---

# 🔹 READ

## Basic Queries

```js
db.students.find()                  // Returns first 20 documents
db.students.find({ age: 11 })       // Filter documents
db.students.findOne({ age: 11 })    // Returns first matching document
```

### Example Output

```js
db.students.find({ name: "Tunnu" })
[
  { _id: ObjectId("..."), name: "Tunnu", age: 11 }
]

db.students.findOne({ name: "Tunnu" })
{ _id: ObjectId("..."), name: "Tunnu", age: 11 }
```

---

## 🔹 Cursor in MongoDB

* `find()` returns a **cursor** (a pointer to result set).
* Used to iterate over documents efficiently.

### Cursor Usage

```js
db.students.find().count()                  // Count documents
db.students.find().limit(2)                // Limit results

db.students.find().forEach(doc => printjson(doc))   // Iterate documents
db.students.find().toArray()               // Convert cursor to array
```

---

## 🔹 Query Operators

```js
db.students.find({ age: 12 })

db.students.find({
  age: { $gte: 10, $lte: 15 }   // Range query
})
```

---

# 🔹 UPDATE

> Syntax:

```js
db.collection.updateOne(filter, update, options)
```

### Examples

```js
use students

db.students.updateOne(
  { name: "Vijay" },
  { $set: { age: 15 } }
)

db.students.updateMany(
  { age: 15 },
  { $set: { age: 13 } }
)

db.students.updateMany(
  { age: 13 },
  { $set: { isEligible: false } }
)

db.students.updateMany(
  { age: { $gt: 15 } },
  { $set: { isEligible: true } }
)
```

---

# 🔹 DELETE

```js
db.students.deleteOne({ name: "Ankit" })

db.students.deleteMany({ age: { $lt: 12 } })
```

---

# 🔹 Key Notes

* MongoDB stores data in **JSON-like documents (BSON)**.
* `_id` is a **unique identifier** automatically added to each document.
* `find()` returns a **cursor**, not direct data.
* Use `$set` to update specific fields without replacing the whole document.

---


