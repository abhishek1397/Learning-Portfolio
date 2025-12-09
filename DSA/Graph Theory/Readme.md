# **Introduction to Graph Theory**

### **What is Graph Theory?**

Graph Theory is a branch of mathematics used to model relationships between objects. It represents real-world systems such as:

* City road networks
* Social connections
* Computer networks
* Biological and logistics systems

Graphs allow these relationships to be studied mathematically and algorithmically.

||||
|-|-|-|
|![google_maps](https://github.com/user-attachments/assets/aaa07190-2cde-418c-9625-b52e06f4519a)|![social_networks](https://github.com/user-attachments/assets/35f17e79-8383-4324-bf35-150f1bac0925)|![linux_file_system](https://github.com/user-attachments/assets/9c32f25f-6a95-4015-b537-5d429905def6)|


### **Definition of a Graph**

A **Graph (G)** is formally defined as:

```
G = (V, E)
```

Where:
* **V** → set of vertices (nodes)
* **E** → set of edges (connections between vertices)


|||
|-|-|
| ![Introduction-to-Graphs](https://github.com/user-attachments/assets/f16c0a23-1213-410d-a3be-095ed63ac1d0) | ![Graph](https://github.com/user-attachments/assets/494be43f-7ebb-4357-9125-9f903143e2b4)|


## **Basic Components**

| Term                   | Meaning                                                              |
| ---------------------- | -------------------------------------------------------------------- |
| **Vertex (Node)**      | A point representing an object/entity                                |
| **Edge (Link)**        | A line connecting two vertices                                       |
| **Adjacent Vertices**  | Two vertices connected directly by an edge                           |
| **Degree of a Vertex** | Number of edges connected to it                                      |
| **Path**               | A sequence of vertices connected by edges (no repetition)            |
| **Cycle**              | A path that starts and ends at the same vertex                       |
| **Connected Graph**    | A path exists between every pair of vertices                         |
| **Subgraph**           | A graph formed from a subset of vertices and edges of a larger graph |
| **Loop**               | An edge connecting a vertex to itself                                |
| **Parallel Edges**     | Multiple edges between the same pair of vertices                     |

### Degree Specifics:

* **Undirected Graph:** Degree = count of connected edges
* **Directed Graph:**
  * **In-Degree:** incoming edges
  * **Out-Degree:** outgoing edges

---

## **Types of Graphs**

<img width="686" height="511" alt="GraphCM" src="https://github.com/user-attachments/assets/17c4a23f-3a1d-48d5-9743-2dbebececdd5" />

### **1️⃣ Based on Size**

| Graph Type         | Description                         | Example / Notes                   ||
| ------------------ | ----------------------------------- | --------------------------------- |-|
| **Finite Graph**   | Finite number of vertices and edges | Most real-world networks          |![finite](https://github.com/user-attachments/assets/c4724c85-9274-466e-b6a9-a3b1825ef95a) |
| **Infinite Graph** | Infinite vertices and edges         | Mathematical / theoretical models |![infinite](https://github.com/user-attachments/assets/e0d5a42a-2b96-4264-9b8d-83c8bba8d30d) |

---

### **2️⃣ Based on Structure**

| Graph Type              | Allows Parallel Edges? | Allows Self-loops? | Description                                        ||
| ----------------------- | ---------------------- | ------------------ | -------------------------------------------------- |-|
| **Trivial Graph**       | No                     | No                 | Single vertex, no edges                            | ![trivial](https://github.com/user-attachments/assets/86a0e6b7-a66f-4500-ad59-f14a26a9e6f5)|
| **Simple Graph**        | No                     | No                 | Basic undirected model                             | ![simple](https://github.com/user-attachments/assets/125c6a79-63aa-482d-9270-122f31e49f1f)|
| **Multigraph**          | Yes                    | No                 | Multiple edges between same vertices               |![multi](https://github.com/user-attachments/assets/b5dc5d71-9f2a-4c1f-a700-19ca69c4a5b4) |
| **Null Graph**          | No                     | No                 | Only vertices, no edges                            |![null](https://github.com/user-attachments/assets/74542767-e99b-493f-8da3-78836c82273f) |
| **Complete Graph (Kn)** | No                     | No                 | Every pair of vertices connected; edges = n(n−1)/2 | ![Undirected](https://github.com/user-attachments/assets/5ce1a2db-88cb-463a-98ad-cb48a256ae1f)|

---

### **3️⃣ Based on Direction**

| Graph Type                   | Edge Direction | Description             | Use Case                       ||
| ---------------------------- | -------------- | ----------------------- | ------------------------------ |-|
| **Directed Graph (Digraph)** | Yes            | Edges have direction    | Web links, one-way roads       |![simplee](https://github.com/user-attachments/assets/20fadabd-27e7-4994-9f82-6775e6d5353d) |
| **Undirected Graph**         | No             | Edges are bidirectional | Social networks, two-way roads |![Undirected](https://github.com/user-attachments/assets/2df7a2a4-77fe-4fd4-8b81-c01c34287d94) |

---

### **4️⃣ Based on Edge Weights**

| Graph Type           | Edge Weight | Description                    | Examples                      ||
| -------------------- | ----------- | ------------------------------ | ----------------------------- |-|
| **Weighted Graph**   | Yes         | Edges store cost/distance/time | Google Maps, airline networks | ![w](https://github.com/user-attachments/assets/055aec45-412b-4baa-8c9a-f1b9f4a5784f)|
| **Unweighted Graph** | No          | All edges considered equal     | Basic relationship graphs     | ![dense](https://github.com/user-attachments/assets/f7728e79-8d85-4bc4-90a6-83458af73aa8)|

---

### **5️⃣ Special Graph Categories**

| Graph Type        | Description                     | Properties                         ||
| ----------------- | ------------------------------- | ---------------------------------- |-|
| **Pseudograph**   | Allows loops and multiple edges | Most flexible structure            |![Pseudo_Graph (1)](https://github.com/user-attachments/assets/1628f984-5d9f-4c9f-8894-d49f66f9099d) |
| **Regular Graph** | Every vertex has same degree k  | Complete graph Kn is (n−1)-regular |![frame_3266](https://github.com/user-attachments/assets/7df0d6e4-b206-41e1-9780-be0d874e7484) |

---

### **6️⃣ Based on Density**

| Graph Type       | Edge Count                     | Description                        | Example                    ||
| ---------------- | ------------------------------ | ---------------------------------- | -------------------------- |-|
| **Sparse Graph** | Low edges relative to vertices | Leaves many possible edges missing | Chemical reaction networks | ![sparse](https://github.com/user-attachments/assets/797f81b3-d293-4c0d-b02d-5f6ee8367562) |
| **Dense Graph**  | High number of edges           | Close to complete graph            | Strong social network      | ![dense](https://github.com/user-attachments/assets/41a82e4f-2e2a-4fa9-80b1-b7f16f5dcfe4) |


---

### **7️⃣ Based on Connectivity**

| Graph Type             | Reachability Condition                         | Notes                            |
| ---------------------- | ---------------------------------------------- | -------------------------------- |
| **Connected Graph**    | Every pair of vertices has a path between them | No isolated vertices             |
| **Disconnected Graph** | Some vertices are not reachable                | Null graph is fully disconnected |
|  | ![file](https://github.com/user-attachments/assets/e10cc700-6e3e-47c8-a352-f2a4bd741552) |  |
---

### **8️⃣ Based on Cycles**

| Graph Type        | Contains Cycles? | Notes                             ||
| ----------------- | ---------------- | --------------------------------- |-|
| **Cyclic Graph**  | Yes              | Has at least one cycle            | ![cyclic](https://github.com/user-attachments/assets/67b8909b-cbd2-4a8c-8f30-f4777f88527d) |
| **Acyclic Graph** | No               | Tree is a connected acyclic graph | ![-Trees](https://github.com/user-attachments/assets/dd41345e-b22f-4f53-b53f-9fe05c429fd6) |

---

### Quick Relations 🎯

| Concept                      | Condition            |
| ---------------------------- | -------------------- |
| Trees                        | Connected + Acyclic  |
| DAG (Directed Acyclic Graph) | Directed + No cycles |
| Complete Graph Kn            | n(n−1)/2 edges       |


## **Applications of Graph Theory in Computer Science**

Graph theory is fundamental in multiple computing domains:

| Area                              | Application                                               |
| --------------------------------- | --------------------------------------------------------- |
| **Computer Networks**             | Routing and shortest path detection                       |
| **Operating Systems**             | Deadlock detection through resource allocation graphs     |
| **Social Media Analytics**        | Relationship mapping, influencer ranking                  |
| **Compiler Design**               | Control flow graphs, register allocation (graph coloring) |
| **Search Engines & Web Crawlers** | Ranking pages using link structure (PageRank)             |
| **Artificial Intelligence**       | State space graphs, A* search, decision trees             |

---

## **Important Formulas**

| Concept                                | Formula                                         |
| -------------------------------------- | ----------------------------------------------- |
| Edges in Complete Graph Kn             | n(n−1)/2                                        |
| Edges in Complete Bipartite Graph Km,n | m × n                                           |
| Degree Sum Rule                        | Sum of all vertex degrees = 2 × number of edges |
| Minimum number of vertices in Cn       | n ≥ 3                                           |

---

## **Key Observations**

* Graphs help model relationships where order or hierarchy is **not strictly linear**.
* Structures like trees, networks, and paths are special subsets or extensions of graphs.
* Graphs form the mathematical foundation for many modern algorithms.

