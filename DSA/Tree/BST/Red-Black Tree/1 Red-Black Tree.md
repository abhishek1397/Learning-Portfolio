# **Red-Black Tree**

## **Definition**

A **Red-Black Tree** is a **self-balancing Binary Search Tree (BST)** where each node has an additional color attribute (red or black). The tree maintains balance through enforced coloring rules, ensuring that its height remains **O(log n)** even in the worst case.

![Red-black-Tree-banner](https://github.com/user-attachments/assets/e15ae241-a238-4464-8a93-eb7d61241ccd)

---

## **Properties of Red-Black Tree**

A valid Red-Black Tree must satisfy the following rules:

1. **Node Color:** Every node is either **red or black**.
2. **Root Property:** The **root node is always black**.
3. **Red Property:** No red node can have a red child (no two consecutive red nodes).
4. **Black-Height Property:** Every path from a node to its descendant NIL leaves must contain the **same number of black nodes**.
5. **Leaf Property:** All **NIL (null) leaves are considered black**.

> These properties ensure that no path is more than twice as long as another, keeping the tree balanced.

![New-Project-8](https://github.com/user-attachments/assets/02cfb508-1dcd-466c-a15c-a57c31f943f5)
> The Correct Red-Black Tree in above image ensures that every path from the root to a leaf node has the same number of black nodes. In this case,​ there is one (excluding the root node).

> The Incorrect Red Black Tree does not follow the red-black properties as two red nodes are adjacent to each other. Another problem is that one of the paths to a leaf node has zero black nodes, whereas the other two contain a black node.


---

## **Why Red-Black Trees?**

Binary Search Trees can degrade to a linear chain (**O(n)** height) if unbalanced.
Red-Black Trees preserve height as:

```
h < log_2(n+1)
```

So operations always run in:

| Operation | Time Complexity |
| --------- | --------------- |
| Search    | **O(log n)**    |
| Insert    | **O(log n)**    |
| Delete    | **O(log n)**    |

---

## **Comparison with AVL Tree**

| Feature            | AVL Tree               | Red-Black Tree                   |
| ------------------ | ---------------------- | -------------------------------- |
| Balance Strictness | More strict            | Less strict                      |
| Rotations          | More frequent          | Fewer                            |
| Search Speed       | Faster                 | Slightly slower                  |
| Best Use Case      | Search-heavy workloads | Frequent insert/delete workloads |

---

## **How Balance Is Ensured**

Red-Black Trees avoid long skewed chains because any sequence of nodes cannot have more than one consecutive red node.
Example rule preventing imbalance:

> A chain of **three consecutive nodes** cannot exist without violating the red property.
<img width="1100" height="401" alt="3NodedRedBlacktree" src="https://github.com/user-attachments/assets/06b4071a-d056-4e52-9a7a-516bda46b6cb" />

---

## **Important Terminology**

* **Black Height:** Number of black nodes from a node to any leaf (including NIL).
* **Black Depth:** Number of black ancestor nodes from the root to a given node.

---

## **Basic Operations**

### **1. Insertion**

Steps:

1. Insert the key using normal BST rules.
2. Color the newly inserted node **red**.
3. Fix violations based on parent and uncle colors.

Violation Fix Cases:

| Case                           | Condition                                              | Fix |
| ------------------------------ | ------------------------------------------------------ | --- |
| **Case 1:** Uncle is **red**   | Recolor parent and uncle to black, grandparent to red  |     |
| **Case 2:** Uncle is **black** | Perform rotation(s) based on node position and recolor |     |

Sub-cases under Case 2:

* **Right child of left parent** → Left rotation (convert to straight line)
* **Left child of left parent** → Right rotation (with recoloring)
* Mirror cases apply on right side

---

### **2. Searching**

Same as BST search:

1. Start at root.
2. Compare key.
3. Move left if smaller, right if larger.
4. Stop when found or reach NIL node.

Time complexity remains **O(log n)** due to guaranteed balancing.

---

### **3. Deletion**

Steps:

1. Delete using normal BST rules.
2. If deleting a **black node**, a **double black** situation may occur → requires fixes.

Fixing deletion violations depends on **sibling color and children colors**:

| Case                                                      | Condition                                      | Fix |
| --------------------------------------------------------- | ---------------------------------------------- | --- |
| **Case 1:** Sibling is red                                | Rotate and recolor                             |     |
| **Case 2.1:** Sibling is black and both children black    | Recolor sibling and propagate                  |     |
| **Case 2.2:** Sibling is black and at least one child red | Rotate and recolor depending on near/far child |     |

---

Here is the final **clean, structured, notebook-ready version** created strictly from your provided content — no extra additions.

---

### **4 Rotation in Red-Black Tree**

Rotations are essential operations used to maintain the balanced structure of a Red-Black Tree. They ensure that none of the Red-Black properties are violated and that the height of the tree remains **O(log n)**. Two types of rotations are used:

* **Left Rotation**
* **Right Rotation**

Rotations are applied during **insertion** and **deletion** when violations occur.

---

### **1. Left Rotation**

A left rotation pivots the tree **leftward**, moving a node **down to the left** while its right child moves **up** to take its place.

#### **Steps:**

1. Set `y` as the **right child** of `x`.
2. Move `y`’s **left subtree** to become the **right subtree** of `x`.
3. Update parent pointers of both `x` and `y`.
4. Make `y` the parent of `x`.
5. Set `x` as the **left child** of `y`.
```Before Rotation:

    x                                              
     \                                             
      y                                                         
     / \                                                     
    a   b                                                     

After Left Rotation:

      y
     / \
    x   b
     \
      a
  ```

---

### **2. Right Rotation**

A right rotation is the mirror of a left rotation. Node `x` moves **down to the right**, and its left child `y` moves **up**.

#### **Steps:**

1. Set `y` as the **left child** of `x`.
2. Move `y`’s **right subtree** to become the **left subtree** of `x`.
3. Update parent pointers of both `x` and `y`.
4. Make `y` the parent of `x`.
5. Set `x` as the **right child** of `y`.

```
Befor Right Rotation:    

      x
     /
    y
   / \
  a   b

After Right Rotation:

    y
   / \
  a   x
     /
    b
```

---

## **When Are Rotations Performed?**

Rotations are used during **insertions** and **deletions** whenever any Red-Black property is violated.

---

### **A. Fixing Violations After Insertion**

During insertion, the new node is always colored **red**, which may cause rule violations.

Two main cases occur:

#### **Case 1 — Recoloring**

* If both **parent** and **uncle** are **red**, recolor:

  * Parent → black
  * Uncle → black
  * Grandparent → red
* Continue fixing from the grandparent if needed.

#### **Case 2 — Rotation + Recolor**

* If the uncle is **black**, fix with rotation depending on the position of the node:

  * **Right child of a left parent** → Left rotation
  * **Left child of a left parent** → Right rotation (after recoloring)
  * Mirror logic applies for right subtree.

---

### **B. Fixing Violations After Deletion**

Deletion can create a **double-black** situation which must be corrected.

#### Cases:

| Case                                                  | Condition                       | Action                                         |
| ----------------------------------------------------- | ------------------------------- | ---------------------------------------------- |
| **1. Sibling is Red**                                 | Parent is black or red          | Rotate and recolor                             |
| **2. Sibling is Black and both children are Black**   | Balanced but still double-black | Recolor sibling and move problem upward        |
| **3. Sibling is Black and at least one child is Red** | Can repair locally              | Rotate and recolor depending on child position |

---

### **Advantages of Red-Black Trees**

* Self-balancing structure.
* Worst-case time complexity for search, insert, and delete is **O(log n)**.
* Efficient and commonly used in real-world systems.
* Easy to maintain compared to stricter balancing trees.

---

### **Disadvantages**

* More complex than simple BST and AVL rotation logic.
* Additional overhead due to recoloring and rotation rules.

---

### **Applications**

* Maps and Sets (Java `TreeMap`, `TreeSet`, C++ `map`, `set`)
* File systems
* In-memory databases
* Graphics and game development (collision detection, pathfinding)
* Data indexing and memory allocators

---



