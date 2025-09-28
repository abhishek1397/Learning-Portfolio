# 🔍 Search (with Position) + 🖊️ Update in Singly Linked List

---

## 1️⃣ Search in Unsorted Linked List

* Traverse **entire list** until `key` is found.
* Return the **position** if found, else return `-1`.

### Code:

```cpp
int searchUnsorted(Node* head, int key) {
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
int searchSorted(Node* head,int key) {
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
int updateUnsorted(Node* head,int oldVal, int newVal) {
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
int updateSorted(Node* head,int oldVal, int newVal) {
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

##### Nice 👍 Let’s extend the **update functions** so they handle **all occurrences** of a given value in the linked list (both **sorted** and **unsorted**). 

# 🖊️ Update All Occurrences in Singly Linked List

## 1️⃣ Update All in Unsorted Linked List

* Traverse the **entire list**.
* Replace **every node** with `oldVal` by `newVal`.
* Keep track of positions updated.

### Code:

```cpp
vector<int> updateAllUnsorted(int oldVal, int newVal) {
    Node* temp = head;
    int pos = 1;
    vector<int> updatedPositions;

    while (temp) {
        if (temp->data == oldVal) {
            temp->data = newVal;
            updatedPositions.push_back(pos);
        }
        temp = temp->next;
        pos++;
    }

    if (!updatedPositions.empty()) {
        cout << "Updated all occurrences of " << oldVal 
             << " to " << newVal << " at positions: ";
        for (int p : updatedPositions) cout << p << " ";
        cout << endl;
    } else {
        cout << oldVal << " not found, update failed." << endl;
    }

    return updatedPositions;
}
```

---

## 2️⃣ Update All in Sorted Linked List

* Traverse while `node->data <= oldVal`.
* Replace all matches of `oldVal` with `newVal`.
* Stop early if `node->data > oldVal`.

### Code:

```cpp
vector<int> updateAllSorted(Node* head,int oldVal, int newVal) {
    Node* temp = head;
    int pos = 1;
    vector<int> updatedPositions;

    while (temp && temp->data <= oldVal) {
        if (temp->data == oldVal) {
            temp->data = newVal;
            updatedPositions.push_back(pos);
        }
        temp = temp->next;
        pos++;
    }

    if (!updatedPositions.empty()) {
        cout << "Updated all occurrences of " << oldVal 
             << " to " << newVal << " at positions: ";
        for (int p : updatedPositions) cout << p << " ";
        cout << endl;
    } else {
        cout << oldVal << " not found, update failed." << endl;
    }

    return updatedPositions;
}
```

---

## 📌 Summary

| Case         | Traversal                            | Stops Early? | Updates                 | Returns             |
| ------------ | ------------------------------------ | ------------ | ----------------------- | ------------------- |
| **Unsorted** | Traverse entire list                 | ❌ No         | All matches             | Vector of positions |
| **Sorted**   | Traverse until `node->data > oldVal` | ✅ Yes        | All matches up to limit | Vector of positions |

---

