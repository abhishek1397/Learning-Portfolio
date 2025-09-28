# 🔍 Search (with Position) + 🖊️ Update in Singly Linked List

---

## 1️⃣ Search in Unsorted Linked List

* Traverse **entire list** until `key` is found.
* Return the **position** if found, else return `-1`.

### Code:

```cpp
int searchUnsorted(int key) {
    Node* temp = head;
    int pos = 1;
    while (temp) {
        if (temp->data == key) {
            cout << "Found " << key << " at position " << pos << endl;
            return pos;
        }
        temp = temp->next;
        pos++;
    }
    cout << key << " not found in the list." << endl;
    return -1; // Not found
}
```

---

## 2️⃣ Search in Sorted Linked List

* Stop early if `node->data > key`.
* Return **position** if found, else `-1`.

### Code:

```cpp
int searchSorted(int key) {
    Node* temp = head;
    int pos = 1;
    while (temp && temp->data <= key) {
        if (temp->data == key) {
            cout << "Found " << key << " at position " << pos << endl;
            return pos;
        }
        temp = temp->next;
        pos++;
    }
    cout << key << " not found in the list." << endl;
    return -1; // Not found
}
```

---

## 3️⃣ Update in Unsorted Linked List

* Traverse until `oldVal` is found.
* Replace with `newVal` and return position.

### Code:

```cpp
int updateUnsorted(int oldVal, int newVal) {
    Node* temp = head;
    int pos = 1;
    while (temp) {
        if (temp->data == oldVal) {
            temp->data = newVal;
            cout << "Updated " << oldVal << " to " << newVal 
                 << " at position " << pos << endl;
            return pos;
        }
        temp = temp->next;
        pos++;
    }
    cout << oldVal << " not found, update failed." << endl;
    return -1; // Not found
}
```

---

## 4️⃣ Update in Sorted Linked List

* Stop traversal if `node->data > oldVal`.
* Replace with `newVal` and return position.

### Code:

```cpp
int updateSorted(int oldVal, int newVal) {
    Node* temp = head;
    int pos = 1;
    while (temp && temp->data <= oldVal) {
        if (temp->data == oldVal) {
            temp->data = newVal;
            cout << "Updated " << oldVal << " to " << newVal 
                 << " at position " << pos << endl;
            return pos;
        }
        temp = temp->next;
        pos++;
    }
    cout << oldVal << " not found, update failed." << endl;
    return -1; // Not found
}
```

---

## 📌 Summary Table

| Operation      | Unsorted                                              | Sorted                                                                                |
| -------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Search**     | Traverse full list, return position                   | Stop early if `node->data > key`, return position                                     |
| **Update**     | Replace first `oldVal` with `newVal`, return position | Replace `oldVal` with `newVal` if found before `node->data > oldVal`, return position |
| **Best Case**  | O(1) (head node)                                      | O(1) (head node)                                                                      |
| **Worst Case** | O(n)                                                  | O(n), but may terminate early                                                         |

---

