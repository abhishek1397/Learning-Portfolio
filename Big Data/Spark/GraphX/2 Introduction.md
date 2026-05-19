# Apache Spark GraphX Master Notes

## Scenario: Academic Collaboration Network Analysis

A university wants to analyze relationships between:

```text
Students
Professors
Postdocs
Researchers
```

Relations:

```text
advisor
collab
colleague
pi
```

Graph:

```text
istoica(prof)
      |
 colleague
      ↓

franklin(prof)
   |        \
advisor      pi
   ↓          ↓

rxin(student) → collab → jgonzal(postdoc)
```

Meaning:

```text
Vertex

↓

Person + Role


Edge

↓

Relationship
```

---

# Step 1: Import Required Libraries

Import GraphX:

```scala
import org.apache.spark._

import org.apache.spark.rdd.RDD

import org.apache.spark.graphx._
```

Purpose:

| Package | Purpose              |
| ------- | -------------------- |
| Spark   | Configure Spark      |
| RDD     | Distributed datasets |
| GraphX  | Graph processing     |

---

# Step 2: Create Vertices

Vertices:

Format:

```scala
(VertexID,
(Name,
Role))
```

Create:

```scala
val vertices =
Array(

(3L,("rxin","student")),

(7L,("jgonzal","postdoc")),

(5L,("franklin","prof")),

(2L,("istoica","prof"))

)
```

Output:

```text
(3,(rxin,student))

(7,(jgonzal,postdoc))

(5,(franklin,prof))

(2,(istoica,prof))
```

Interpretation:

| ID | Name     | Role    |
| -- | -------- | ------- |
| 3  | rxin     | student |
| 7  | jgonzal  | postdoc |
| 5  | franklin | prof    |
| 2  | istoica  | prof    |

---

# Step 3: Convert Vertices to RDD

GraphX requires RDD.

Command:

```scala
val vRDD =
sc.parallelize(vertices)
```

Meaning:

```text
Array

↓

RDD
```

---

# Step 4: Create Edges (Relationships)

Edge format:

```scala
Edge(
source,
destination,
relationship
)
```

Create:

```scala
val edges =
Array(

Edge(
3L,
7L,
"collab"
),

Edge(
5L,
3L,
"advisor"
),

Edge(
2L,
5L,
"colleague"
),

Edge(
5L,
7L,
"pi"
)

)
```

Interpretation:

```text
rxin

↓

collab

↓

jgonzal


franklin

↓

advisor

↓

rxin


istoica

↓

colleague

↓

franklin


franklin

↓

pi

↓

jgonzal
```

---

# Step 5: Convert Edges to RDD

Command:

```scala
val eRDD =
sc.parallelize(edges)
```

---

# Step 6: Create Default Vertex

Missing vertex value:

```scala
val defaultUser =
("john doe","missing")
```

Meaning:

Unknown user:

```text
name

↓

john doe


role

↓

missing
```

---

# Step 7: Create Graph

Combine:

```text
Vertices

+

Edges

=

Graph
```

Command:

```scala
val graph =
Graph(
vRDD,
eRDD,
defaultUser
)
```

Output:

```text
Graph[(String,String),String]
```

Meaning:

```text
Vertex attribute

↓

(name,role)


Edge attribute

↓

relationship
```

---

# Step 8: Display All Vertices

Command:

```scala
graph.vertices
.collect
.foreach(println)
```

Output:

```text
(2,(istoica,prof))

(3,(rxin,student))

(5,(franklin,prof))

(7,(jgonzal,postdoc))
```

---

# Step 9: Display All Edges

Command:

```scala
graph.edges
.collect
.foreach(println)
```

Output:

```text
Edge(
3,
7,
collab
)

Edge(
5,
3,
advisor
)

Edge(
2,
5,
colleague
)

Edge(
5,
7,
pi
)
```

---

# Step 10: Filter Vertices by Role

Find:

```text
Only postdocs
```

Command:

```scala
graph.vertices
.filter{

case (
id,
(name,pos)
)

=>

pos=="postdoc"

}
.count
```

