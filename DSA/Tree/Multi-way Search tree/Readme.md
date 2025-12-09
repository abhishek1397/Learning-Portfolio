# **M-Way Search Tree**

<img width="950" height="550" alt="5-way-search-tree" src="https://github.com/user-attachments/assets/d79fd68e-9908-4297-bb66-efc7807b3d7c" />

## **Definition**

An **M-Way Search Tree** (also called a **Multi-Way Search Tree of order m**) is a generalization of a Binary Search Tree (BST) in which each node may contain **multiple keys** and can have **up to m child pointers**.
It reduces tree height by increasing branching, improving search performance for large datasets.

---

## **Node Structure and Constraints**

For a tree of order **m**, each node satisfies:

* Maximum **m children**
* Maximum **m − 1 keys**
* Minimum **1 key** (for non-root nodes; depends on implementation)
* Keys are stored in **sorted ascending order**
* Each key divides child pointers into ordered ranges

If a node contains keys:

```
[K1, K2, ..., K(k-1)]
```

and children:

```
[C1, C2, ..., Ck]
```

then the ordering rule must hold:

* All keys in subtree `C1` are **less than K1**
* For every `i` between `2` and `k-1`, all keys in subtree `Ci` are **greater than Ki-1 and less than Ki**
* All keys in subtree `Ck` are **greater than K(k-1)**

This rule ensures correct ordered searching.

---

## **Properties**

* Nodes may store multiple keys, meaning each node forms multiple comparison points.
* Searching inside a node involves comparing the target with stored sorted keys.
* Traversal continues through the correct child pointer based on comparisons.
* Logical ordering is maintained similar to a BST, but with multiple branching options.



## **Height and Efficiency**

Height comparison for storing **N keys**:

```
Binary Search Tree:    O(log base 2 of N)
M-Way Search Tree:     O(log base m of N)
```

A larger branching factor reduces height, making searches faster—especially important when mapping nodes to disk blocks or memory pages.

---


## **Limitations**

* No automatic balancing in the basic form.
* Poor input sequences can produce **skewed trees**, increasing height to:

```
O(N)
```

* Additional balancing logic is required in practical systems.

---

## **Relation to Balanced Multi-Way Structures**

Balanced structures derived from M-Way Search Trees:

| Structure   | Characteristic                                                     |
| ----------- | ------------------------------------------------------------------ |
| **B-Tree**  | Self-balancing; all leaves at same depth                           |
| **B⁺-Tree** | Actual data stored only in leaves; leaves linked for range queries |
| **B*-Tree** | Improves node-space utilization and reduces frequency of splits    |

These variants maintain order while guaranteeing stable performance for insertion, deletion, and searching.

---

# **Insertion and Deletion in an M-Way Search Tree**


## **Insertion in an M-Way Search Tree**

Insertion follows the same traversal logic used during searching. The element must be placed in the correct sorted position within a node, ensuring that no node exceeds the allowed maximum of:

```
m − 1 keys  and  m children
```

### **General Rules**

* Insertion always begins by searching for the correct position of the new key.
* Keys inside a node remain **sorted in ascending order**.
* If the node has space (less than `m−1 keys`), the new key is inserted in sorted order.
* If the node is full, a **new child node must be created** (in simple m-way trees) or the node may be split depending on tree variant.

### **Insertion Process**

1. **Search for the key’s correct position**

   * Follow subtree pointers based on the key range logic.
   * Continue until a `NULL` child pointer is reached.

2. **Check node capacity**

   * If the node contains fewer than `m−1 keys`:

     * Insert the key into the node in sorted position.
   * If the node is already full:

     * Create a new child node and insert the key there.
     * (Balanced m-way variants like B-Trees perform node splitting, but a basic m-way tree does not enforce balancing.)

### **Example Behavior**

* Inserting `6` into a 5-way search tree:

  * Search continues until falling off at the child pointer of node `[7,12]`.
  * Since the node still has fewer than 4 keys (limit for 5-way), `6` is inserted in sorted order → `[6,7,12]`.

* Inserting `146` into a full node `[148,151,172,186]`:

  * Since the node already contains the maximum number of keys, a **new child node is created** to store `146`.

### **Key Observations**

* Insertions may cause tree growth in width rather than height.
* Basic m-way trees **do not enforce balancing**, so the height may degrade over time.
* Only balanced extensions (B-Tree, B⁺-Tree, B*-Tree) handle automatic splitting with height control.

---

## **Deletion in an M-Way Search Tree**

Deletion also begins with searching for the target key. Once located, removal depends on whether the node has children.

Let `K` be the key to delete.

### **Cases for Deletion**

