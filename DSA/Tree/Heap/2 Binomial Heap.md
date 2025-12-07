# **Binomial Heap**

## **Definition**

A **Binomial Heap** is a collection of **Binomial Trees** where:

* Each tree satisfies the **Min-Heap property**
* There is **at most one binomial tree of any degree**
* Trees are stored in **linked list form sorted by increasing degree**

Binomial Heap is designed to support **efficient merge (union)** operations, unlike a binary heap.

A Binomial Heap is a merge-efficient heap implemented as a collection of binomial trees, where each tree obeys the min-heap property and no two trees share the same degree.

---

## **Binomial Tree**

A **Binomial Tree of order `k` (Bk)** is defined recursively:

* **B0**: single node
* **Bk**: formed by joining two **Bk−1** trees → making one the leftmost child of the other.

### **Properties of Binomial Tree Bk**

| Property           | Value                                      |
| ------------------ | ------------------------------------------ |
| Number of nodes    | **2ᵏ**                                     |
| Height             | **k**                                      |
| Nodes at depth `i` | **C(k, i)**                                |
| Children of root   | **k children** (orders: k−1, k−2, … , 0)** |

``` php

Here height = k

k = 0 (Single Node)
 o
 
k = 1 (2 nodes) 
[We take two k = 0 order Binomial Trees, and make one as a child of other]
  o
 /  
o     

k = 2 (4 nodes)
[We take two k = 1 order Binomial Trees, and make one as a child of other]
     o
   /   \
  o     o
 /       
o        

k = 3 (8 nodes)
[We take two k = 2 order Binomial Trees, and make one as a child of other]
        o   
     /  | \ 
    o   o  o
   / \  | 
  o   o o   
 /              
o  
```

---

## **Properties of Binomial Heap**

* Contains a set of **binomial trees** `{B0, B1, B2, …}`
* At most **one tree of each degree**
* Follows **Min-Heap property**
* The root list is sorted by **increasing degree**

Example:

```
13 nodes → Trees of orders: B0, B2, B3   (1 + 4 + 8 = 13)
```

```
12------------10--------------------20
             /  \                 /  | \
           15    50             70  50  40
           |                  / |    |     
           30               80  85  65 
                            |
                           100
A Binomial Heap with 13 nodes. It is a collection of 3 Binomial Trees of orders 0, 2, and 3 from left to right.


    10--------------------20
   /  \                 /  | \
 15    50             70  50  40
 |                  / |    |     
 30               80  85  65 
                  |
                 100
A Binomial Heap with 12 nodes. It is a collection of 2. Binomial Trees of orders 2 and 3 from left to right. 

```

---

## **Operations on Binomial Heap**

Most operations rely on the **union()** operation.

| Operation                      | Description                                                     | Time Complexity                         |
| ------------------------------ | --------------------------------------------------------------- | --------------------------------------- |
| **Insert(H, key)**             | Create single-node heap and perform `union` with H              | **O(log n)**                            |
| **Get-Min(H)**                 | Scan root list OR maintain pointer                              | **O(log n)** (or **O(1)** with pointer) |
| **Extract-Min(H)**             | Remove tree with min root, break into subtrees, then union back | **O(log n)**                            |
| **Decrease-Key(H, x, newKey)** | Bubble up by swapping with parent if needed                     | **O(log n)**                            |
| **Delete(H, x)**               | Decrease key to −∞ then Extract-Min                             | **O(log n)**                            |
| **Union(H1, H2)**              | Merge and fix duplicate degrees                                 | **O(log n)**                            |

---

## **Union Operation (Core Operation)**

Steps:

1. **Merge** root lists of H1 and H2 in increasing order of degree.
2. Traverse merged list and fix duplicates:

   * **Case 1:** Degree(x) ≠ Degree(next) → move forward
   * **Case 2:** Degree(x) = Degree(next) = Degree(next-next) → skip forward
   * **Case 3:** key(x) ≤ key(next) → make `next` child of `x`
   * **Case 4:** key(x) > key(next) → make `x` child of `next`

After processing → result contains at most **one tree per degree**.

![Union operation binomial heap](https://github.com/user-attachments/assets/ae3083ed-09c8-4fe3-8c8c-a10c59081aa1)


---

## **Comparison with Other Heaps**

| Operation    | Binary Heap | Binomial Heap | Fibonacci Heap     |
| ------------ | ----------- | ------------- | ------------------ |
| Insert       | Θ(log n)    | Θ(log n)      | **Θ(1)** amortized |
| Find Min     | Θ(1)        | O(log n)      | **Θ(1)**           |
| Extract Min  | Θ(log n)    | Θ(log n)      | Θ(log n)           |
| Union        | Θ(n)        | **O(log n)**  | **Θ(1)**           |
| Decrease Key | Θ(log n)    | Θ(log n)      | **Θ(1)**           |
| Delete       | Θ(log n)    | Θ(log n)      | Θ(log n)           |

---

## **Why Binomial Heap Exists**

Binary Heap is fast but **union is expensive (Θ(n))**.
Binomial Heap is slower in some operations but supports **efficient merge in O(log n)** → critical in:

* Distributed job scheduling
* Mergeable priority queues
* Graph algorithms with frequently merging PQ states

---


