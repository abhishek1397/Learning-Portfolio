# Singly Linked List - Insertions in C++

This project demonstrates different ways to **insert nodes** in a **singly linked list** using C++.

---

## 📌 What is a Singly Linked List?
A **singly linked list** is a linear data structure where each node contains:
- `data`: the value of the node
- `next`: pointer to the next node in the list

Unlike arrays, linked lists do not require contiguous memory and allow dynamic memory allocation.

---

## 🛠 Node Structure
```cpp
struct Node {
    int data;
    Node *next;

    Node(int new_data) {
        data = new_data;
        next = NULL;
    }
};
````

---

## 📌 Insertion Cases Implemented

### 1️⃣ Insert at the Front

```cpp
Node* insertAtFront(Node* head, int new_data) {
    Node* new_node = new Node(new_data);
    new_node->next = head;
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
        new_node->next = head;
        return new_node;
    }

    Node* temp = head;
    for (int i = 1; i < pos - 1 && temp != NULL; i++) {
        temp = temp->next;
    }

    if (temp == NULL) {
        cout << "Position out of range!" << endl;
        delete new_node;  // cleanup
        return head;
    }

    // Insert in middle or at end
    new_node->next = temp->next;
    temp->next = new_node;

    return head;
}
```

---

### 4️⃣ Insert at the Middle (True Middle)

Here we use the **slow/fast pointer method** to find the middle.

```cpp
Node* insertAtMiddle(Node* head, int new_data) {
    if (head == NULL) return new Node(new_data);

    Node* slow = head;
    Node* fast = head;

    // Move fast by 2 and slow by 1 until fast reaches end
    while (fast->next != NULL && fast->next->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }

    Node* new_node = new Node(new_data);
    new_node->next = slow->next;
    slow->next = new_node;

    return head;
}
```

---

## 📌 Traversal Function

```cpp
void traverseList(Node* head) {
    Node* curr = head;
    while (curr != NULL) {
        cout << curr->data << " ";
        curr = curr->next;
    }
    cout << endl;
}
```

---

## 📌 Freeing Memory

To avoid memory leaks, always free the list:

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
    Node *next;
    Node(int new_data) {
        data = new_data;
        next = NULL;
    }
};

Node* insertAtFront(Node* head, int new_data) {
    Node* new_node = new Node(new_data);
    new_node->next = head;
    return new_node;
}

Node* insertAtEnd(Node* head, int new_data) {
    Node* new_node = new Node(new_data);
    if (head == NULL) return new_node;
    Node* temp = head;
    while (temp->next != NULL) temp = temp->next;
    temp->next = new_node;
    return head;
}

Node* insertAtPosition(Node* head, int pos, int new_data) {
    Node* new_node = new Node(new_data);
    if (pos == 1) {
        new_node->next = head;
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
    temp->next = new_node;
    return head;
}

Node* insertAtMiddle(Node* head, int new_data) {
    if (head == NULL) return new Node(new_data);
    Node* slow = head;
    Node* fast = head;
    while (fast->next != NULL && fast->next->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }
    Node* new_node = new Node(new_data);
    new_node->next = slow->next;
    slow->next = new_node;
    return head;
}

void traverseList(Node* head) {
    Node* curr = head;
    while (curr != NULL) {
        cout << curr->data << " ";
        curr = curr->next;
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

    cout << "Original List: ";
    traverseList(head);

    head = insertAtFront(head, 5);
    cout << "After inserting 5 at front: ";
    traverseList(head);

    head = insertAtPosition(head, 3, 15);
    cout << "After inserting 15 at position 3: ";
    traverseList(head);

    head = insertAtMiddle(head, 25);
    cout << "After inserting 25 at middle: ";
    traverseList(head);

    freeList(head);
    return 0;
}
```

---

## ✅ Sample Output

```
Original List: 10 20 30
After inserting 5 at front: 5 10 20 30
After inserting 15 at position 3: 5 10 15 20 30
After inserting 25 at middle: 5 10 15 25 20 30
```

---

## 📚 Notes

* Memory management is important. Use `freeList()` after use.
* In modern C++, you can replace raw pointers with `std::unique_ptr` to avoid manual `delete`.

---


Would you like me to also prepare a **second markdown for deletion cases (delete front, delete end, delete by value/position)** so you can upload both together on GitHub?
```
