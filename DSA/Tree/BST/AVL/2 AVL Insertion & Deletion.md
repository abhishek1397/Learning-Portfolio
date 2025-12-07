# **Insertion in AVL Tree**

Insertion in an AVL Tree follows the same steps as insertion in a Binary Search Tree (BST):

1. **Insert the new key using BST rules**

   * If key < node → go to left subtree
   * If key > node → go to right subtree
  
![Deletion-in-an-AVL-Tree_](https://github.com/user-attachments/assets/f69e0aca-9ae9-44af-8a95-70424c72cd0d)

2. **After insertion**, while returning back up the recursion stack, compute the **Balance Factor** of each ancestor node:

Balance Factor = Height(left) - Height(right)


3. If the **Balance Factor becomes less than −1 or greater than +1**, the tree is **unbalanced**, and a **rotation is applied** to restore AVL property.
4. 
   * LL → Right Rotation
   * RR → Left Rotation
   * LR → Left then Right Rotation
   * RL → Right then Left Rotation

| | |
|--|--|
|![right_left_rotation_3](https://github.com/user-attachments/assets/dcb796d3-8ec7-4a88-bb7a-bce707508b8d) | ![right_left_rotation_4](https://github.com/user-attachments/assets/95492da0-6841-419d-b8f5-1c81f33ec938)|
|![right_left_rotation_5](https://github.com/user-attachments/assets/c67c61b5-a45b-4eca-96ee-fd1e632289d5) |![right_left_rotation_6](https://github.com/user-attachments/assets/7ba6c2cf-313c-4fd4-8c07-ffab2dced41a)|
|![right_left_rotation_7](https://github.com/user-attachments/assets/ae92756d-7a8d-4c76-944a-8f3020a0d2ba) | ![right_left_rotation_8](https://github.com/user-attachments/assets/c901495a-d9a1-45cc-b36e-2993a1d15dd7)|
|![right_left_rotation_9](https://github.com/user-attachments/assets/99cddee8-e4fc-4322-8e2a-2e6a4761cc1b) |![right_left_rotation_10](https://github.com/user-attachments/assets/6cd5bbcb-902b-4ca1-971e-f4730a2116c9) |
|![right_left_rotation_11](https://github.com/user-attachments/assets/85bb4726-f446-4c2f-b72f-bcd447d785fa) | ![right_left_rotation_12](https://github.com/user-attachments/assets/aa2fd96d-04c8-4b67-8489-8f213746b7bd)|
|![right_left_rotation_13](https://github.com/user-attachments/assets/505bd4f8-2757-4f3c-ad83-121b421022ff) |![right_left_rotation_14](https://github.com/user-attachments/assets/228eb8c8-3c94-4a11-8931-b8cbac7ff26a) |


---

### **Time Complexity**

Insertion in AVL Tree takes: **O(log n)** because the height of an AVL tree is always maintained as **O(log n)**.

## **When to Choose AVL Tree vs Red-Black Tree**

| Scenario                                     | Best Choice        |
| -------------------------------------------- | ------------------ |
| Search operations more frequent than updates | **AVL Tree**       |
| Heavy insert/delete operations               | **Red-Black Tree** |

AVL is more strictly balanced → faster searches.
Red-Black Tree performs fewer rotations → faster updates.

---

## **Applications**

* Databases
* Memory management
* Indexing and file systems
* Routing tables
* Any system requiring predictable worst-case performance

---

## **Advantages**

* Always balanced → guaranteed **O(log n)**
* Faster lookup than Red-Black Tree
* Sorted order maintained via in-order traversal

---

## **Disadvantages**

* More complex implementation than BST
* More rotations than Red-Black trees → slower insert/delete



Tell me which one.
