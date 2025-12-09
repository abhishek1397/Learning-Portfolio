# **Kruskal’s Algorithm (Minimum Spanning Tree)**


## **Overview**

Kruskal’s Algorithm is a **Greedy algorithm** used to construct a **Minimum Spanning Tree (MST)** from a weighted, connected, undirected graph.

An **MST** is a spanning tree that:

* Includes **all vertices**
* Contains **exactly (V − 1) edges**
* Has **no cycles**
* Has the **minimum total weight** among all possible spanning trees

Kruskal’s approach is edge-based rather than vertex-based (unlike Prim’s).

---

## **Key Idea**

The algorithm repeatedly selects the **minimum weight edge** that:

✔ Connects two **different components**
✖ Does **not** form a **cycle**

To check cycles efficiently, Kruskal’s algorithm uses the **Disjoint Set (Union-Find)** data structure.

---

## **Steps in Kruskal’s Algorithm**

1. **Sort all edges** in non-decreasing order of their weights.
2. Start with an empty MST.
3. For each edge (in sorted order):

   * Check if including it forms a **cycle**.
   * If **no cycle**, add the edge to the MST.
   * If it forms a cycle, **discard** it.
4. Stop when the MST contains **(V − 1) edges**.

|||
|-|-|
| ![Kruskals-Minimum-Spanning-Tree-MST-Algorithm-1](https://github.com/user-attachments/assets/9235a7a6-be38-4049-8a39-11fdf281b11c) | ![Kruskals-Minimum-Spanning-Tree-MST-Algorithm-2](https://github.com/user-attachments/assets/8daac1af-103f-4dc8-930a-40f8b6c5a552) |
|![Kruskals-Minimum-Spanning-Tree-MST-Algorithm-3](https://github.com/user-attachments/assets/e49d665e-90e5-4d5e-9925-8086b850b225)  | ![Kruskals-Minimum-Spanning-Tree-MST-Algorithm-4](https://github.com/user-attachments/assets/d49787f8-95b7-4c1e-8568-32f4c02a7cdf) |
| ![Kruskals-Minimum-Spanning-Tree-MST-Algorithm-5](https://github.com/user-attachments/assets/7634bdb1-cc8b-45e8-8517-8f5a7444b393) | ![Kruskals-Minimum-Spanning-Tree-MST-Algorithm-6](https://github.com/user-attachments/assets/c6221b88-f0d3-4717-8f65-520126496974) |
| ![Kruskals-Minimum-Spanning-Tree-MST-Algorithm-7](https://github.com/user-attachments/assets/3f1742a4-db00-4536-9bfd-a53953b9bdce) | ![Kruskals-Minimum-Spanning-Tree-MST-Algorithm-8](https://github.com/user-attachments/assets/9db557a2-49c8-4d38-bbe5-4a78641ed557) |
| ![Kruskals-Minimum-Spanning-Tree-MST-Algorithm-9](https://github.com/user-attachments/assets/739b2bd7-8a80-494e-9751-cbc9ecfe4ead) | ![Kruskals-Minimum-Spanning-Tree-MST-Algorithm-10](https://github.com/user-attachments/assets/7c85bac7-68a0-4074-b16e-0eac5ce8f253) |

---

## **Example Logic Summary**

```
Sorted edges → Pick smallest → Add if no cycle → Repeat until (V − 1) edges included
```

---

## **Time Complexity**

| Operation              | Cost                                                   |
| ---------------------- | ------------------------------------------------------ |
| Sorting edges          | `O(E * logE)`                                          |
| Union-Find operations  | `O(E * logV)` (optimized with rank + path compression) |
| **Overall Complexity** | `O(E * logE)` or `O(E * logV)`                         |

Since `E ≤ V²`, `logE ≈ logV`, so the expressions are equivalent.

---

## **Space Complexity**

* **`O(V + E)`**

  * Space for storing edges and the disjoint set structure.

---

## **Why Disjoint Set is Needed**

It allows:

| Operation       | Purpose                                       |
| --------------- | --------------------------------------------- |
| **Find(x)**     | Determine which component vertex belongs to   |
| **Union(x, y)** | Merge two components when adding a valid edge |

This ensures cycle detection happens efficiently.

---

## **Characteristics of Kruskal’s Algorithm**

| Feature             | Behavior                                                   |
| ------------------- | ---------------------------------------------------------- |
| Type                | Greedy Algorithm                                           |
| Works on            | Connected, undirected, weighted graphs                     |
| Order of processing | Edge-based                                                 |
| Result              | One MST (or multiple possible MSTs if equal weights exist) |

---

## **Advantages**

* Works well for **sparse graphs** (`E << V²`).
* Simple concept: sort edges + union-find.
* Efficient when graph is stored as an **edge list**.

---

## **Disadvantages**

* Sorting all edges may be expensive for **dense graphs** (`E ≈ V²`).
* Requires additional structure (**Union-Find**) for cycle detection.
* Not suitable for **dynamic graphs** where edges frequently change (sorting must be redone).

---

## **Use Cases**

| Application Area                      | Usage                                    |
| ------------------------------------- | ---------------------------------------- |
| Network design (telecom, power grids) | Minimize laying cost                     |
| Clustering algorithms                 | Building minimum inter-cluster links     |
| Image segmentation                    | Region grouping based on similarity      |
| Road/transport design                 | Minimizing building and maintenance cost |

---

