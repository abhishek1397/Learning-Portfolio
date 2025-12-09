# **Deletion in Red-Black Tree**

Deletion in a Red-Black Tree is more complex than insertion because removing a node may violate Red-Black properties, especially the **black-height rule**.

Like insertion, deletion uses:

* **Recoloring**
* **Rotations**

However, the decision logic is based on the **sibling's color**, not the uncle’s (as in insertion).

---

## **Cases Based on Node Type**

When deleting a node, three situations exist:

1. **Node has no children** → simply remove it.
2. **Node has one child** → replace the node with its child.
3. **Node has two children** →
   * replace it with its **in-order successor** (leftmost node of right subtree)
   * delete that successor (successor will have at most one child).

After deletion, Red-Black properties may be violated, requiring correction.

---

## **Insertion vs Deletion**

| Feature           | Insertion                  | Deletion                                        |
| ----------------- | -------------------------- | ----------------------------------------------- |
| Decision based on | Uncle's color              | Sibling’s color                                 |
| Main violation    | Two consecutive red nodes  | Black-height change                             |
| Tool used         | Recolor first, then rotate | Recolor + rotation with possible multiple steps |

---

## **Main Issue After Deletion: Double Black**

When a **black node is deleted** and replaced with a black child, this creates a **double black node**.
Double black is a temporary state indicating imbalance that must be corrected.

Goal: **convert double black → normal single black**.

---

## **Deletion Algorithm (Detailed Steps)**

Let:

* **v** = node to delete
* **u** = child that replaces v
  (or **NULL**, considered black)

### **Step 1 — Standard BST Delete**

Delete v:

* If v has 0 or 1 child → remove directly
* If v has 2 children → replace with successor → delete successor

### **Step 2 — Handle Coloring Cases**

#### Case A — **Either u or v is Red**

* Replace node color with **black**
* No property violated
* **STOP**
*  ![](https://github.com/user-attachments/assets/464b82c2-fef2-48ee-b9c7-e07a86386e36)

Reason:

> Removing red does not change black height.

#### Case B — **Both u and v are Black**

This creates **double black** at u.
![](https://github.com/user-attachments/assets/303f8750-5cb2-43fc-ab50-f6b73b13c36b)

Now we must fix it.

---

## **Fixing Double Black Cases**

### **Case 1: Sibling is Black and at Least One Child is Red**

→ Perform rotation(s).
Let the red child of sibling be **r**.

| Case   | Condition                              | Operation                          |
| ------ | -------------------------------------- | ---------------------------------- |
| **LL** | s is left child & r is left child of s | Right Rotation on parent + recolor |
| **LR** | s is left child & r is right child     | Left Rotation on s → LL fix        |
| **RR** | s is right child & r is right child    | Left Rotation on parent + recolor  |
||![](https://github.com/user-attachments/assets/c5cd0348-50b1-42a8-b80e-0d7e9084585b)||
||||
| **RL** | s is right child & r is left child     | Right Rotation on s → RR fix       |
||![](https://github.com/user-attachments/assets/372700b9-ca7a-47de-925e-050561ca8f66)||


This immediately removes double black.
(These correspond to rotation patterns similar to AVL and insertion logic.)

---

### **Case 2 — Sibling s is Black and its children are both Black**

![](https://github.com/user-attachments/assets/f5002bc4-1b2b-491b-a179-8d1be2578d0d)

* Recolor sibling **s → Red**
* Move double black **up to parent**
* If parent is **red**, recolor parent black and **stop**
* Else continue fixing upwards

This case **propagates** the double black condition toward the root.

---

### **Case 3 — Sibling s is Red**

* Rotate at parent (direction depends on sibling side)
* Recolor parent and sibling (swap colors)
* Now sibling becomes black → reduced to **Case 1 or Case 2**
* Continue fixing

This case restructures the subtree to expose a black sibling.
![](https://github.com/user-attachments/assets/ba32f901-a9ae-46eb-90da-960ab89f6886)

---

### **Step 3 — If u becomes root**

* Remove double-black mark (root is always black)
* Black height reduces by 1 safely


### **Final Step**

If `u` becomes the **root**, convert it to **single black** and stop.

---


> Red-Black Trees maintain worst-case balanced height:
> O(log_2 (n+1))

---

## **Time & Space Complexity**

| Metric           | Value                   |
| ---------------- | ----------------------- |
| Time Complexity  | **O(log n)**            |
| Space Complexity | **O(n)** (tree storage) |

---
