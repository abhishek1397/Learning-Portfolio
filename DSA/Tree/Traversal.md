# Binary Tree

### Simple C++ Program for Binary Tree using `struct`:

```cpp
#include <iostream>
using namespace std;

// Define the structure for a tree node
struct Node {
    int data;
    Node* left;
    Node* right;

    // Constructor to create a new node
    Node(int val) {
        data = val;
        left = nullptr;
        right = nullptr;
    }
};

// Function to insert a node into the binary tree (basic method)
Node* insert(Node* root, int data) {
    if (root == nullptr) {
        return new Node(data); // Create a new node if the tree is empty
    }

    // Else, insert data into the left or right subtree
    if (data < root->data) {
        root->left = insert(root->left, data);
    } else {
        root->right = insert(root->right, data);
    }
    return root;
}

// Inorder Traversal (Left, Root, Right)
void inorderTraversal(Node* root) {
    if (root == nullptr)
        return;
    
    inorderTraversal(root->left); // Traverse left subtree
    cout << root->data << " ";     // Visit root
    inorderTraversal(root->right); // Traverse right subtree
}

int main() {
    Node* root = nullptr;

    // Insert nodes into the binary tree
    root = insert(root, 50);
    insert(root, 30);
    insert(root, 20);
    insert(root, 40);
    insert(root, 70);
    insert(root, 60);
    insert(root, 80);

    cout << "Inorder Traversal of the Binary Tree: ";
    inorderTraversal(root); // Should print nodes in ascending order
    cout << endl;

    return 0;
}
```

### Explanation:

1. **Struct `Node`**: This struct defines each tree node, with `data`, `left`, and `right` as its members.
2. **Insert Function**: A basic insert function is used to place nodes in the correct position based on their value (left subtree for smaller values, right for larger).
3. **Inorder Traversal**: This function prints out the tree in ascending order, as it first visits the left subtree, then the root, and finally the right subtree.
4. **Main Function**: This demonstrates inserting values into the tree and performing an inorder traversal.

### Example Output:

```
Inorder Traversal of the Binary Tree: 20 30 40 50 60 70 80 
```
***

Below are the function snippets for **Preorder**, **Inorder**, and **Postorder** traversals of a binary tree in C++.

---

### ✅ **Inorder Traversal** (Left → Root → Right)

```cpp
void inorderTraversal(Node* root) {
    if (root == nullptr)
        return;

    inorderTraversal(root->left);
    cout << root->data << " ";
    inorderTraversal(root->right);
}
```

---

### ✅ **Preorder Traversal** (Root → Left → Right)

```cpp
void preorderTraversal(Node* root) {
    if (root == nullptr)
        return;

    cout << root->data << " ";
    preorderTraversal(root->left);
    preorderTraversal(root->right);
}
```

---

### ✅ **Postorder Traversal** (Left → Right → Root)

```cpp
void postorderTraversal(Node* root) {
    if (root == nullptr)
        return;

    postorderTraversal(root->left);
    postorderTraversal(root->right);
    cout << root->data << " ";
}
```

---

You can call these functions from `main()` like this:

```cpp
preorderTraversal(root);
inorderTraversal(root);
postorderTraversal(root);
```


