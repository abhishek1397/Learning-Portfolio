# **Binary Search Tree (BST)**

## **Definition**

A **Binary Search Tree (BST)** is a binary tree in which each node stores a **unique key** and satisfies the ordering rule:

* Keys in the **left subtree** are **strictly less** than the node’s key.
* Keys in the **right subtree** are **strictly greater** than the node’s key.

This ordering enables efficient searching, insertion, and deletion when the tree remains balanced.

| |
|--|
|![bst1](https://github.com/user-attachments/assets/c90b2858-5bae-4e93-8edb-efbf50027dbc) |
|![bst2](https://github.com/user-attachments/assets/83b98311-8885-4d50-b67f-46e77f2d5f01) |


---

## **Key Properties**

* Structure follows strict ordering rule.
* No duplicate values allowed.
* In-order traversal always produces elements in **sorted order**.
* Performance depends on tree shape (balanced vs. skewed).

---

## **Time Complexity**

| Operation | Best/Average Case | Worst Case |
| --------- | ----------------- | ---------- |
| Search    | **O(log n)**      | **O(n)**   |
| Insert    | **O(log n)**      | **O(n)**   |
| Delete    | **O(log n)**      | **O(n)**   |

* Worst-case performance occurs when the tree becomes **skewed** (like a linked list).

Using **self-balancing variants** (AVL Tree, Red-Black Tree) guarantees worst-case **O(log n)**.

---

## **Applications**

* Database indexing
* Symbol tables and compilers
* Maintaining a real-time sorted dataset
* Range queries (min, max, predecessor, successor)
* Foundation for advanced structures like **AVL Tree, Red-Black Tree, Treaps, and Splay Trees**

---

## **Advantages**

* Supports ordered data.
* Faster than arrays and linked lists for search/insert/delete (when balanced).
* Easy to extend into self-balancing forms.

---

## **Disadvantages**

* Without balancing, the tree can degrade into a linked list.
* Sensitive to insertion order.

---

