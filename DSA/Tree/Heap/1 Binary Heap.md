# **BINARY HEAP DATA STRUCTURE**


## **Definition**

A **Binary Heap** is a **complete binary tree** that satisfies the **heap property**:

* **Min-Heap:** Every parent node ≤ its children → smallest element at root.
* **Max-Heap:** Every parent node ≥ its children → largest element at root.

Because the tree is **complete**, nodes are filled **level-by-level from left to right**.
 
![Heap](https://media.geeksforgeeks.org/wp-content/uploads/20250324101433667420/Representation-of-a-Binary-Heap.webp)
 
## **Key Characteristics**

* Stored using **arrays** (not pointers).
* Parent and child index relationships (0-based indexing):

  * **Parent of i** → `(i - 1) / 2`
  * **Left child** → `2i + 1`
  * **Right child** → `2i + 2`


---

## **Types of Heaps**

| Type                          | Description                         | Use Case                         |
| ----------------------------- | ----------------------------------- | -------------------------------- |
| **Min-Heap**                  | Root holds minimum element          | Dijkstra, Prim’s Algorithm       |
| **Max-Heap**                  | Root holds maximum element          | Heap Sort, Scheduling            |
| **d-ary Heap**                | Node has d children                 | Faster priority queue operations |
| **Binomial / Fibonacci Heap** | Supports efficient merge operations | Advanced PQ operations           |

| Valid Heap | Invalid Heap |
| ----------------------------- | ----------------------------------- | 
|![Min-Max heap](https://media.geeksforgeeks.org/wp-content/uploads/20241105101737867907/min-heap-1.webp)  | ![Min-Max heap](https://media.geeksforgeeks.org/wp-content/uploads/20241105101737995053/min-heap-2.webp)          |
|![Min-Max heap](https://media.geeksforgeeks.org/wp-content/uploads/20241105101737567635/max-heap-1.webp)  | ![Min-Max heap](https://media.geeksforgeeks.org/wp-content/uploads/20241105101737719243/max-heap-2.webp)         |


---

## **Basic Operations on Heap**

| Operation              | Description                                                    | Time Complexity      |
| ---------------------- | -------------------------------------------------------------- | -------------------- |
| **Insert (Push)**      | Add element at last position → restore heap via **heapify-up** | **O(log n)**         |
| **Delete Root (Pop)**  | Replace root with last element → apply **heapify-down**        | **O(log n)**         |
| **Peek / Get Min/Max** | Return root element                                            | **O(1)**             |
| **Heapify**            | Convert array into heap                                        | **O(n)** (bottom-up) |
| **Search**             | Not efficient due to no ordering (except levels)               | **O(n)**             |

| Operation on | Heap | 
|--------------|------|
|![Min-Max heap](https://github.com/user-attachments/assets/e38da509-6382-43a4-8875-4e03ad3a16b4)  | ![Min-Max heap](https://github.com/user-attachments/assets/14590465-f8b8-425c-8c7a-bcab3a20833c) |
|![Min-Max heap](https://github.com/user-attachments/assets/cfddef3d-fba4-4133-8b4f-d050f9d594fe) | ![Min-Max heap](https://github.com/user-attachments/assets/36bac48a-4b2a-424c-a6fa-befa565967c7)  |
| ![Min-Max](https://github.com/user-attachments/assets/a5941bd5-7a08-499f-b79e-68496ceca40a) | |


---

## **Heap Construction Methods**

### **Top-Down (Repeated Insert):**

Insert each element one-by-one → heapify up.
⏱ Complexity: **O(n log n)**

### **Bottom-Up (Heapify):**

Convert given array into heap using repeated heapify-down from last non-leaf node.
⏱ Complexity: **O(n)** (more efficient)

---

## **Applications of Heap**

1. **Priority Queues**

   * The most common use of heaps.
   * A priority queue retrieves elements based on **priority instead of insertion order.**
   * Heaps ensure:

     * **Insert:** `O(log n)`
     * **Extract-Min / Extract-Max:** `O(log n)`
   * Used in:

     * Task scheduling
     * Operating system interrupts
     * Event-driven simulators

---

2. **Sorting (Heap Sort)**

   * Heap Sort is implemented using a **Max-Heap**.
   * Steps:

     * Build a heap from the array
     * Repeatedly extract the max element and rebuild the heap
   * Time Complexity:

     * Worst, Average, Best: **O(n log n)**
   * Requires no extra memory → **In-place sorting algorithm.**

---

3. **Graph Algorithms**
   Heaps are used for efficient priority queue operations in:

   * **Dijkstra’s Shortest Path**
   * **Prim’s Minimum Spanning Tree**
   * **A* Pathfinding Algorithm**

   These algorithms repeatedly select the smallest-weight edge or shortest tentative distance, which a **min-heap** supports efficiently.

---

4. **Lossless Data Compression**

   * Used in **Huffman Coding**.
   * A **min-heap** stores characters based on frequency.
   * The algorithm repeatedly extracts the two smallest nodes to build the Huffman tree.
   * Enables efficient prefix coding used in:

     * ZIP files
     * PNG images
     * Text compression systems

---

### Summary Table

| Application Area | Why Heap is Needed                          | Type Used    |
| ---------------- | ------------------------------------------- | ------------ |
| Priority Queue   | Fast insert and extract priority            | Min/Max Heap |
| Heap Sort        | Guarantees O(n log n) sorting               | Max-Heap     |
| Graph Algorithms | Fast retrieval of minimum weight            | Min-Heap     |
| Huffman Coding   | Repeated extraction of least frequent nodes | Min-Heap     |

---



