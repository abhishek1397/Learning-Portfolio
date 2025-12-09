# **Shortest Path in Directed Graph Using Dijkstra’s Algorithm**

---

## **Purpose**

Dijkstra’s algorithm is used to compute the **shortest distance and corresponding shortest path** from a **single source vertex** to all other vertices in a **directed, weighted graph** where all edge weights are **non-negative**.

Since the graph is directed, edges represent **one-way connections**, meaning traversal is allowed only in the direction of the edge.

---

## **Key Characteristics**

| Property             | Value                                 |
| -------------------- | ------------------------------------- |
| Graph Type           | Directed and Weighted                 |
| Edge Weights Allowed | Only non-negative                     |
| Output               | Minimum distance + shortest path tree |
| Algorithm Type       | Greedy                                |
| Optimal For          | Sparse and large graphs               |

---

## **Why Dijkstra Works Here**

Because directed graphs still allow well-defined edge relaxation and the algorithm always processes the **smallest tentative distance first**, ensuring correctness as long as weights are non-negative.

Edges’ directions only affect which neighbors are processed — traversal cannot move backward unless an explicit directed edge exists.

---

## **Concept of Relaxation**

For every reachable adjacent vertex `v` of the current vertex `u`:

```
new_distance = distance[u] + weight(u → v)
```

If:

```
new_distance < existing distance[v]
```

Then update:

```
distance[v] = new_distance
parent[v] = u   (store predecessor to reconstruct the path)
```

This allows the algorithm not only to compute distances, but also the **shortest path tree**.

---

## **Working Steps**

1. **Initialize**

   * Set all distances to **∞ (infinity)**.
   * Set the source vertex distance to `0`.
   * Mark all vertices as **unvisited**.

2. **Pick the Current Vertex**

   * Select the unvisited vertex with the **smallest distance value**.

3. **Relax Adjacent Directed Edges**

   * For each outgoing edge from the current vertex, compute tentative distances.
   * Update if a shorter path is discovered.

4. **Mark Visited**

   * After processing its outgoing edges, mark the vertex as permanently visited (final shortest distance confirmed).

5. **Repeat**

   * Continue until all vertices are visited or no additional vertices are reachable.

---

## **Path Reconstruction**

Since the algorithm records the **parent (predecessor) of each vertex**, the shortest path to any vertex can be obtained by:

```
Start at destination → follow stored parents → reverse the sequence
```

Example:

```
Path: target → 5 → 2 → 0 → source
(reverse)
Result: source → 0 → 2 → 5 → target
```

---

## **Complexity Analysis**

| Case                                | Complexity          |
| ----------------------------------- | ------------------- |
| Using Min Heap / Priority Queue     | `O((V + E) * logV)` |
| Space Used (distance + parent + PQ) | `O(V + E)`          |

Works efficiently for large directed graphs.

---

## **When It Fails**

Dijkstra **cannot handle negative edge weights** because once a vertex is marked visited, the algorithm assumes its shortest distance will never change — negative edges can invalidate this assumption.

For directed graphs with negative weights, use:

✔ Bellman–Ford Algorithm
✔ Floyd–Warshall (for all-pairs shortest paths)

---

## **Applications**

| Area                 | Use Case                                              |
| -------------------- | ----------------------------------------------------- |
| Navigation Systems   | Routing in one-way roadway networks                   |
| Internet Routing     | Packet forwarding where links have direction and cost |
| Logistics & Delivery | Directed network supply chains                        |
| Game AI              | Directed weighted movement paths and constraints      |

---

## **Summary**

* Dijkstra’s algorithm finds the shortest distance and shortest path in a weighted **directed graph** using a greedy approach.
* Works only if **all weights are non-negative**.
* Uses priority queue and relaxation to iteratively refine shortest paths.

---

