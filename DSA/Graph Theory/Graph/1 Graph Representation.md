# **Graph Representation**

A **Graph** is a non-linear data structure consisting of:

* **Vertices (Nodes):** Entities in the graph
* **Edges (Links):** Connections between vertices

A graph is formally represented as:

```
G(V, E)
```

Where:

* `V` = Set of vertices
* `E` = Set of edges connecting pairs of vertices

---

## **Why Representation Matters**

Since graphs can be implemented in multiple ways depending on:

* Graph type (directed, undirected, weighted)
* Memory usage constraints
* Expected operations (searching, updating, traversing)
* Application (network routing, social graphs, compilers, maps)

Different storage structures are chosen to optimize performance.


### **Common Ways to Represent Graphs**

| Representation Method | Storage Type                             | Best For                                      | Space Complexity | Edge Lookup | Traversal Speed      |
| --------------------- | ---------------------------------------- | --------------------------------------------- | ---------------- | ----------- | -------------------- |
| **Adjacency Matrix**  | 2-D Matrix (V×V)                         | Dense graphs                                  | O(V²)            | O(1)        | O(V²)                |
| **Adjacency List**    | Array of linked lists (or dynamic lists) | Sparse graphs                                 | O(V + E)         | O(degree)   | O(V + E)             |
| **Edge List**         | List of edges                            | Simple storage, graph algorithms input format | O(E)             | O(E)        | Depends on algorithm |

---

### **1. Adjacency Matrix Representation**

A **V×V matrix** where:

* `A[i][j] = 1` → edge exists (unweighted)
* `A[i][j] = w` → weighted edge exists
* `A[i][j] = 0 or ∞` → no edge

Matrix is:

* **Symmetric** for undirected graphs
* **Not symmetric** for directed graphs

Useful when:

* Graph is **dense**
* Frequent edge lookup required
* Used in algorithms like Floyd-Warshall


### **2. Adjacency List Representation**

Each vertex stores a list of connected vertices.

Example (undirected graph):

```
A → B, C
B → A, D
C → A
D → B
```

Efficient when:

* Graph is **sparse**
* Memory needs optimization
* Used in DFS, BFS, Dijkstra, Prim algorithms

Space required:

```
O(V + E)
```

### **3. Edge List Representation**

Stores only the edges in the form:

```
(u, v)
```

For weighted graphs:

```
(u, v, w)
```

Example:

```
[(1,2), (1,3), (2,4)]
```

Useful for:

* Sorting edges (Kruskal’s MST algorithm)
* File formats for large networks
* Simple storage and exporting

### **Choosing the Right Representation**

| Requirement                             | Best Representation |
| --------------------------------------- | ------------------- |
| Fast edge lookup                        | Adjacency Matrix    |
| Memory efficiency with sparse edges     | Adjacency List      |
| Graph algorithms requiring sorted edges | Edge List           |

### **Summary**

Graph representation affects:

* Space usage
* Speed of searching edges
* Traversal complexity
* Suitability for different real-world applications

Choosing the correct representation ensures efficient graph processing and algorithm performance.

---

# **Adjacency Matrix Representation of Graphs**

An **Adjacency Matrix** is a **square matrix** used to represent a graph.
For a graph with **V vertices**, the matrix is of size:

```
V × V
```

Each cell `A[i][j]` indicates whether there is an edge between **vertex i and vertex j**, and optionally stores its **weight**.

A graph is represented as:

```
G(V, E)
```

Where:

* `V` = set of vertices
* `E` = set of edges

Adjacency Matrix is widely used in graph representation, especially when the graph is **dense**.


## **Types of Adjacency Matrix Representations**

