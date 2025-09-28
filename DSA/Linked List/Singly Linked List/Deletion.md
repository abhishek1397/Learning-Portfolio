# Singly Linked List - Deletions in C++

This project demonstrates different ways to **delete nodes** in a **singly linked list** using C++.

---

## 📌 What is Deletion in Linked List?
Deletion means removing a node from the list while maintaining proper connections between the remaining nodes.  

There are multiple cases to handle:
1. Delete from the **front** (head node)  
2. Delete from the **end**  
3. Delete from a **specific position**  
4. Delete by **value**  

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

## 📌 Deletion Cases Implemented

### 1️⃣ Delete from the Front

```cpp
Node* deleteFront(Node* head) {
    if (head == NULL) return NULL; // Empty list

    Node* temp = head;
    head = head->next;
    delete temp; // free memory
    return head;
}
```

---

### 2️⃣ Delete from the End

```cpp
Node* deleteEnd(Node* head) {
    if (head == NULL) return NULL;       // Empty list
    if (head->next == NULL) {            // Single node
        delete head;
        return NULL;
    }

    Node* temp = head;
    while (temp->next->next != NULL) {
        temp = temp->next;
    }

    delete temp->next;  // delete last node
    temp->next = NULL;  // set new end
    return head;
}
```

---

### 3️⃣ Delete from a Given Position

(Position is **1-based index**)

```cpp
Node* deleteAtPosition(Node* head, int pos) {
    if (head == NULL) return NULL;

    // Case 1: Delete head
    if (pos == 1) {
        Node* temp = head;
        head = head->next;
        delete temp;
        return head;
    }

    Node* temp = head;
    for (int i = 1; i < pos - 1 && temp != NULL; i++) {
        temp = temp->next;
    }

    if (temp == NULL || temp->next == NULL) {
        cout << "Position out of range!" << endl;
        return head;
    }

    Node* del = temp->next;
    temp->next = del->next;
    delete del;

    return head;
}
```

---

### 4️⃣ Delete by Value

```cpp
Node* deleteByValue(Node* head, int key) {
    if (head == NULL) return NULL;

    // Case 1: If head node holds the key
    if (head->data == key) {
        Node* temp = head;
        head = head->next;
        delete temp;
        return head;
    }

    Node* temp = head;
    while (temp->next != NULL && temp->next->data != key) {
        temp = temp->next;
    }

    if (temp->next == NULL) {
        cout << "Value not found!" << endl;
        return head;
    }

    Node* del = temp->next;
    temp->next = del->next;
    delete del;

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

Node* insertAtEnd(Node* head, int new_data) {
    Node* new_node = new Node(new_data);
    if (head == NULL) return new_node;
    Node* temp = head;
    while (temp->next != NULL) temp = temp->next;
    temp->next = new_node;
    return head;
}

Node* deleteFront(Node* head) {
    if (head == NULL) return NULL;
    Node* temp = head;
    head = head->next;
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
    while (temp->next->next != NULL) temp = temp->next;
    delete temp->next;
    temp->next = NULL;
    return head;
}

Node* deleteAtPosition(Node* head, int pos) {
    if (head == NULL) return NULL;
    if (pos == 1) {
        Node* temp = head;
        head = head->next;
        delete temp;
        return head;
    }
    Node* temp = head;
    for (int i = 1; i < pos - 1 && temp != NULL; i++) temp = temp->next;
    if (temp == NULL || temp->next == NULL) {
        cout << "Position out of range!" << endl;
        return head;
    }
    Node* del = temp->next;
    temp->next = del->next;
    delete del;
    return head;
}

Node* deleteByValue(Node* head, int key) {
    if (head == NULL) return NULL;
    if (head->data == key) {
        Node* temp = head;
        head = head->next;
        delete temp;
        return head;
    }
    Node* temp = head;
    while (temp->next != NULL && temp->next->data != key) temp = temp->next;
    if (temp->next == NULL) {
        cout << "Value not found!" << endl;
        return head;
    }
    Node* del = temp->next;
    temp->next = del->next;
    delete del;
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

    // Build initial list: 10 -> 20 -> 30 -> 40
    head = insertAtEnd(head, 10);
    head = insertAtEnd(head, 20);
    head = insertAtEnd(head, 30);
    head = insertAtEnd(head, 40);

    cout << "Original List: ";
    traverseList(head);

    head = deleteFront(head);
    cout << "After deleting front: ";
    traverseList(head);

    head = deleteEnd(head);
    cout << "After deleting end: ";
    traverseList(head);

    head = deleteAtPosition(head, 2);
    cout << "After deleting at position 2: ";
    traverseList(head);

    head = deleteByValue(head, 10);
    cout << "After deleting node with value 10: ";
    traverseList(head);

    freeList(head);
    return 0;
}
```

---

## ✅ Sample Output

```
Original List: 10 20 30 40
After deleting front: 20 30 40
After deleting end: 20 30
After deleting at position 2: 20
After deleting node with value 10: Value not found!
20
```

---

## 📚 Notes

* Always handle **edge cases**: empty list, single node, position out of range, value not found.
* Free memory after operations to avoid memory leaks.
* In modern C++, prefer `std::unique_ptr` to manage memory automatically.

---

