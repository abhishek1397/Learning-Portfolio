# **AVL Tree**

## **Definition**

An **AVL Tree** is a **self-balancing Binary Search Tree** in which the **height difference (Balance Factor)** between the left and right subtree of any node is:

```
-1 <= {Balance Factor} <= +1

Balance Factor = Height(left subtree) - Height(right subtree)
```
| AVL Tree | Not an AVL Tree |
|----------|-----------------|
| ![Example-of-an-AVL-Tree-11](https://github.com/user-attachments/assets/1098bb28-108c-4e7f-800e-2cf3bb33644e) | ![Example-of-an-AVL-Tree-22](https://github.com/user-attachments/assets/b905f347-31b7-4f6c-b935-ed6f104b2e50) |
|![insert-ava1](https://github.com/user-attachments/assets/55f25609-88f6-49dd-8072-615e295973d4) |![Example-of-an-AVL-Tree_-2](https://github.com/user-attachments/assets/0fb0f8ca-1503-4128-9ed1-5fd0cd44a55c) |


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

#### 1. LL (Left-Left) Case:
| **LL (Left-Left)** | Inserted in **left subtree of left child** | Right Rotation     |
|------|-----|----|
| ![Right-Rotation-1](https://github.com/user-attachments/assets/0a439e08-0395-4b03-9ed0-f70c24cc43f7) | ![Right-Rotation-2](https://github.com/user-attachments/assets/dd93e763-ba25-49f2-b58b-a0deb24854ff) | ![Right-Rotation-3](https://github.com/user-attachments/assets/cb910f1f-f98f-4e98-bc1b-00948aac402d) | 

#### 2. RR (Right-Right) Case:
| **RR (Right-Right)** | Inserted in **right subtree of right child** |Left Rotation|
|------|-----|----|
| ![Left-Rotation-1](https://github.com/user-attachments/assets/ce2400ce-0c93-4c9f-aaaa-b108ceb28625) | ![Left-Rotation-2](https://github.com/user-attachments/assets/9989b81d-42ef-49eb-926a-41e6e24db984) | ![Left-Rotation-3](https://github.com/user-attachments/assets/381021c0-486e-49af-ab54-b317a730af27) |

#### 3. LR (Left-Right Case
| **LR (Left-Right)** | Inserted in **right subtree of left child** | Left Rotation on child + Right Rotation |
|------|-----|----|
| ![Left-Right-Rotation-1](https://github.com/user-attachments/assets/17f5b3ab-d3ae-4050-85a7-30be218416be) | ![Left-Right-Rotation-2](https://github.com/user-attachments/assets/391c8177-f7b5-4ab1-bd30-162fa29a7047) | ![Left-Right-Rotation-3](https://github.com/user-attachments/assets/f5d1d3b7-b112-44e9-afa6-f08261057cc8) |
| ![Left-Right-Rotation-4](https://github.com/user-attachments/assets/17adfd0c-3707-4d1b-9f4e-60b2a041748a) | ![Left-Right-Rotation-5](https://github.com/user-attachments/assets/2d9d7e1c-ce9f-493a-ab5c-f220dd65c23b) | |


#### 4. RL (Right-Left Case
| **RL (Right-Left)** |  Inserted in **left subtree of right child** | Right Rotation on child + Left Rotation |
|------|-----|----|
| ![Right-Left-Rotation-1](https://github.com/user-attachments/assets/4ae343f6-804c-4b8b-87ff-cea1252323ba) | ![Right-Left-Rotation-2](https://github.com/user-attachments/assets/a2a42ff0-b706-4b7d-ba22-d83b3ea568df) | ![Right-Left-Rotation-3](https://github.com/user-attachments/assets/4c386d12-a88b-49d0-b3c9-75bd79bb2e06) |
|![Right-Left-Rotation-4](https://github.com/user-attachments/assets/ddc3f3dd-ec4f-4c93-a40a-fe639eacc4ef) | ![Right-Left-Rotation-5](https://github.com/user-attachments/assets/699fed1a-c6e3-45c5-a568-3d493615fbaa) | |

---
### Let's Practise Rotation:
| No | Cheating :)|
|--|--|
|![right_left_rotation_27](https://github.com/user-attachments/assets/27c50483-d040-4153-a6a4-987823ff0db8) | ![right_left_rotation_28](https://github.com/user-attachments/assets/acb8ee8a-deb4-479c-85ea-0558ac9ebcbe) |
| ![right_left_rotation_29](https://github.com/user-attachments/assets/a10b6413-70e5-4049-86fe-ca0b52deaeac) | ![right_left_rotation_30](https://github.com/user-attachments/assets/d99551e7-8daf-48a1-8dd3-58efb891d8d1) |



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


