# **HEAP DATA STRUCTURE**

### **Definition**

A **Heap** is a **complete binary tree** that satisfies the **heap property**:

* **Min-Heap:** Every parent node ≤ its children → smallest element at root.
* **Max-Heap:** Every parent node ≥ its children → largest element at root.

Because the tree is **complete**, nodes are filled **level-by-level from left to right**.

| Valid Heap | Invalid Heap |
| ----------------------------- | ----------------------------------- | 
|![Min-Max heap](https://media.geeksforgeeks.org/wp-content/uploads/20241105101737867907/min-heap-1.webp)  | ![Min-Max heap](https://media.geeksforgeeks.org/wp-content/uploads/20241105101737995053/min-heap-2.webp)          |
|![Min-Max heap](https://media.geeksforgeeks.org/wp-content/uploads/20241105101737567635/max-heap-1.webp)  | ![Min-Max heap](https://media.geeksforgeeks.org/wp-content/uploads/20241105101737719243/max-heap-2.webp)         |



### **Key Characteristics**

* Stored using **arrays** (not pointers).
* Parent and child index relationships (0-based indexing):

  * **Parent of i** → `(i - 1) / 2`
  * **Left child** → `2i + 1`
  * **Right child** → `2i + 2`

---

### **Types of Heaps**

| Type                          | Description                         | Use Case                         |
| ----------------------------- | ----------------------------------- | -------------------------------- |
| **Min-Heap**                  | Root holds minimum element          | Dijkstra, Prim’s Algorithm       |
| **Max-Heap**                  | Root holds maximum element          | Heap Sort, Scheduling            |
| **d-ary Heap**                | Node has d children                 | Faster priority queue operations |
| **Binomial / Fibonacci Heap** | Supports efficient merge operations | Advanced PQ operations           |

---

### **Basic Operations on Heap**

| Operation              | Description                                                    | Time Complexity      |
| ---------------------- | -------------------------------------------------------------- | -------------------- |
| **Insert (Push)**      | Add element at last position → restore heap via **heapify-up** | **O(log n)**         |
| **Delete Root (Pop)**  | Replace root with last element → apply **heapify-down**        | **O(log n)**         |
| **Peek / Get Min/Max** | Return root element                                            | **O(1)**             |
| **Heapify**            | Convert array into heap                                        | **O(n)** (bottom-up) |
| **Search**             | Not efficient due to no ordering (except levels)               | **O(n)**             |

---

### **Heap Construction Methods**

#### **Top-Down (Repeated Insert):**

Insert each element one-by-one → heapify up.
⏱ Complexity: **O(n log n)**

#### **Bottom-Up (Heapify):**

Convert given array into heap using repeated heapify-down from last non-leaf node.
⏱ Complexity: **O(n)** (more efficient)



