# **M-Way Search Tree**

### **Definition**

An **M-Way Search Tree** (also called a **Multi-Way Search Tree of order m**) is a generalization of a Binary Search Tree (BST) in which each node may contain **multiple keys** and can have **up to m child pointers**.
It reduces tree height by increasing branching, improving search performance for large datasets.


### **Node Structure and Constraints**

For a tree of order **m**, each node satisfies:

* Maximum **m children**
* Maximum **m − 1 keys**
* Minimum **1 key** (for non-root nodes; depends on implementation)
* Keys are stored in **sorted ascending order**
* Each key divides child pointers into ordered ranges

<img width="1355" height="736" alt="image" src="https://github.com/user-attachments/assets/c5a28cc6-6d4b-41d9-afcd-bf882ea8e273" />

---

<img width="1353" height="705" alt="image" src="https://github.com/user-attachments/assets/18d208ca-a545-4bc8-9e72-3085c3b62f4f" />

If a node contains keys: ``` [K1, K2, ..., K(k-1)] ```
and children: ```[C1, C2, ..., Ck]```

then the ordering rule must hold:

* All keys in subtree `C1` are **less than K1**
* For every `i` between `2` and `k-1`, all keys in subtree `Ci` are **greater than Ki-1 and less than Ki**
* All keys in subtree `Ck` are **greater than K(k-1)**

This rule ensures correct ordered searching.

### **Properties**

* Nodes may store multiple keys, meaning each node forms multiple comparison points.
* Searching inside a node involves comparing the target with stored sorted keys.
* Traversal continues through the correct child pointer based on comparisons.
* Logical ordering is maintained similar to a BST, but with multiple branching options.


### **Height and Efficiency**

Height comparison for storing **N keys**:

<img width="950" height="550" alt="image" src="https://github.com/user-attachments/assets/215a59b2-9d0a-4a26-a06e-681c1371cd24" />

```
Binary Search Tree:    O( log_2(N) )
M-Way Search Tree:     O( log_m(N) )
```

A larger branching factor reduces height, making searches faster—especially important when mapping nodes to disk blocks or memory pages.


### **Limitations**

* No automatic balancing in the basic form.
* Poor input sequences can produce **skewed trees**, increasing height to:

```
O(N)
```

* Additional balancing logic is required in practical systems.


### **Relation to Balanced Multi-Way Structures**

Balanced structures derived from M-Way Search Trees:

| Tree Type   | Derived From   | Balancing Strategy                                 | Common Usage                  |
| ----------- | -------------- | -------------------------------------------------- | ----------------------------- |
| **B-Tree**  | M-Way Tree     | Height-balanced; keys stored at all internal nodes | Filesystems, indexing         |
| **B⁺-Tree** | B-Tree         | All keys stored in leaf nodes; leaves linked       | Databases (MySQL, PostgreSQL) |
| **B*-Tree** | B-Tree Variant | Higher node utilization; delayed splitting         | Disk-based storage systems    |


These variants maintain order while guaranteeing stable performance for insertion, deletion, and searching.

---

# **Insertion in an M-Way Search Tree**

Insertion follows the same traversal logic used during searching. The element must be placed in the correct sorted position within a node, ensuring that no node exceeds the allowed maximum of:

```
m − 1 keys  and  m children
```

*   **General Rule:** Insertion begins by searching for the correct sorted position for the new key.
  
*   **Scenario 1: Node has space (keys < m-1)**
    *   The new key is inserted directly into the node in its correct sorted position.
*   **Scenario 2: Node is full**
    *   In a basic M-Way tree, a new child node is created to store the key.
    *   *Note:* Unlike B-Trees, a basic M-Way tree does not enforce automatic node splitting or balancing.
      
*   **Key Observations**
  * Insertions may cause tree growth in width rather than height.
  * Basic m-way trees **do not enforce balancing**, so the height may degrade over time.
  * Only balanced extensions (B-Tree, B⁺-Tree, B*-Tree) handle automatic splitting with height control.

---

# **Deletion in an M-Way Search Tree**

Deletion also begins with searching for the target key. Once located, removal depends on whether the node has children.

Deletion requires finding the key and then removing it based on the node's structure.
*   **Case 1: Key is in a Leaf**
    *   Simply remove the key.
*   **Case 2: Key has a Left Subtree**
    *   Replace the target key with the **largest key** from its left subtree, then recursively delete that replacement key from its original position.
*   **Case 3: Key has a Right Subtree**
    *   Replace the target key with the **smallest key** from its right subtree, then recursively delete the replacement.
*   **Case 4: Key has Both Subtrees**
    *   You may choose either strategy (largest of left or smallest of right).
  
*   **Post-Deletion:** Restructuring (shifting keys, merging nodes) may be required to maintain key counts and pointer integrity, though this does not guarantee global balancing.


Tree restructuring may involve:

* **Borrowing keys from siblings (shifting)**
* **Merging nodes**
* **Promoting or demoting keys**

This ensures node integrity but does **not guarantee balancing**, unlike B-Trees.

---

# **Searching in an M-Way Search Tree**

Searching in an m-Way Search Tree follows the same conceptual approach as searching in a Binary Search Tree, but with multiple comparison points in each node instead of just one. The search algorithm uses the **sorted order of keys** within each node to determine which child pointer to follow.

|||
|--|--|
|The search complexity is proportional to the tree height:|``` Time complexity: O(h) ```|
|where `h` ideally remains close to:|```log_m(n + 1)```|

*   **Logic:** Searching follows the same concept as a BST but involves multiple comparison points within a single node.
*   **Procedure:**
    1.  Compare the target value with the sorted keys inside the current node.
    2.  If the target matches a key, the search is successful.
    3.  If not, determine the correct range (e.g., target < $K_1$, or $K_{i-1} < \text{target} < K_i$).
    4.  Traverse the specific child pointer corresponding to that range.
    5.  Repeat until the key is found or a NULL pointer is reached.
*   **Efficiency:** Because nodes have more branches, the tree is shorter than a BST. Searching involves more comparisons *inside* a node but traverses fewer levels overall.




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
