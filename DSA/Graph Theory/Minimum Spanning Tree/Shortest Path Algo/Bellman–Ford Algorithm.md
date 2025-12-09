# **Bellman–Ford Algorithm**

---

## **Purpose**

The **Bellman–Ford algorithm** is used to compute the **Single Source Shortest Path (SSSP)** in a weighted graph (directed or undirected) that may contain **negative edge weights**.
It is also capable of detecting **negative weight cycles**, a limitation of Dijkstra’s algorithm.

---

## **Key Output Conditions**

| Situation                      | Output                         |
| ------------------------------ | ------------------------------ |
| Graph has valid shortest paths | Return shortest distance array |
| Vertex unreachable from source | Mark distance as `∞`           |
| Negative weight cycle exists   | Return `-1`                    |

---

## **Why Bellman–Ford?**

Unlike Dijkstra’s algorithm, Bellman–Ford does **not assume finality** of a shortest distance once a node is processed.
It continues relaxing edges multiple times, allowing it to correct distance estimates even when negative edges are involved.

<img width="451" height="400" alt="image" src="https://github.com/user-attachments/assets/7372e8e5-aa5e-47f3-bb72-8c2e93ed5a97" />

---

## **Core Concept: Edge Relaxation**

For every edge `(u → v)` with weight `w`:

```
If distance[v] > distance[u] + w
      Update: distance[v] = distance[u] + w
```

Relaxation gradually improves estimates of shortest distances.

---

## **Algorithm Logic**

1. Initialize distances:

   * `dist[source] = 0`
   * All other vertices: `∞`

2. Repeat the relaxation process for all edges **exactly (V − 1) times**, where `V` is number of vertices.

3. Perform one additional relaxation (the `Vth iteration`) to detect negative cycles:

   * If any distance improves again → **negative cycle detected** → return `-1`.




---

## **Why (V − 1) Relaxations?**

<img width="579" height="306" alt="image" src="https://github.com/user-attachments/assets/b2a27a13-7cce-4e0c-8b52-5b11a908114e" />

A shortest path in a graph without cycles can contain at most:

```
V − 1 edges
```

Therefore, relaxing edges `V − 1` times guarantees that all shortest paths have been considered.

Further improvement after `(V − 1)` iterations indicates a cycle contributing negative weight.

---

## **Negative Weight Cycle**

A **negative weight cycle** is a cycle where the total sum of edge weights is negative:

```
w1 + w2 + ... + wk < 0
```

If reachable from the source, shortest paths are undefined because traversing the cycle repeatedly reduces cost infinitely.

Bellman–Ford is the standard method to **detect** such cycles.


||
|-|
| ![BellmanFord-Algorithm-1](https://github.com/user-attachments/assets/d856e87c-4d46-4170-9b65-7e08125e7f1d) |
| ![BellmanFord-Algorithm-2](https://github.com/user-attachments/assets/9f5d616f-38b4-4db6-99e8-301c95f46dde) |
| ![BellmanFord-Algorithm-3](https://github.com/user-attachments/assets/03e204d3-badc-4297-87c7-54d562123e77) |
| ![BellmanFord-Algorithm-4](https://github.com/user-attachments/assets/77af6eb9-162f-4c82-a68c-b72ca250bac5) |
| ![BellmanFord-Algorithm-5](https://github.com/user-attachments/assets/08ef3d57-c8a2-41e0-ae15-5753b74023ec) |
| ![BellmanFord-Algorithm-6](https://github.com/user-attachments/assets/86fdc36e-1ab6-475f-b602-3f9c167bc428) |


---

## **Why Dijkstra Fails Here**

Dijkstra finalizes a node's shortest distance prematurely.
If later relaxation through a negative edge yields a shorter path, Dijkstra does not reconsider it.

Bellman–Ford resolves this by **revisiting** and **relaxing edges multiple times**.

---

## **Time and Space Complexity**

| Metric | Complexity |
| ------ | ---------- |
| Time   | `O(V × E)` |
| Space  | `O(V)`     |

Works well on sparse graphs; inefficient for dense graphs.

---

## **Suitable For**

✔ Graphs with **negative edge weights**
✔ Graphs requiring **negative cycle detection**
✔ SSSP problems where accuracy > performance

---

## **Applications**

| Area                  | Use Case                                               |
| --------------------- | ------------------------------------------------------ |
| Routing protocols     | Used in distance-vector routing algorithms (e.g., RIP) |
| Financial systems     | Arbitrage detection (negative cycle = profit loop)     |
| Graph analysis        | Networks with gain/loss weights                        |
| Optimization problems | Cost-based path planning where costs may be negative   |

---

## **Summary**

* Bellman–Ford is a reliable SSSP algorithm even for graphs containing **negative weights**.
* Requires `V − 1` relaxation phases plus one additional phase for **negative cycle detection**.
* Slower than Dijkstra, but far more flexible and powerful in graphs with negative weights.

---

