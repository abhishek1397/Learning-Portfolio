# Apache Spark GraphX Master Notes

## Scenario: Student Friendship Network Analysis

University wants to analyze student friendships.

Students:

```text
Aman
Riya
Karan
Simran
```

Friendships:

```text
Aman → Riya
Riya → Karan
Karan → Simran
Simran → Aman
```

Graph representation:

```text
Aman ----> Riya
 ↑          |
 |          ↓
Simran <--- Karan
```

Graph concepts:

```text
Vertex = Student

Edge = Friendship

Graph = Students + Friendships
```

---

# Step 1: Import Required Libraries

Import GraphX packages:

```scala
import org.apache.spark._
import org.apache.spark.rdd.RDD
import org.apache.spark.graphx._
```

Purpose:

| Package | Use                  |
| ------- | -------------------- |
| Spark   | Configure Spark      |
| RDD     | Distributed datasets |
| GraphX  | Graph processing     |

---

# Step 2: Create Spark Context

Initialize Spark:

```scala
val conf =
new SparkConf()
.setAppName("StudentFriendship")
.setMaster("local")

val sc =
new SparkContext(conf)
```

Meaning:

```text
local

↓

Run on local machine
```

---

# Step 3: Create Vertices (Students)

Vertices represent students.

Format:

```scala
(VertexID, Attribute)
```

Example:

```scala
val vertices =
Array(

(1L,"Aman"),
(2L,"Riya"),
(3L,"Karan"),
(4L,"Simran")

)
```

Output:

```text
(1,Aman)
(2,Riya)
(3,Karan)
(4,Simran)
```

Visual:

```text
1 → Aman

2 → Riya

3 → Karan

4 → Simran
```

---

# Step 4: Convert Vertices to RDD

GraphX needs RDDs.

Command:

```scala
val vRDD =
sc.parallelize(vertices)
```

Check:

```scala
vRDD.take(2)
```

Output:

```text
Array(
(1,Aman),
(2,Riya)
)
```

Meaning:

```text
take(n)

↓

Retrieve first n records
```

---

# Step 5: Create Edges (Friendships)

Edges:

Format:

```scala
Edge(
source,
destination,
attribute
)
```

Example:

Friendship strength:

```scala
val edges =
Array(

Edge(1L,2L,1800),

Edge(2L,3L,800),

Edge(3L,4L,1400),

Edge(4L,1L,1000)

)
```

Interpretation:

```text
Aman → Riya =1800

Riya → Karan=800

Karan → Simran=1400

Simran → Aman=1000
```

---

# Step 6: Convert Edges to RDD

Command:

```scala
val eRDD =
sc.parallelize(edges)
```

Check:

```scala
eRDD.take(2)
```

Output:

```text
Edge(1,2,1800)

Edge(2,3,800)
```

---

# Step 7: Default Vertex Value

If missing vertex occurs:

```scala
val nowhere =
"nowhere"
```

Meaning:

Missing node:

```text
Vertex → "nowhere"
```

---

# Step 8: Create Graph

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
nowhere
)
```

Output:

```text
Graph[String,Int]
```

Meaning:

```text
Vertex attribute → String

Edge attribute → Int
```

---

# Step 9: Display All Vertices

Command:

```scala
graph.vertices
.collect
.foreach(println)
```

Output:

```text
(1,Aman)

(2,Riya)

(3,Karan)

(4,Simran)
```

---

# Step 10: Display All Edges

Command:

```scala
graph.edges
.collect
.foreach(println)
```

Output:

```text
Edge(1,2,1800)

Edge(2,3,800)

Edge(3,4,1400)

Edge(4,1,1000)
```

---

# Step 11: Count Total Friendships

Command:

```scala
val total =
graph.numEdges
```

Output:

```text
4
```

Meaning:

Total edges:

```text
A→B

B→C

C→D

D→A

Total =4
```

---

# Step 12: Filter Friendships

Find friendship >1000

Command:

```scala
graph.edges
.filter{

case Edge(
src,
dst,
prop
)

=> prop>1000

}
.collect
.foreach(println)
```

Output:

```text
Edge(1,2,1800)