|||
|-|-|
| ![](https://github.com/user-attachments/assets/24939892-fd67-474f-ab54-76c1fdb486e1) |![Adjacency-Matrix-for-Directed-and-Unweighted-graph](https://github.com/user-attachments/assets/61b5d1b7-ebc3-418e-ba93-b6f6df70c876)  |
| ![Adjacency-Matrix-for-Undirected-and-Weighted-graph](https://github.com/user-attachments/assets/2aa28cba-7d6c-44e6-a845-5758f840f51b) | ![Adjacency-Matrix-for-Directed-and-Weighted-graph](https://github.com/user-attachments/assets/f2361061-4320-4737-871c-ddf6665d70fd) |


### **1. Undirected and Unweighted Graph**

* If an edge exists between vertex `i` and `j`, then:

```
A[i][j] = 1
A[j][i] = 1   (symmetric matrix)
```

* If no edge exists:

```
A[i][j] = 0
```

Key Characteristics:

* Matrix is **symmetric**
* Values are **0 or 1**

### **2. Undirected and Weighted Graph**



* If no edge exists between `i` and `j`, then:

```
A[i][j] = ∞ (or 0 depending on convention)
```

* If edge exists with weight `w`:

```
A[i][j] = w
A[j][i] = w   (symmetric)
```

 Key Characteristics:

* Represents real-world networks: maps, distances, communication cost
* Matrix remains **symmetric**


### **3. Directed and Unweighted Graph**

* If there is a directed edge from `i → j`:

```
A[i][j] = 1
```

* If no edge:

```
A[i][j] = 0
```

Key Characteristics:

* **Matrix is not symmetric**
* Direction matters (e.g., one-way roads, dependencies)


### **4. Directed and Weighted Graph**

* If no directed edge exists from `i → j`:

```
A[i][j] = ∞
```

* If directed edge exists with weight `w`:

```
A[i][j] = w
```

Key Characteristics:

* Used in shortest path algorithms (Dijkstra, Floyd–Warshall)


## **Properties of Adjacency Matrix**

| Property        | Description                                          |
| --------------- | ---------------------------------------------------- |
| Matrix Size     | `V × V`                                              |
| Diagonal Values | Usually `0` (no self-loops) or weight if loop exists |
| Symmetry        | Only for **undirected** graphs (`A[i][j] = A[j][i]`) |
| Value Meaning   | 0/1 for unweighted, weights/∞ for weighted graphs    |


## **Applications of Adjacency Matrix**

* Faster edge lookups
* Detecting connectivity between nodes
* Finding vertex degrees
* Used in algorithms like:

  * **Floyd–Warshall**
  * **Prim’s (dense graphs)**
  * **Graph coloring**
  * **Network flow analysis**

### **Advantages**

| Advantage             | Explanation                                  |
| --------------------- | -------------------------------------------- |
| Simple Representation | Easy to understand and implement             |
| Fast Edge Query       | Checking if edge exists takes `O(1)` time    |
| Best for Dense Graphs | Uses space efficiently when most edges exist |

### **Disadvantages**

| Limitation                          | Explanation                                       |
| ----------------------------------- | ------------------------------------------------- |
| Space Inefficient for Sparse Graphs | Always uses `V²` space, even when few edges exist |
| Costly Modifications                | Adding/deleting nodes requires resizing matrix    |
| Slower Traversal                    | BFS/DFS takes `O(V²)` even if few edges exist     |

### **Degree Calculation Using Adjacency Matrix**

| Graph Type       | Degree Computation                             |
| ---------------- | ---------------------------------------------- |
| Undirected Graph | Degree of vertex = Sum of row entries          |
| Directed Graph   | In-degree = column sum ; Out-degree = row sum |

---

# **Adjacency List Representation**

An **adjacency list** is a graph representation method where each vertex stores a list of its adjacent (connected) vertices. It is memory-efficient and ideal for **sparse graphs**.

### **Structure**

* Implemented as an array/list of linked lists or dynamic lists.
* Index represents a vertex.
* The list at each index contains the vertices directly reachable from that vertex.

Example format:

```
0 → 1, 3  
1 → 0, 2  
2 → 1  
3 → 0
```

## **Types of Adjacency Lists**

### **1. Directed and Unweighted Graph**

|||
|-|-|
| ![graph-representation-of-directed-graph-to-adjacency-list](https://github.com/user-attachments/assets/f5a5c69b-8e49-44b4-9642-620a44e85ec9) | ![graph-representation-of-directed-graph-to-adjacency-list-2](https://github.com/user-attachments/assets/465b30ee-6bbb-4f45-9da7-173b16317b5d) |
|![graph-representation-of-directed-graph-to-adjacency-list-3](https://github.com/user-attachments/assets/e23c1fd1-1d23-47ab-a85c-59db27a4e0a6) |![graph-representation-of-directed-graph-to-adjacency-list-4](https://github.com/user-attachments/assets/4dded0a4-2811-4a1f-9cb1-deda6bdb90de)|


* Each directed edge `(u → v)` appears only once under vertex `u`.

Example:

```
0:  
1: 0, 2  
2: 0
```

### **2. Undirected and Unweighted Graph**

|||
|-|-|
| ![graph-representation-of-undirected-graph-to-adjacency-list-1](https://github.com/user-attachments/assets/dd70f917-009d-4d37-8fdd-33211f6c6737) | ![graph-representation-of-undirected-graph-to-adjacency-list-2](https://github.com/user-attachments/assets/f2833ef7-d7fd-4e74-9857-896e07d76f5e) |
| ![graph-representation-of-undirected-graph-to-adjacency-list-3](https://github.com/user-attachments/assets/39390885-e8bf-4170-ae67-de4d9d1dc029) | ![graph-representation-of-undirected-graph-to-adjacency-list-4](https://github.com/user-attachments/assets/0f2fdc46-312c-4174-815d-547389f9070a) |


* Each edge `(u — v)` appears **twice**:

  * Once under `u`
  * Once under `v`

Example:

```
0: 1, 2  
1: 0, 2  
2: 0, 1
```


### **3. Directed and Weighted Graph**

|||
|-|-|
| ![graph-representation-of-directed-weighted-graph-to-adjacency-list-1](https://github.com/user-attachments/assets/8c60ae24-041f-4e45-b883-141e474f360f) | ![graph-representation-of-directed-weighted-graph-to-adjacency-list-2](https://github.com/user-attachments/assets/4c8d0e15-5a42-4747-b429-fe1666540530) |
| ![graph-representation-of-directed-weighted-graph-to-adjacency-list-3](https://github.com/user-attachments/assets/e9ede249-3cf0-47b8-bb91-38ef1896cedd) | ![graph-representation-of-directed-weighted-graph-to-adjacency-list-4](https://github.com/user-attachments/assets/23b4362c-3b7c-43a1-bcc4-33a550663bdb) |


* Each stored entry contains both the adjacent vertex and weight `(vertex, weight)`.

Example:

```
1 → {0,4}, {2,3}  
2 → {0,1}
```

### **4. Undirected and Weighted Graph**

|||
|-|-|
| ![graph-representation-of-undirected-weighted-graph-to-adjacency-list-1](https://github.com/user-attachments/assets/f2f2f5ae-fe73-4d3d-aed1-16ce9089e284) | ![graph-representation-of-undirected-weighted-graph-to-adjacency-list-2](https://github.com/user-attachments/assets/353767a2-4215-4554-a729-2d054ac16574) |
|![graph-representation-of-undirected-weighted-graph-to-adjacency-list-3](https://github.com/user-attachments/assets/31132fad-242c-48ac-af9a-b72eb1d476f1)  | ![graph-representation-of-undirected-weighted-graph-to-adjacency-list-4](https://github.com/user-attachments/assets/6fb704e9-524a-47b6-9c3a-bd202c7178db) |


* Every weighted edge appears twice, once from each direction.

Example:

```
0 → {1,4}, {2,1}
1 → {0,4}, {2,3}
2 → {1,3}, {0,1}
```

---

### **Characteristics**

* Uses a list of lists (or dictionary mapping).
* Size grows proportionally with vertices and edges.
* Listing all neighbors of a vertex takes time proportional to its degree.

Time to get all neighbors of a vertex:

```
O(k)
```

Where `k` = number of adjacent vertices.

## **Applications**

Adjacency lists are commonly used in:

* **Graph traversal algorithms**
  – BFS
  – DFS
* **Shortest path algorithms**
  – Dijkstra
  – Bellman-Ford
* **Minimum spanning tree algorithms**
  – Prim
  – Kruskal
* **Real-world modeling**
  – Social networks
  – Road networks
  – Routing tables

### **Advantages**

| Benefit                        | Explanation                                              |
| ------------------------------ | -------------------------------------------------------- |
| **Space Efficient**            | Requires `O(V + E)` memory, ideal for sparse graphs.     |
| **Faster Traversals**          | BFS/DFS run in linear time.                              |
| **Easy to Modify**             | Adding or removing vertices/edges is simpler.            |
| **Better for Most Algorithms** | Works efficiently with shortest path and MST algorithms. |


### **Disadvantages**

| Limitation                          | Explanation                                                   |
| ----------------------------------- | ------------------------------------------------------------- |
| **Slow Edge Lookup**                | Checking if edge exists `(u,v)` may take linear scan time.    |
| **Less Efficient for Dense Graphs** | When edges approach `V²`, adjacency matrix becomes better.    |
| **Not Constant Time for Access**    | Since edges are stored as lists, random access is not direct. |

### **When to Use**

| Condition                       | Best Choice               |
| ------------------------------- | ------------------------- |
| Graph is sparse                 | ✔ Use adjacency list      |
| Need fast iteration of edges    | ✔ Adjacency list          |
| Frequent edge-existence queries | ✘ Prefer adjacency matrix |

---

# **Edge List Representation**

An **Edge List** is a graph storage format where the graph is represented as a list of edges. Each edge is stored as a **pair (u, v)** or a **triple (u, v, w)** if the graph is weighted.

It is one of the simplest graph representations and is especially suited for **sparse graphs** and algorithms that operate directly on edges.


### **Structure**

* Stored as a list/array/set of tuples:

  ```
  (u, v)        → Unweighted edge  
  (u, v, w)     → Weighted edge  
  ```

* No adjacency relationships are precomputed; the list only stores edges.

### **Representation Based on Graph Type**

| Graph Type                | Format Example   | Notes                                                    |
| ------------------------- | ---------------- | -------------------------------------------------------- |
| **Undirected Unweighted** | `(A, B), (A, C)` | Edge implies bidirectional connection.                   |
| **Directed Unweighted**   | `(A, B), (A, C)` | Represents directed edges `A → B` and `A → C`.           |
| **Undirected Weighted**   | `(A, B, 5)`      | Weight indicated along with endpoints.                   |
| **Directed Weighted**     | `(A, B, 5)`      | Represents directed weighted edge `A → B` with weight 5. |

### **Properties**

* **Space Complexity:**

  ```
  O(E)
  ```

  Only edges are stored.

* **Suitable for Sparse Graphs:**
  Efficient when `E` is much smaller than `V²`.

* **Direct Edge Traversal:**
  Ideal for algorithms that iterate over edges rather than checking neighbors.

### **Applications**

| Use Case                                               | Why Edge List Works Well                                             |
| ------------------------------------------------------ | -------------------------------------------------------------------- |
| **Graph Construction**                                 | Easy to build when edges arrive incrementally.                       |
| **Shortest Path Algorithms** (Dijkstra, Bellman-Ford)  | Bellman-Ford and Relaxation-based methods operate directly on edges. |
| **Network Flow Algorithms** (Ford-Fulkerson, Max-Flow) | Uses edges as primary objects for capacity and flow updates.         |
| **Graph Traversal** (DFS/BFS in sparse graphs)         | Efficient for iterating edges during traversal initialization.       |
| **Graph Coloring / Constraints Checking**              | Edges directly represent conflicts or adjacency rules.               |

### **Advantages**

| Advantage                             | Description                                                             |
| ------------------------------------- | ----------------------------------------------------------------------- |
| **Space Efficient for Sparse Graphs** | Stores only existing edges, not full matrix.                            |
| **Simple Representation**             | Intuitive and minimal format.                                           |
| **Easy Edge Manipulation**            | Adding/removing edges is constant-time (append/remove).                 |
| **Efficient Edge Iteration**          | Algorithms processing edges (MST, Bellman-Ford, etc.) benefit directly. |


### **Disadvantages**

| Limitation                         | Consequence                                                          |
| ---------------------------------- | -------------------------------------------------------------------- |
| **Slow Vertex Lookup**             | To check adjacency `(u, v)`, full scan of edges may be needed.       |
| **Inefficient Neighbor Retrieval** | Finding all neighbors of a vertex requires scanning the entire list. |
| **Degree Not Directly Available**  | Computing degrees requires counting occurrences in full edge list.   |
| **Not Ideal for Dense Graphs**     | Adjacency matrix becomes more efficient when `E ≈ V²`.               |


### **When to Use Edge List vs Other Representations**

| Condition                              | Best Representation           |
| -------------------------------------- | ----------------------------- |
| Graph is **sparse**                    | ✔ Edge List or Adjacency List |
| Need **fast edge processing**          | ✔ Edge List                   |
| Frequent **adjacency checks** `(u,v)?` | ✘ Adjacency Matrix preferred  |
| Frequent **vertex traversal**          | ✔ Adjacency List              |

---

