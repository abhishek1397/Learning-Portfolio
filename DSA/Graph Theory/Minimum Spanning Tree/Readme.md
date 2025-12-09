# **Minimum Spanning Tree (MST)**

<img src="https://github.com/user-attachments/assets/953a254c-2003-4c98-a8aa-6a2c2edad9f3" width="950" height="450">

## **What is a Spanning Tree?**

A **spanning tree** of a connected, undirected graph is a subgraph that:

* Includes **all vertices** of the original graph
* Contains exactly **(V − 1)** edges
* Is **connected**
* Contains **no cycles** (acyclic)

A graph may have **multiple possible spanning trees**.

---

## **What is a Minimum Spanning Tree (MST)?**

<img width="471" height="296" alt="image" src="https://github.com/user-attachments/assets/bfdce30a-b3da-4ee2-843e-9831a292c86b" />

A **Minimum Spanning Tree** is a spanning tree with the **minimum total edge weight** among all possible spanning trees of the graph.

* MST contains **exactly (V − 1)** edges
* All vertices must be included
* Multiple MSTs may exist for the same graph if edge weights allow ties

---

## **Properties of Spanning Tree**

| Property           | Description                       |
| ------------------ | --------------------------------- |
| Number of Vertices | Same as original graph (V)        |
| Number of Edges    | Always `(V - 1)`                  |
| Connectivity       | Always connected                  |
| Acyclic            | No cycles allowed                 |
| Cost               | Sum of all included edge weights  |
| Uniqueness         | Multiple spanning trees may exist |

---

## **Properties of Minimum Spanning Tree**

| Aspect            | Description                                                        |
| ----------------- | ------------------------------------------------------------------ |
| Weight            | Minimum possible among all spanning trees                          |
| Input Requirement | Graph must be **connected** and **undirected** with weighted edges |
| Result            | May not be unique (depends on weights)                             |

---

## **Algorithms for Finding MST**

| Algorithm               | Strategy Type | Key Concepts                                                                                                          | Best Use Case                              |
| ----------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| **Kruskal’s Algorithm** | Greedy        | Sort edges by weight, pick smallest edges without forming cycles, use **Disjoint Set (Union-Find)**                   | Sparse graphs, edge list representation    |
| **Prim’s Algorithm**    | Greedy        | Start from any vertex, repeatedly add the smallest edge connecting tree to non-tree vertices, uses **priority queue** | Dense graphs, adjacency matrix or list     |
| **Borůvka’s Algorithm** | Greedy        | Each vertex picks the cheapest outgoing edge, merge components iteratively                                            | Distributed systems or parallel processing |

---

### **1. Kruskal’s Algorithm — Summary**

* Sort edges by increasing weight
* Add the smallest edge that does **not** form a cycle
* Repeat until `(V - 1)` edges are included
* Uses **Disjoint Set Union (DSU)** for cycle detection

---

### **2. Prim’s Algorithm — Summary**

* Start from any vertex
* Grow the MST by selecting the smallest weight edge connecting visited and unvisited vertices
* Uses **priority queue (min-heap)** to track cheapest edge

---

### **3. Borůvka’s Algorithm — Summary**

* Initially treat each vertex as its own tree
* Each component selects its **minimum outgoing edge**
* Merge components until only one remains (the MST)

---

## **Applications of MST**

| Domain                                 | Usage                                                                  |
| -------------------------------------- | ---------------------------------------------------------------------- |
| **Network Design**                     | Building cost-efficient communication, road, or electrical networks    |
| **Image Processing & Computer Vision** | Segmentation, edge detection, clustering                               |
| **Biology (Phylogenetics)**            | Constructing evolutionary trees                                        |
| **Data Clustering**                    | Used in MST-based clustering algorithms (e.g., single-link clustering) |
| **Social Network Analysis**            | Identifying minimum connection structures                              |
| **Routing and Optimization**           | Logistics, shortest linkage between distributed nodes                  |

---

## **Quick Comparison: MST vs Shortest Path Tree**

| Feature               | Minimum Spanning Tree      | Shortest Path Tree              |
| --------------------- | -------------------------- | ------------------------------- |
| Goal                  | Minimize total edge weight | Minimize distance from a source |
| Includes All Vertices | Yes                        | Only reachable vertices         |
| Uses Edge Weights     | Yes                        | Yes                             |
| Algorithms            | Kruskal, Prim, Borůvka     | Dijkstra, Bellman-Ford          |

---

## **Summary Facts for Exams**

* MST exists **only** for **connected, weighted, undirected graphs**
* Uses **greedy strategy**
* Contains **(V − 1)** edges
* MST may not be **unique**

---

