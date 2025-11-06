# ✅ **Hash Table using Division Method + Separate Chaining**

## 🧭 Bird’s Eye View: Hashing (with Collision Handling — Separate Chaining)

```
main()
 │
 ▼
HashTable ht(size)
 │
 ├──► Step 1: Initialize Hash Table
 │       └── allocates → array of Node* (linked list heads)
 │       └── sets all indices → nullptr
 │
 ├──► Step 2: Insert Keys
 │       └── insert(key)
 │             │
 │             ├──► compute index = hashFunction(key)
 │             │        └── index = key % capacity
 │             │
 │             ├──► check if key already exists at index
 │             │        └── traverse linked list at table[index]
 │             │
 │             ├──► if key not found:
 │             │        └── create new Node(key)
 │             │        └── link new node at head of list (separate chaining)
 │             │
 │             └──► print "Inserted key at index"
 │
 ├──► Step 3: Display Hash Table
 │       └── display()
 │             │
 │             ├──► iterate over each index
 │             ├──► print index number
 │             ├──► traverse linked list at that index
 │             └──► print each key → (e.g., 12 -> 22 -> NULL)
 │
 ├──► Step 4: Search Key
 │       └── search(key)
 │             │
 │             ├──► compute index = hashFunction(key)
 │             ├──► traverse linked list at table[index]
 │             ├──► if key found → return true
 │             └──► else → return false
 │
 ├──► Step 5: Remove Key
 │       └── remove(key)
 │             │
 │             ├──► compute index = hashFunction(key)
 │             ├──► traverse linked list at table[index]
 │             │
 │             ├──► if found:
 │             │        ├── adjust pointers (unlink node)
 │             │        ├── delete node
 │             │        └── print "Key removed"
 │             │
 │             └──► else:
 │                      └── print "Key not found"
 │
 └──► Step 6: Destructor (Cleanup)
         └── ~HashTable()
              │
              ├──► for each index:
              │        └── traverse linked list → delete all nodes
              └──► delete[] table
```

---



```cpp
#include <iostream>
using namespace std;

struct Node {
    int key;
    Node* next;
    Node(int k) {
        key = k;
        next = nullptr;
    }
};

class HashTable {
private:
    int capacity;
    Node** table;  // Array of linked list heads

public:
    // Constructor
    HashTable(int size = 10) {
        capacity = size;
        table = new Node*[capacity];
        for (int i = 0; i < capacity; i++)
            table[i] = nullptr;
    }

    // Destructor
    ~HashTable() {
        for (int i = 0; i < capacity; i++) {
            Node* current = table[i];
            while (current != nullptr) {
                Node* temp = current;
                current = current->next;
                delete temp;
            }
        }
        delete[] table;
    }

    // Division method hash function
    int hashFunction(int key) {
        return key % capacity;
    }

    // Insert key
    void insert(int key) {
        int index = hashFunction(key);

        // Check if key already exists
        Node* current = table[index];
        while (current != nullptr) {
            if (current->key == key) {
                cout << "Key " << key << " already exists at index " << index << endl;
                return;
            }
            current = current->next;
        }

        // Insert at head of chain
        Node* newNode = new Node(key);
        newNode->next = table[index];
        table[index] = newNode;

        cout << "Inserted " << key << " at index " << index << endl;
    }

    // Search key
    bool search(int key) {
        int index = hashFunction(key);
        Node* current = table[index];
        while (current != nullptr) {
            if (current->key == key)
                return true;
            current = current->next;
        }
        return false;
    }

    // Remove key
    void remove(int key) {
        int index = hashFunction(key);
        Node* current = table[index];
        Node* prev = nullptr;

        while (current != nullptr) {
            if (current->key == key) {
                if (prev == nullptr)
                    table[index] = current->next;  // Remove head
                else
                    prev->next = current->next;

                delete current;
                cout << "Key " << key << " removed from index " << index << endl;
                return;
            }
            prev = current;
            current = current->next;
        }

        cout << "Key " << key << " not found\n";
    }

    // Display hash table
    void display() {
        cout << "\nHash Table (Separate Chaining):\n";
        for (int i = 0; i < capacity; i++) {
            cout << i << " --> ";
            Node* current = table[i];
            if (current == nullptr) {
                cout << "[empty]";
            } else {
                while (current != nullptr) {
                    cout << current->key << " -> ";
                    current = current->next;
                }
                cout << "NULL";
            }
            cout << endl;
        }
    }
};

int main() {
    HashTable ht(10);

    ht.insert(12);
    ht.insert(22);
    ht.insert(32);
    ht.insert(42);
    ht.insert(52);

    ht.display();

    cout << "\nSearching for 22: " << (ht.search(22) ? "Found" : "Not Found") << endl;
    cout << "Searching for 25: " << (ht.search(25) ? "Found" : "Not Found") << endl;

    ht.remove(22);
    ht.display();

    return 0;
}
```

---

### 🧠 Explanation

* **Hash function:**
  `index = key % capacity`
* **Separate chaining:**
  Each `table[i]` points to a linked list of nodes.
* **Insertion:** Adds new keys at the head of the linked list.
* **Search/Remove:** Traverses the linked list at the appropriate index.
* **Display:** Prints all chains clearly.

---