#### **Case 1 — Leaf Key (Ai = NULL and Aj = NULL)**

* The key exists in a leaf node.
* It is simply removed.
* Example: Deleting `151` from `[148,151,172,186]` → resulting `[148,172,186]`.

#### **Case 2 — Key Has Left Subtree (Ai ≠ NULL, Aj = NULL)**

* Replace the key with the **largest key** from its left subtree.
* Delete that replacement key recursively.
* Example: Deleting `12` from `[7,12]`:

  * Largest key in left subtree is `10`
  * Replace → `[7,10]`
  * Then delete original `10` from its leaf position.

#### **Case 3 — Key Has Right Subtree (Ai = NULL, Aj ≠ NULL)**

* Replace the key with the **smallest key** from its right subtree.
* Delete the replacement key recursively.
* Example: Deleting `262`:

  * Smallest value from right child is `272`
  * Replace `262` with `272`
  * Then delete `272` from its original node.

#### **Case 4 — Key Has Both Left and Right Subtrees (Ai ≠ NULL and Aj ≠ NULL)**

* Either replacement strategy can be chosen:

  * **Largest key in left subtree**, or
  * **Smallest key in right subtree**
* Continue deletion recursively on the chosen replacement key.

### **Post-Deletion Rearrangement**

After deletion, restructuring may be needed to avoid:

* Nodes having too few keys
* Missing pointers
* Violations of sequential key storage

Tree restructuring may involve:

* **Borrowing keys from siblings (shifting)**
* **Merging nodes**
* **Promoting or demoting keys**

This ensures node integrity but does **not guarantee balancing**, unlike B-Trees.

---

# **Searching in an M-Way Search Tree**

---

Searching in an m-Way Search Tree follows the same conceptual approach as searching in a Binary Search Tree, but with multiple comparison points in each node instead of just one. The search algorithm uses the **sorted order of keys** within each node to determine which child pointer to follow.

The search complexity is proportional to the tree height:

```
Time complexity: O(h)
```

where `h` ideally remains close to:

```
log base m of (n + 1)
```

---

## **Search Procedure**

To search for a value `K` in an m-Way Search Tree:

1. **Start at the Root Node**

   * Compare `K` with keys stored inside the current node.

2. **Key Comparison Inside the Node**

   * Since the keys are sorted, the search checks whether:

     * `K` matches one of the keys (search successful), or
     * `K` lies between two keys.

3. **Decide Which Child Pointer to Follow**

   * If `K` is smaller than the first key, traverse the **first child**.
   * If `K` is greater than the last key, traverse the **last child**.
   * Otherwise, locate the interval where:

   ```
   Ki-1 < K < Ki
   ```

   and traverse the corresponding child.

4. **Repeat the Process**

   * Continue recursively until:

     * The key is found → **successful search**
     * A `NULL` pointer is reached → **key does not exist in the tree**

---

## **Example**

Searching for `77` in a **5-Way Search Tree**:

* Start at the root.
* Since:

```
77 > 76 > 44 > 18
```

select the **4th child**.

* In that node, `77 < 80`, so move to the **1st child**.
* The leaf node contains `77`, so the search succeeds.

---

## **Search Result Conditions**

| Condition                          | Meaning                     |
| ---------------------------------- | --------------------------- |
| Key found inside a node            | Search successful           |
| Traversal ends at a non-NULL child | Continue search             |
| Traversal ends at a NULL pointer   | Key not present in the tree |

---

## **Important Notes**

* The efficiency of the search depends on the **height of the tree**, which is impacted by the order `m`.
* Increasing `m` **reduces the height**, leading to fewer comparisons and faster search, especially for large datasets.
* Unlike BSTs, searching inside an m-way node may involve **multiple comparisons per level**, but fewer levels overall.

---

## **Advantages of Search in M-Way Trees**

* Reduced height compared to BSTs.
* Optimized for secondary storage where each node corresponds to a disk block.
* Efficient for large dataset indexing.

---

## **Limitations**

* Since a standard m-Way Search Tree lacks automatic balancing, poor insertion sequences may create long, unbalanced paths, degrading worst-case performance to:

```
O(n)
```

* Balanced variants (B-Tree, B⁺-Tree, B*-Tree) overcome this limitation.

---


## **Important Notes**

* Basic m-way trees are **not self-balancing**.
* Performance depends heavily on insertion/deletion order.
* Worst-case height may degrade to:

```
Height = n   (degenerate form)
```

* Optimized variants such as **B-Tree, B⁺-Tree, and B*-Tree** enforce balancing rules and are used in:

  * Databases
  * File systems
  * Disk indexing
  * Secondary storage search systems

---
