# Doubly Linked List - Insertions in C++

## 📌 What is a Doubly Linked List?

A **doubly linked list (DLL)** is a linear data structure where each node contains:

* `data`: the value of the node
* `next`: pointer to the next node
* `prev`: pointer to the previous node

This makes traversal possible in both **forward** and **backward** directions.

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

## 📌 Insertion Cases Implemented

### 1️⃣ Insert at the Front

```cpp
Node* insertAtFront(Node* head, int new_data) {
    Node* new_node = new Node(new_data);

    if (head != NULL) {
        new_node->next = head;
        head->prev = new_node;
    }

    return new_node;  // new head
}
```

---

### 2️⃣ Insert at the End

```cpp
Node* insertAtEnd(Node* head, int new_data) {
    Node* new_node = new Node(new_data);

    if (head == NULL) return new_node; // Empty list → new node is head

    Node* temp = head;
    while (temp->next != NULL) {
        temp = temp->next;
    }

    temp->next = new_node;
    new_node->prev = temp;

    return head;
}
```

---

### 3️⃣ Insert at a Given Position

(Position is **1-based index**, i.e. `pos=1` inserts at the head)

```cpp
Node* insertAtPosition(Node* head, int pos, int new_data) {
    Node* new_node = new Node(new_data);

    // Case 1: Insert at head
    if (pos == 1) {
        if (head != NULL) {
            new_node->next = head;
            head->prev = new_node;
        }
        return new_node;
    }

    Node* temp = head;
    for (int i = 1; i < pos - 1 && temp != NULL; i++) {
        temp = temp->next;
    }

    if (temp == NULL) {
        cout << "Position out of range!" << endl;
        delete new_node;
        return head;
    }

    new_node->next = temp->next;
    new_node->prev = temp;

    if (temp->next != NULL) {
        temp->next->prev = new_node;
    }

    temp->next = new_node;

    return head;
}
```

---

## 📌 Traversal Functions

```cpp
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
    while (curr->next != NULL) curr = curr->next; // move to tail
    while (curr != NULL) {
        cout << curr->data << " ";
        curr = curr->prev;
    }
    cout << endl;
}
```

---

## 📌 Freeing Memory

```cpp
void freeList(Node* head) {
    Node* temp;
    while (head != NULL) {
        temp = head;
        head = head->next;
        delete temp;
    }
}
```

---

## 📌 Full Example Code

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

Node* insertAtFront(Node* head, int new_data) {
    Node* new_node = new Node(new_data);
    if (head != NULL) {
        new_node->next = head;
        head->prev = new_node;
    }
    return new_node;
}

Node* insertAtEnd(Node* head, int new_data) {
    Node* new_node = new Node(new_data);
    if (head == NULL) return new_node;
    Node* temp = head;
    while (temp->next != NULL) temp = temp->next;
    temp->next = new_node;
    new_node->prev = temp;
    return head;
}

Node* insertAtPosition(Node* head, int pos, int new_data) {
    Node* new_node = new Node(new_data);
    if (pos == 1) {
        if (head != NULL) {
            new_node->next = head;
            head->prev = new_node;
        }
        return new_node;
    }
    Node* temp = head;
    for (int i = 1; i < pos - 1 && temp != NULL; i++) temp = temp->next;
    if (temp == NULL) {
        cout << "Position out of range!" << endl;
        delete new_node;
        return head;
    }
    new_node->next = temp->next;
    new_node->prev = temp;
    if (temp->next != NULL) temp->next->prev = new_node;
    temp->next = new_node;
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
    while (curr->next != NULL) curr = curr->next;
    while (curr != NULL) {
        cout << curr->data << " ";
        curr = curr->prev;
    }
    cout << endl;
}

void freeList(Node* head) {
    Node* temp;
    while (head != NULL) {
        temp = head;
        head = head->next;
        delete temp;
    }
}

int main() {
    Node* head = NULL;

    head = insertAtEnd(head, 10);
    head = insertAtEnd(head, 20);
    head = insertAtEnd(head, 30);

    cout << "Forward Traversal: ";
    traverseForward(head);

    head = insertAtFront(head, 5);
    cout << "After inserting 5 at front: ";
    traverseForward(head);

    head = insertAtPosition(head, 3, 15);
    cout << "After inserting 15 at position 3: ";
    traverseForward(head);

    cout << "Backward Traversal: ";
    traverseBackward(head);

    freeList(head);
    return 0;
}
```

---

## ✅ Sample Output

```
Forward Traversal: 10 20 30
After inserting 5 at front: 5 10 20 30
After inserting 15 at position 3: 5 10 15 20 30
Backward Traversal: 30 20 15 10 5
```

---

## 📚 Notes

* In DLL, always update **both `next` and `prev` pointers** during insertions.
* Memory management is crucial — free memory when done.
* Use **smart pointers** in modern C++ (`std::unique_ptr`) to avoid manual deletes.

---

👉 Next step after this would be **deletions in DLL (front, end, position/value)**.
Would you like me to prepare the **deletion cases for DLL** just like this, so your GitHub has both insertions and deletions side by side?