Output:

```text
1
```

Meaning:

Only:

```text
jgonzal

↓

postdoc
```

Count:

```text
1
```

---

# Step 11: Filter Edges Using Source and Destination IDs

Command:

```scala
graph.edges
.filter(

e =>

e.srcId >
e.dstId

)
.count
```

Output:

```text
1
```

Meaning:

Find:

```text
sourceID

>

destinationID
```

Example:

```text
5→3

TRUE
```

---

# Step 12: Same Edge Filtering Using Pattern Matching

Equivalent command:

```scala
graph.edges
.filter{

case Edge(
src,
dst,
prop
)

=>

src >
dst

}
.count
```

Output:

```text
1
```

This is same logic written differently.

---

# Step 13: PageRank

## What is PageRank?

PageRank measures:

```text
Importance

or

Influence

of vertices
```

Higher rank:

```text
More important node
```

---

## Run PageRank

Command:

```scala
val rank =
graph
.pageRank(
0.0001
)
.vertices
```

Meaning:

Tolerance:

```text
0.0001

↓

Convergence threshold
```

---

## Print PageRank

Command:

```scala
println(

rank.collect()
.mkString("\n")

)
```

Output:

```text
(2,0.5037)

(3,0.8997)

(5,0.9318)

(7,1.6645)
```

Interpretation:

| Person   | Rank |
| -------- | ---- |
| istoica  | 0.50 |
| rxin     | 0.89 |
| franklin | 0.93 |
| jgonzal  | 1.66 |

Highest:

```text
jgonzal

↓

Most influential
```

Because:

Multiple incoming relationships:

```text
rxin → jgonzal

franklin → jgonzal
```

---

# Step 14: Important GraphX Commands Summary

| Command            | Purpose             |
| ------------------ | ------------------- |
| `parallelize()`    | Convert array → RDD |
| `Graph()`          | Create graph        |
| `vertices`         | Access nodes        |
| `edges`            | Access connections  |
| `filter()`         | Apply condition     |
| `count()`          | Count records       |
| `collect()`        | Bring to driver     |
| `foreach(println)` | Print               |
| `pageRank()`       | Compute importance  |
| `srcId`            | Source vertex       |
| `dstId`            | Destination vertex  |
| `Edge()`           | Create edge         |

---

# Full Program

```scala
import org.apache.spark._
import org.apache.spark.rdd.RDD
import org.apache.spark.graphx._

val vertices=
Array(

(3L,("rxin","student")),

(7L,("jgonzal","postdoc")),

(5L,("franklin","prof")),

(2L,("istoica","prof"))

)

val vRDD=
sc.parallelize(vertices)


val edges=
Array(

Edge(3L,7L,"collab"),

Edge(5L,3L,"advisor"),

Edge(2L,5L,"colleague"),

Edge(5L,7L,"pi")

)

val eRDD=
sc.parallelize(edges)


val defaultUser=
("john doe","missing")


val graph=
Graph(
vRDD,
eRDD,
defaultUser
)


graph.vertices
.collect
.foreach(println)


graph.edges
.collect
.foreach(println)



graph.vertices
.filter{

case(
id,
(name,pos)
)

=>

pos=="postdoc"

}
.count



graph.edges
.filter(

e=>

e.srcId>
e.dstId

)
.count



graph.edges
.filter{

case Edge(
src,
dst,
prop
)

=>

src>
dst

}
.count



val rank=
graph
.pageRank(
0.0001
)
.vertices



println(

rank.collect
.mkString("\n")

)
```

---

# Complete Workflow

```text
Create Vertices
      ↓

Convert → vRDD
      ↓

Create Edges
      ↓

Convert → eRDD
      ↓

Create Default Vertex
      ↓

Create Graph
      ↓

Display Graph
      ↓

Filter Vertices
      ↓

Filter Edges
      ↓

Count Results
      ↓

Compute PageRank
      ↓

Analyze Influence
```

This practical introduces **attribute filtering + relationship analysis + PageRank**, which are more advanced than simple `degrees` and `triplets`.
