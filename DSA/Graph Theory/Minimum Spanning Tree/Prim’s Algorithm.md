# **Prim’s Algorithm (Minimum Spanning Tree)**

---

## **Overview**

Prim’s Algorithm is a **Greedy algorithm** used to construct a **Minimum Spanning Tree (MST)** from a weighted, connected, undirected graph.

It builds the MST **incrementally**, starting from a single vertex and repeatedly selecting the **minimum-weight edge** connecting a vertex in the MST to a vertex outside it.

---

## **Concept**

Prim’s algorithm maintains two sets:

| Set            | Meaning                          |
| -------------- | -------------------------------- |
| **MST Set**    | Vertices already included in MST |
| **Fringe Set** | Vertices not yet included        |

At each step, it selects the **minimum edge** that connects a vertex in the MST to a vertex outside of it.

Such edges form what is known in graph theory as a **cut**, and the selected smallest-weight edge is called the **safe edge**.

---

## **Steps of Prim’s Algorithm**

1. **Choose an arbitrary vertex** as the starting point (commonly vertex `0`).
2. Repeat until all vertices are added to the MST:

   * Identify all edges connecting MST-included vertices to vertices outside MST.
   * Select the edge with the **minimum weight**.
   * Add this edge and its new endpoint to MST.
3. Stop once the MST contains **V − 1 edges**.

Since only edges leading **out of the current MST** are considered, **cycles can never form.**


| | |
|-|-|
| <img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/995fbc6a-fb47-4f48-8107-aa7c321252c1" />  | <img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/21065219-d4c2-47a3-b8f6-9cfee1459b1c" />|
|![Prims-Algorithm-3](https://github.com/user-attachments/assets/8651ea25-760a-457f-9168-bedc90739f93) | ![Prims-Algorithm-4](https://github.com/user-attachments/assets/74429484-d818-471e-810a-b67afa954b90) |
| ![Prims-Algorithm-5](https://github.com/user-attachments/assets/d6172ee1-324a-4ad4-b806-ed44ab8a263d) | ![Prim-Algorithm-6](https://github.com/user-attachments/assets/7566dc1c-f8a8-428b-9ef0-46590985155c) |
| ![Prims-Algorithm-7](https://github.com/user-attachments/assets/b8b583ce-edff-432b-9740-ad89744d4d1d) | ![Prims-Algorithm-8](https://github.com/user-attachments/assets/c79604f7-820f-4ede-ae6f-d015f7372658) |
|![Prims-Algorithm-9](https://github.com/user-attachments/assets/62cc69e9-03ba-490a-a19b-6696af96ffb4)  | ![Prims-Algorithm-10](https://github.com/user-attachments/assets/8c7e1409-9e24-451e-9df5-6c3fa340cd3e) |
|![Prims-Algorithm-11](https://github.com/user-attachments/assets/51353082-fb23-4cd7-9e3f-16d27dbc2014)  | ![Prims-Algorithm-12](https://github.com/user-attachments/assets/8a69a9ce-8461-4c7a-9a2e-86c7d72f62e1) |


## **Example Workflow (Conceptual)**

```
Start at node 0  
↓  
Pick the smallest connecting edge  
↓  
Add the new node to the MST  
↓  
Repeat until all nodes are included
```

---

## **Time and Space Complexity**

| Complexity Type      | Value                                                                |
| -------------------- | -------------------------------------------------------------------- |
| **Time Complexity**  | `O((E + V) * log V)` using priority queue (binary or Fibonacci heap) |
| **Space Complexity** | `O(E + V)` (for storing graph and priority queue)                    |

---

## **Advantages**

* Guarantees finding the MST for any **connected weighted graph**.
* Efficient for **dense graphs**, especially when using adjacency lists + priority queue.
* Implementation is conceptually simpler compared to some other MST approaches.

---

## **Disadvantages**

* Can be slower for extremely dense graphs as many edges may be evaluated.
* Requires a **priority queue**, increasing implementation complexity and memory usage.
* The **starting vertex may affect which MST is produced** when multiple MSTs exist.

---

## **When to Use Prim's Algorithm**

| Scenario                                 | Suitability                              |
| ---------------------------------------- | ---------------------------------------- |
| Dense graph                              | ✔ Recommended                            |
| Graph represented by adjacency list      | ✔ Efficient                              |
| Sparse graph                             | 👌 Still works but Kruskal may be faster |
| Need MST starting from a specific vertex | ✔ Useful                                 |

---


