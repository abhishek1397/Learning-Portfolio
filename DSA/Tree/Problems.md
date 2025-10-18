 # 1. Minimum value in a binary tree

```cpp
// Function to find the minimum value in a binary tree (not necessarily BST)

int findMin(Node* root) {
    int root_val, left, right, min = INT_MAX;

    if (root != NULL) {
        root_val = root->data;
        left = findMin(root->left);
        right = findMin(root->right);

        if (left < right)
            min = left;
        else
            min = right;

        if (root_val < min)
            min = root_val;
    }

    return min;
}
```

### 📘 Notes:

* This function finds the **minimum element in a binary tree** using **recursive traversal**.
* It is **not** assuming any ordering (like in a Binary Search Tree).
* Base case: if `root == NULL`, return `INT_MAX` to ensure it doesn't affect the minimum comparison.
* At each node:

---

# 2.  Maximum value in a binary tree

```cpp
#include <iostream>
#include <climits>
using namespace std;

// Function to find the maximum value in a binary tree
int findMax(Node* root) {
    int root_val, left, right, max = INT_MIN;

    if (root != NULL) {
        root_val = root->data;
        left = findMax(root->left);
        right = findMax(root->right);

        if (left > right)
            max = left;
        else
            max = right;

        if (root_val > max)
            max = root_val;
    }

    return max;
}
```

### 🔍 Description:
* This function recursively finds the **maximum element in a binary tree**.
* It does **not assume** any order like in a Binary Search Tree.
* It checks all nodes via **post-order traversal** and compares values.

***
# 3. 
