# **Insertion in Red-Black Tree**

Insertion in a Red-Black Tree involves two balancing mechanisms:

* **Recoloring**
* **Rotation**

Unlike AVL trees (where rotations are always used to fix imbalance), Red-Black Trees **attempt recoloring first**, and only perform rotations if recoloring cannot restore properties.

---

## **Rules to Remember**

* Newly inserted nodes are always colored **RED**.
* The color of **NULL (leaf) nodes is BLACK**.
* If the inserted node becomes the **root**, its color must be changed to **BLACK**.

---

## **Balancing Logic After Insertion**

Once the node is inserted using standard BST rules and colored **RED**, violations may occur if the **parent is also RED** (because Red-Black Trees do not allow two consecutive red nodes).

The next step depends on the **uncle’s color**:

---

### **Case 1 — Uncle is RED → Recoloring**

If the parent and uncle are both red:

* Change **parent color → BLACK**
* Change **uncle color → BLACK**
* Change **grandparent color → RED**
* Move upward and continue checking from the **grandparent**.

> If the grandparent becomes the root, it must remain **BLACK**.

---

### **Case 2 — Uncle is BLACK → Rotation + Recoloring**

If the uncle is black, one of the four rotation cases applies (similar to AVL tree patterns):

| Case Type            | When It Happens                                          | Fix                            |
| -------------------- | -------------------------------------------------------- | ------------------------------ |
| **Left-Left (LL)**   | Parent is left child, new node is left child of parent   | Right Rotation                 |
| **Left-Right (LR)**  | Parent is left child, new node is right child of parent  | Left Rotation → Right Rotation |
| **Right-Right (RR)** | Parent is right child, new node is right child of parent | Left Rotation                  |
| **Right-Left (RL)**  | Parent is right child, new node is left child of parent  | Right Rotation → Left Rotation |

#### **Recoloring Rule After Rotation:**

| Rotation Case | Swap Colors Between         |
| ------------- | --------------------------- |
| **LL and RR** | Parent ↔ Grandparent        |
| **LR and RL** | Inserted Node ↔ Grandparent |

---

## **Algorithm (Summary)**

Let **x** be the newly inserted node:

1. Insert using standard BST logic.
2. Color the inserted node **RED**.
3. If `x` is root → color it **BLACK**, stop.
4. While parent is RED:

   * If **uncle is RED** → recolor parent + uncle → grandparent becomes new `x`.
   * Else (**uncle BLACK**) → perform appropriate rotation (LL, LR, RR, RL) and recolor.
5. Ensure root is **BLACK**.

---

## **Time & Space Complexity**

| Operation | Complexity   |
| --------- | ------------ |
| Time      | **O(log n)** |
| Space     | **O(n)**     |

---

