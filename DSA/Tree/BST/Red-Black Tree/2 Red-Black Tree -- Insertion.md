# **Insertion in Red-Black Tree**

Insertion in a Red-Black Tree involves two balancing mechanisms:

* **Recoloring**
* **Rotation**

Unlike AVL trees (where rotations are always used to fix imbalance), 
Red-Black Trees **attempt recoloring first**, and only perform rotations if recoloring cannot restore properties.

---

## **Rules to Remember**

* Newly inserted nodes are always colored **RED**.
* The color of **NULL (leaf) nodes is BLACK**.
* If the inserted node becomes the **root**, its color must be changed to **BLACK**.

---

## **Balancing Logic After Insertion**

![First Node inserted](https://github.com/user-attachments/assets/f775577a-3443-4c8c-af2c-26473e8f5233)

Once the node is inserted using standard BST rules and colored **RED**, violations may occur if the **parent is also RED** (because Red-Black Trees do not allow two consecutive red nodes).

The next step depends on the **uncle’s color**:

---

### **Case 1 — Uncle is RED → Recoloring**

If the **parent** and **uncle** are both **red**:
![Uncle is Red](https://github.com/user-attachments/assets/994c662d-7400-48fb-9d0a-4f4636eac2cd)

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
||<img width="993" height="370" alt="output244" src="https://github.com/user-attachments/assets/a5c62f24-fd8b-49f5-84fe-5356c12dc879" />||
||||
| **Left-Right (LR)**  | Parent is left child, new node is right child of parent  | Left Rotation → Right Rotation |
||<img width="993" height="370" alt="output245copy" src="https://github.com/user-attachments/assets/e32887c9-822d-4f07-adb0-e0ff4cd8b994" />||
||||
| **Right-Right (RR)** | Parent is right child, new node is right child of parent | Left Rotation                  |
||<img width="993" height="370" alt="output246" src="https://github.com/user-attachments/assets/e6cb8f8f-6db8-489f-8752-a2a2ffce2279" />||
||||
| **Right-Left (RL)**  | Parent is right child, new node is left child of parent  | Right Rotation → Left Rotation |
||<img width="993" height="370" alt="output247" src="https://github.com/user-attachments/assets/c78b4eb2-1b35-4477-8a39-79ac371020ae" />||


#### **Recoloring Rule After Rotation:**

| Rotation Case | Swap Colors Between         |
| ------------- | --------------------------- |
| **LL and RR** | Parent ↔ Grandparent        |
| **LR and RL** | Inserted Node ↔ Grandparent |

---

## Example: Creating a red-black tree with elements 3, 21, 32 and 15 in an empty tree.
||
|--|
|<img width="680" height="340" alt="output248" src="https://github.com/user-attachments/assets/52982e0f-c2c8-4c7b-b980-fdb4f88a993f" />|
|When the first element is inserted it is inserted as a root node and as root node has black colour so it acquires the colour black.|
||
|<img width="680" height="370" alt="output249" src="https://github.com/user-attachments/assets/b4423477-ca5b-4232-8320-b87c8570d2c8" />|
|The new element is always inserted with a red colour and as 21 > 3 so it becomes the part of the right subtree of the root node.|
||
|<img width="680" height="370" alt="output250" src="https://github.com/user-attachments/assets/d35c7c9f-d9cd-4a9d-8da8-4a5a22ba249c" />|
|Now, as we insert 32 we see there is a red father-child pair which violates the Red-Black tree rule so we have to rotate it. Moreover, we see the conditions of RR rotation (considering the null node of the root node as black) so after rotation as the root node can’t be Red so we have to perform recolouring in the tree resulting in the tree shown above. |
||
|<img width="680" height="370" alt="Annotation20210501131749-660x451" src="https://github.com/user-attachments/assets/96440e65-29f5-4ac1-9491-fe94e0af2eb3" />|
||
|Final Tree Structure:|
|<img width="680" height="370" alt="output252" src="https://github.com/user-attachments/assets/e3ac87ab-7dc6-4c56-bf31-1d3a68e7d213" />|
|

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