Edge(3,4,1400)
```

Meaning:

Remove:

```text
prop<=1000
```

---

# Step 13: Graph Triplets

Triplet:

```text
(Source Vertex,
Destination Vertex,
Edge Value)
```

Command:

```scala
graph.triplets
.collect
.foreach(println)
```

Output:

```text
((1,Aman),
(2,Riya),
1800)

((2,Riya),
(3,Karan),
800)
```

Triplets provide:

```text
Who

↓

Connected to whom

↓

Relationship value
```

---

# Step 14: In-Degree

Definition:

```text
Incoming edges
```

Command:

```scala
val inDeg =
graph.inDegrees

inDeg.collect()
```

Example output:

```text
(1,1)

(2,1)

(3,1)

(4,1)
```

Meaning:

Each receives:

```text
1 friendship
```

---

# Step 15: Out-Degree

Definition:

```text
Outgoing edges
```

Command:

```scala
val outDeg =
graph.outDegrees

outDeg.collect()
```

Output:

```text
(1,1)

(2,1)

(3,1)

(4,1)
```

Meaning:

Each sends:

```text
1 friendship
```

---

# Step 16: Total Degree

Formula:

```text
Total Degree

=

InDegree

+

OutDegree
```

Command:

```scala
val degrees =
graph.degrees

degrees.collect()
```

Output:

```text
(1,2)

(2,2)

(3,2)

(4,2)
```

Interpretation:

Example:

Aman:

```text
Incoming=1

Outgoing=1

Total=2
```

---

# Step 17: Find Number of Friends Per Student

Join vertices with degrees:

Command:

```scala
graph.vertices
.join(graph.degrees)
.collect
.foreach(println)
```

Output:

```text
(1,(Aman,2))

(2,(Riya,2))

(3,(Karan,2))

(4,(Simran,2))
```

Meaning:

```text
Aman → 2 friends

Riya → 2 friends

Karan → 2 friends

Simran → 2 friends
```

---

# Step 18: Important GraphX Commands Summary

| Command            | Purpose                     |
| ------------------ | --------------------------- |
| `parallelize()`    | Convert collection to RDD   |
| `take(n)`          | First n records             |
| `Graph()`          | Create graph                |
| `vertices`         | Access vertices             |
| `edges`            | Access edges                |
| `collect()`        | Bring data to driver        |
| `foreach(println)` | Print                       |
| `numEdges`         | Count edges                 |
| `filter()`         | Apply condition             |
| `triplets`         | Source + Destination + Edge |
| `inDegrees`        | Incoming edges              |
| `outDegrees`       | Outgoing edges              |
| `degrees`          | Total degree                |
| `join()`           | Combine datasets            |
| `Edge()`           | Create edge                 |

---

# Full Program (Master Version)

```scala
import org.apache.spark._
import org.apache.spark.rdd.RDD
import org.apache.spark.graphx._

val vertices=
Array(

(1L,"Aman"),
(2L,"Riya"),
(3L,"Karan"),
(4L,"Simran")

)

val vRDD=
sc.parallelize(vertices)


val edges=
Array(

Edge(1L,2L,1800),

Edge(2L,3L,800),

Edge(3L,4L,1400),

Edge(4L,1L,1000)

)

val eRDD=
sc.parallelize(edges)


val nowhere=
"nowhere"


val graph=
Graph(
vRDD,
eRDD,
nowhere
)


graph.vertices.collect.foreach(println)

graph.edges.collect.foreach(println)


println(graph.numEdges)


graph.edges
.filter{
case Edge(src,dst,prop)
=> prop>1000
}
.collect
.foreach(println)


graph.triplets
.collect
.foreach(println)


graph.inDegrees.collect()


graph.outDegrees.collect()


graph.degrees.collect()


graph.vertices
.join(graph.degrees)
.collect
.foreach(println)
```

---

# Complete GraphX Workflow

```text
Create Vertices
      ↓

Convert → vRDD
      ↓

Create Edges
      ↓

Convert → eRDD
      ↓

Create Graph
      ↓

Display Graph
      ↓

Analyze

(numEdges)

(filter)

(triplets)

(inDegrees)

(outDegrees)

(degrees)

(join)
```
