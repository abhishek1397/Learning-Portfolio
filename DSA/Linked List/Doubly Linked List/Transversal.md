# Doubly Linked List - Traversal in C++

## 📌 What is a Doubly Linked List?

A **doubly linked list (DLL)** is a data structure where each node contains:

* `data`: value stored in the node
* `next`: pointer to the next node
* `prev`: pointer to the previous node

This allows **bidirectional traversal**.

---

## 🛠 Node Structure

```cpp
struct Node {
    int data;
    Node* prev;
    Node* next;

    Node(int new_data) {
        data = new_data;
        prev = NULL;
        next = NULL;
    }
};
```

---

## 📌 Traversal in DLL

### 1️⃣ Forward Traversal

Moves from **head → tail**.

```cpp
void traverseForward(Node* head) {
    Node* curr = head;
    while (curr != NULL) {
        cout << curr->data << " ";
        curr = curr->next;
    }
    cout << endl;
}
```

---

### 2️⃣ Backward Traversal

Moves from **tail → head**.

```cpp
void traverseBackward(Node* head) {
    if (head == NULL) return;

    // Move to tail
    Node* curr = head;
    while (curr->next != NULL) {
        curr = curr->next;
    }

    // Traverse backwards
    while (curr != NULL) {
        cout << curr->data << " ";
        curr = curr->prev;
    }
    cout << endl;
}
```

---

## 📌 Example Code

```cpp
#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* prev;
    Node* next;
    Node(int new_data) {
        data = new_data;
        prev = NULL;
        next = NULL;
    }
};

// Utility function to append node at end
Node* append(Node* head, int new_data) {
    Node* new_node = new Node(new_data);
    if (head == NULL) return new_node;

    Node* temp = head;
    while (temp->next != NULL) temp = temp->next;

    temp->next = new_node;
    new_node->prev = temp;

    return head;
}

void traverseForward(Node* head) {
    Node* curr = head;
    while (curr != NULL) {
        cout << curr->data << " ";
        curr = curr->next;
    }
    cout << endl;
}

void traverseBackward(Node* head) {
    if (head == NULL) return;

    Node* curr = head;
    while (curr->next != NULL) curr = curr->next; // go to tail

    while (curr != NULL) {
        cout << curr->data << " ";
        curr = curr->prev;
    }
    cout << endl;
}

int main() {
    Node* head = NULL;

    head = append(head, 10);
    head = append(head, 20);
    head = append(head, 30);
    head = append(head, 40);

    cout << "Forward Traversal: ";
    traverseForward(head);

    cout << "Backward Traversal: ";
    traverseBackward(head);

    return 0;
}
```

---

## ✅ Sample Output

```
Forward Traversal: 10 20 30 40
Backward Traversal: 40 30 20 10
```
