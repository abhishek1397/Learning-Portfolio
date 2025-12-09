# **Dijkstra’s Algorithm**

---

## **Purpose**

Dijkstra’s Algorithm is used to find the **shortest path from a source vertex** to all other vertices in a **weighted graph** where:

* All edges have **non-negative weights**
* The graph may be **undirected or directed**

It is widely used in real-world systems such as navigation routing, network paths, and optimization problems.

---

## **Why Not BFS?**

BFS only works efficiently when all edges have **equal weight**, because it explores level-by-level.
When edges have different weights, BFS may discover a path early that is not the shortest — requiring repeated updates.
Dijkstra solves this by always expanding the currently **minimum cost path first**.

---

## **Core Idea**

It uses:

* A **distance array** to track the shortest discovered distance for each node.
* A **priority queue (min-heap)** to always process the vertex with the smallest tentative distance next.

Once a node is removed from the priority queue with the smallest known distance, that distance is considered **final**.

---

## **Algorithm Workflow Undirected**

1. Initialize a distance array where all values are set to **∞** (infinity).
2. Set the source vertex distance to **0**.
3. Insert the source into a **priority queue**.
4. While the queue is not empty:

   * Extract the vertex with the **minimum distance**.
   * Skip processing if the popped distance is no longer current.
   * Relax its edges:

     * If a shorter path to a neighbor exists via the current node, update the distance and push it into the priority queue.
5. Continue until all reachable nodes are processed.
6. The final distance array contains the shortest distances from the source to all nodes.


||
|-|
| ![file1](https://github.com/user-attachments/assets/335e610e-8550-41a3-855a-8aedd87814d2) |
| ![file2](https://github.com/user-attachments/assets/78ef2523-3f79-4a90-a135-e91b31b52211) |
| ![file3](https://github.com/user-attachments/assets/2b7cb275-6aae-478a-b50c-eb634bf076e5) |
| ![file4](https://github.com/user-attachments/assets/f7d0bd4a-a7b1-4fa1-ba2a-a9c511d48caf) |
| ![file5](https://github.com/user-attachments/assets/bb4d2e97-1a39-4309-988a-6b23e84950c8) |
| ![file6](https://github.com/user-attachments/assets/31567f18-0134-4a38-bfaa-a1ccba077d33) |
| ![file7](https://github.com/user-attachments/assets/a53c864a-fcbf-41ec-8217-1dd5b1788813) |



## **Example Output Interpretation**

If the final shortest-path array is:
<img width="400" height="324" alt="image" src="https://github.com/user-attachments/assets/16bec5ef-a001-440c-9c74-226d0ba9ff31" />

```
[0, 4, 7, 9, 10]
```

It means:

| Vertex | Shortest Distance from Source |
| ------ | ----------------------------- |
| 0      | 0                             |
| 1      | 4                             |
| 2      | 7                             |
| 3      | 9                             |
| 4      | 10                            |

---

## **Key Behavior of Priority Queue**

* Ensures the algorithm always expands the **currently shortest known path**.
* Prevents unnecessary exploration of longer paths first.
* Guarantees each node is finalized once.



---

## **Important Constraint**

Dijkstra **does not work with negative edge weights**.

### Reason:

The algorithm assumes that once a vertex is popped from the priority queue, the shortest path to it is final.
Negative edges can later create a shorter path to an already finalized node, making results invalid.

Algorithms like **Bellman-Ford** or **Floyd-Warshall** handle negative weights — Dijkstra does not.

---

## **Time Complexity**

| Operation Source                   | Complexity          |
| ---------------------------------- | ------------------- |
| Main execution with priority queue | `O((V + E) * logV)` |

* Efficient for large sparse graphs.

---

## **Space Complexity**

```
O(V + E)
```

Used by:

* The adjacency list
* Distance array
* Priority queue

---

## **Applications**

| Domain            | Use Case                          |
| ----------------- | --------------------------------- |
| GPS & Navigation  | Shortest driving route            |
| Networking        | Routing protocols (e.g., OSPF)    |
| Operating Systems | Shortest job/task scheduling      |
| AI & Search       | Pathfinding in games and robotics |

---

## **Characteristics Summary**

| Feature              | Description                             |
| -------------------- | --------------------------------------- |
| Algorithm Type       | Greedy                                  |
| Works On             | Weighted graphs without negative edges  |
| Data Structures Used | Priority queue + distance array         |
| Result               | Shortest path tree from a single source |

---

