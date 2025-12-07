# **AVL Tree**

## **Definition**

An **AVL Tree** is a **self-balancing Binary Search Tree** in which the **height difference (Balance Factor)** between the left and right subtree of any node is:

```
-1 <= {Balance Factor} <= +1

Balance Factor = Height(left subtree) - Height(right subtree)
```

If the balance factor violates this range after insertion/deletion, the tree performs **rotations** to restore balance.

---

## **Key Properties**

* Always maintains **BST ordering**
* Height of tree always **O(log n)**
* Rebalancing is done using **rotations**
* Guarantees predictable performance

---

## **Rotations in AVL Tree**

Used to restore balance after insertion/deletion.

| Case                 | Condition                                    | Fix                                     |
| -------------------- | -------------------------------------------- | --------------------------------------- |
| **LL (Left-Left)**   | Inserted in **left subtree of left child**   | Right Rotation                          |
| **RR (Right-Right)** | Inserted in **right subtree of right child** | Left Rotation                           |
| **LR (Left-Right)**  | Inserted in **right subtree of left child**  | Left Rotation on child + Right Rotation |
| **RL (Right-Left)**  | Inserted in **left subtree of right child**  | Right Rotation on child + Left Rotation |

---

## **Operations and Complexity**

| Operation  | Method                                     | Time Complexity |
| ---------- | ------------------------------------------ | --------------- |
| **Search** | Same as BST                                | **O(log n)**    |
| **Insert** | BST insertion + rebalancing                | **O(log n)**    |
| **Delete** | BST deletion + possible multiple rotations | **O(log n)**    |

*Deletion may be more complex because it can trigger multiple balancing steps.*

---

## **Traversal**

AVL Tree follows BST traversals.
**In-order traversal always produces sorted output.**

---

## **Advantages**

* Always height-balanced → **predictable O(log n)** operations.
* Faster search performance than Red-Black Trees due to tighter balancing.
* Useful when lookups are more frequent than updates.

---

## **Disadvantages**

* More complex insertions and deletions (more rotations).
* Slightly slower updates compared to Red-Black trees due to strict balancing.
* Implementation is more complex than a simple BST.

---

## **Applications**

* Used where **fast lookup and sorted structure** are critical:

  * Databases indexing
  * File systems
  * Memory-intensive applications
  * Consistent real-time systems
* Used academically as the first example of a **self-balancing BST**.

---

## **Comparison with Red-Black Tree**

| Feature            | AVL Tree               | Red-Black Tree                |
| ------------------ | ---------------------- | ----------------------------- |
| Balance Strictness | Higher                 | Lower                         |
| Lookup             | Faster                 | Moderate                      |
| Insertion/Deletion | More rotations         | Fewer rotations               |
| Use Case           | Search-heavy workloads | Insert/delete-heavy workloads |

---


