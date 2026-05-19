# Apache Spark RDD Notes (Scala)

---

# 1. What is RDD?

**RDD = Resilient Distributed Dataset**

RDD is the fundamental data structure in Apache Spark used for distributed and parallel processing.

Meaning:

```text
Resilient
→ Can recover lost data automatically

Distributed
→ Data stored across multiple machines/nodes

Dataset
→ Collection of records
```

Definition:

> RDD is an immutable, distributed collection of elements processed in parallel.

---

# 2. Core Properties of RDD

## (1) Immutable

RDD cannot be modified after creation.

Example:

```scala
val rdd1 = sc.parallelize(Array(1,2,3))

val rdd2 =
rdd1.map(x=>x*2)
```

New RDD created:

```text
rdd1 → unchanged

rdd2 → transformed
```

---

## (2) Distributed

Data divided into partitions.

Example:

```text
Node1 → [1,2]

Node2 → [3,4]

Node3 → [5,6]
```

---

## (3) Fault Tolerant

Lost partition recovered using **lineage**.

Example:

```text
RDD1

↓

map()

↓

RDD2

↓

filter()

↓

RDD3
```

If RDD3 lost:

Spark recreates using lineage.

---

## (4) Lazy Evaluation

Transformations execute only after action.

Example:

```scala
val x =
sc.parallelize(1 to 5)

val y =
x.map(_*2)
```

Nothing executes yet.

Execution starts:

```scala
y.collect()
```

---

## (5) Parallel Processing

Multiple tasks execute simultaneously.

---

# 3. Ways to Create RDD

---

## Method 1: Using parallelize()

Create RDD from collection.

Example:

```scala
val r1 =
spark.sparkContext.parallelize(

Seq(

("A",1),

("B",2),

("C",3)

)

)
```

Display:

```scala
r1.collect()
.foreach(println)
```

Output:

```text
(A,1)

(B,2)

(C,3)
```

Use:

Data already in memory.

---

## Method 2: Using textFile()

Load file.

Example:

File:

```text
101,B,2500

102,A,2600

103,C,2700
```

Code:

```scala
val r2 =

spark.sparkContext
.textFile("D:\\data.txt")
```

Display:

```scala
r2.collect()
.foreach(println)
```

Output:

```text
101,B,2500

102,A,2600

103,C,2700
```

---

## Method 3: DataFrame → RDD

Convert:

```scala
val r4 =
spark.range(20)
.toDF()
.rdd
```

Meaning:

```text
range()

↓

DataFrame

↓

RDD
```

Type:

```text
RDD[Row]
```

---

# 4. Types of RDD Operations

RDD operations:

```text
Transformations

Actions
```

---

# A. Transformations

Create new RDD.

Examples:

```scala
map()

flatMap()

filter()

union()

distinct()

groupByKey()

sortByKey()

join()

coalesce()
```

---

# B. Actions

Trigger execution.

Examples:

```scala
collect()

count()

first()

foreach()
```

---

# 5. collect()

Bring RDD to driver.

Example:

```scala
rdd.collect()
```

Output:

```text
Array(...)
```

---

# 6. foreach()

Print records.

Example:

```scala
rdd.foreach(println)
```

May produce unordered output.

Better:

```scala
rdd.collect()
.foreach(println)
```

---

# 7. count()

Count records.

Example:

```scala
rdd.count()
```

Output:

```text
10
```

---

# 8. first()

Retrieve first element.

Example:

```scala
rdd.first()
```

---

# 9. map()

Transform each element.

Example:

```scala
val x=
sc.parallelize(

Array(1,2,3)

)

val y=
x.map(
n=>n*2
)
```

Output:

```text
2

4

6
```

---

# 10. flatMap()

Flatten multiple outputs.

Example:

Input:

```text
Hello Spark
```

Code:

```scala
val r=
sc.parallelize(

Array(
"Hello Spark"
)

)

val x=
r.flatMap(
_.split(" ")
)
```

Output:

```text
Hello

Spark
```

Difference:

```text
map()

↓

Nested


flatMap()

↓

Flattened
```

---

# 11. filter()

Keep matching records.

Example:

```scala
val x=
sc.parallelize(
1 to 10
)

val y=
x.filter(
n=>n%2==0
)
```

Output:

```text
2

4

6

8

10
```

---

# 12. union()

Combine RDDs.

Example:

```scala
val a=
sc.parallelize(
Array(1,2,3)
)

val b=
sc.parallelize(
Array(3,4,5)
)

a.union(b)
.collect()
```

Output:

```text
1

2

3

3

4

5
```

Duplicates remain.

---

# 13. intersection()

Common elements.

Example:

```scala
val rdd1=
sc.parallelize(
Array(1,2,3,4)
)

val rdd2=
sc.parallelize(
Array(2,3,5,6)
)

rdd1
.intersection(rdd2)
.collect()
```

Output:

```text
2

3
```

---

# 14. distinct()

Remove duplicates.

Example:

```scala
val x=
sc.parallelize(

Array(
1,2,2,3,4,4
)

)

x.distinct()
.collect()
```

Output:

```text
1

2

3

4
```

---

# 15. groupByKey()

Group same keys.

Example:

```scala
val data=

sc.parallelize(

Seq(

('k',3),

('l',2),

('l',4),

('m',3)

)

)

data
.groupByKey()
.collect()
```

Output:

```text
(l,Seq(2,4))

(k,Seq(3))

(m,Seq(3))
```

Meaning:

```text
l

↓

2,4
```

---

# 16. sortByKey()

Sort using key.

Example:

```scala
val data=

sc.parallelize(

Seq(

(3,"A"),

(1,"B"),

(2,"C")

)

)

data
.sortByKey()
.collect()
```

Output:

```text
(1,B)

(2,C)

(3,A)
```

---

# 17. join()

Combine datasets by key.

Example:

RDD1:

```text
(1,A)

(2,B)
```

RDD2:

```text
(1,100)

(2,200)
```

Join:

```scala
rdd1.join(rdd2)
```

Output:

```text
(1,(A,100))

(2,(B,200))
```

---

# 18. coalesce()

Reduce partitions.

Example:

```scala
rdd.coalesce(2)
```

Partitions:

```text
Before

↓

5

After

↓

2
```

---

# 19. RDD Workflow

Complete process:

```text
Create RDD
     ↓

Transformation

(map/filter)

     ↓

More transformations

     ↓

Action

(collect/count)

     ↓

Execution starts
```

---

# 20. Important Commands Summary

| Command          | Purpose              |
| ---------------- | -------------------- |
| `parallelize()`  | Create RDD           |
| `textFile()`     | Load file            |
| `collect()`      | Bring data to driver |
| `count()`        | Count records        |
| `first()`        | First element        |
| `map()`          | Transform            |
| `flatMap()`      | Flatten              |
| `filter()`       | Filter               |
| `union()`        | Combine              |
| `intersection()` | Common records       |
| `distinct()`     | Remove duplicates    |
| `groupByKey()`   | Group by key         |
| `sortByKey()`    | Sort                 |
| `join()`         | Merge                |
| `coalesce()`     | Reduce partitions    |
| `foreach()`      | Print                |

---

# Mental Model for Spark

Think of Spark as:

```text
Raw Data

↓

RDD

↓

Transformations
(lazy)

↓

Actions
(execute)

↓

Result
```

Understanding this execution model is more important than memorizing individual commands.
