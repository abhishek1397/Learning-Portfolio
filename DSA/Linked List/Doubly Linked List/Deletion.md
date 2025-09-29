# Doubly Linked List - Deletions in C++

This project demonstrates different ways to **delete nodes** in a **doubly linked list** using C++.

---

## 📌 What is a Doubly Linked List?

A **doubly linked list (DLL)** is a linear data structure where each node contains:

* `data`: the value of the node
* `next`: pointer to the next node
* `prev`: pointer to the previous node

Since we have both directions, deletions are easier compared to singly linked lists.

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

## 📌 Deletion Cases Implemented

### 1️⃣ Delete from Front

```cpp
Node* deleteFront(Node* head) {
    if (head == NULL) return NULL; // Empty list

    Node* temp = head;
    head = head->next;

    if (head != NULL) {
        head->prev = NULL;
    }

    delete temp;
    return head;
}
```

---

### 2️⃣ Delete from End

```cpp
Node* deleteEnd(Node* head) {
    if (head == NULL) return NULL; // Empty list

    if (head->next == NULL) { // Only one node
        delete head;
        return NULL;
    }

    Node* temp = head;
    while (temp->next != NULL) temp = temp->next; // Move to tail

    temp->prev->next = NULL;
    delete temp;

    return head;
}
```

---

### 3️⃣ Delete at a Given Position

(Position is **1-based index**, i.e. `pos=1` deletes head)

```cpp
Node* deleteAtPosition(Node* head, int pos) {
    if (head == NULL) return NULL;

    Node* temp = head;

    // Case 1: Delete head
    if (pos == 1) {
        head = head->next;
        if (head != NULL) head->prev = NULL;
        delete temp;
        return head;
    }

    for (int i = 1; i < pos && temp != NULL; i++) {
        temp = temp->next;
    }

    if (temp == NULL) {
        cout << "Position out of range!" << endl;
        return head;
    }

    if (temp->prev != NULL) temp->prev->next = temp->next;
    if (temp->next != NULL) temp->next->prev = temp->prev;

    delete temp;
    return head;
}
```

---

### 4️⃣ Delete by Value

(Deletes the **first occurrence** of the value)

```cpp
Node* deleteByValue(Node* head, int value) {
    if (head == NULL) return NULL;

    Node* temp = head;

    // Case 1: Value found at head
    if (head->data == value) {
        head = head->next;
        if (head != NULL) head->prev = NULL;
        delete temp;
        return head;
    }

    while (temp != NULL && temp->data != value) {
        temp = temp->next;
    }

    if (temp == NULL) {
        cout << "Value not found!" << endl;
        return head;
    }

    if (temp->prev != NULL) temp->prev->next = temp->next;
    if (temp->next != NULL) temp->next->prev = temp->prev;

    delete temp;
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
    while (curr->next != NULL) curr = curr->next;
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

Node* deleteFront(Node* head) {
    if (head == NULL) return NULL;
    Node* temp = head;
    head = head->next;
    if (head != NULL) head->prev = NULL;
    delete temp;
    return head;
}

Node* deleteEnd(Node* head) {
    if (head == NULL) return NULL;
    if (head->next == NULL) {
        delete head;
        return NULL;
    }
    Node* temp = head;
    while (temp->next != NULL) temp = temp->next;
    temp->prev->next = NULL;
    delete temp;
    return head;
}

Node* deleteAtPosition(Node* head, int pos) {
    if (head == NULL) return NULL;
    Node* temp = head;
    if (pos == 1) {
        head = head->next;
        if (head != NULL) head->prev = NULL;
        delete temp;
        return head;
    }
    for (int i = 1; i < pos && temp != NULL; i++) temp = temp->next;
    if (temp == NULL) {
        cout << "Position out of range!" << endl;
        return head;
    }
    if (temp->prev != NULL) temp->prev->next = temp->next;
    if (temp->next != NULL) temp->next->prev = temp->prev;
    delete temp;
    return head;
}

Node* deleteByValue(Node* head, int value) {
    if (head == NULL) return NULL;
    Node* temp = head;
    if (head->data == value) {
        head = head->next;
        if (head != NULL) head->prev = NULL;
        delete temp;
        return head;
    }
    while (temp != NULL && temp->data != value) temp = temp->next;
    if (temp == NULL) {
        cout << "Value not found!" << endl;
        return head;
    }
    if (temp->prev != NULL) temp->prev->next = temp->next;
    if (temp->next != NULL) temp->next->prev = temp->prev;
    delete temp;
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

    head = append(head, 10);
    head = append(head, 20);
    head = append(head, 30);
    head = append(head, 40);

    cout << "Original List (Forward): ";
    traverseForward(head);

    head = deleteFront(head);
    cout << "After deleting front: ";
    traverseForward(head);

    head = deleteEnd(head);
    cout << "After deleting end: ";
    traverseForward(head);

    head = deleteAtPosition(head, 2);
    cout << "After deleting at position 2: ";
    traverseForward(head);

    head = deleteByValue(head, 10);
    cout << "After deleting value 10: ";
    traverseForward(head);

    cout << "Final List (Backward): ";
    traverseBackward(head);

    freeList(head);
    return 0;
}
```

---

## ✅ Sample Output

```
Original List (Forward): 10 20 30 40
After deleting front: 20 30 40
After deleting end: 20 30
After deleting at position 2: 20
After deleting value 10: Value not found!
Final List (Backward): 20
```

---

## 📚 Notes

* Always update **both `next` and `prev` pointers** during deletions.
* Check **edge cases**: empty list, single node list, invalid position/value.
* Use `freeList()` to avoid memory leaks.
* In modern C++, `std::unique_ptr` can replace raw pointers for safer memory management.

---
