# ✅ **Hash Table** using **open addressing with linear probing**

## 🧠 What is *Open Addressing*?

**Open addressing** is a collision-resolution strategy used in hash tables.

When two keys hash to the same index (a **collision**), instead of using a linked list (as in **separate chaining**), the algorithm looks for another **open (empty)** slot in the **same table array** to store the new key.

So, **all elements are stored inside the same array**, and no extra data structures are needed.


## 🔁 What is *Linear Probing*?

**Linear probing** is one specific method of *open addressing* that resolves collisions by checking the **next available slot sequentially** (in a straight line).

### 🔹 Formula

f `h(k)` is the hash function and a collision occurs,
we check the following indices:

```
h(k), (h(k) + 1) % capacity, (h(k) + 2) % capacity, ...
```

We wrap around using `% capacity` so we stay inside the table.

##### 🧩 Example

Let’s say we have a hash table of size `10` and we’re using the hash function:

```
h(k) = k % 10
```

##### Step 1: Insert 12

```
h(12) = 2
```

→ Slot 2 is empty → store `12` there.

| Index | 0 | 1 | 2  | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| ----- | - | - | -- | - | - | - | - | - | - | - |
| Value |   |   | 12 |   |   |   |   |   |   |   |


##### Step 2: Insert 22

```
h(22) = 2
```

→ Slot 2 is occupied (collision!)
→ Try next slot: index `3`
→ Slot 3 is empty → store `22`.

| Index | 0 | 1 | 2  | 3  | 4 | 5 | 6 | 7 | 8 | 9 |
| ----- | - | - | -- | -- | - | - | - | - | - | - |
| Value |   |   | 12 | 22 |   |   |   |   |   |   |


##### Step 3: Insert 32

```
h(32) = 2
```

→ 2 occupied → try 3 (occupied) → try 4 (empty) → store `32`.

| Index | 0 | 1 | 2  | 3  | 4  | 5 | 6 | 7 | 8 | 9 |
| ----- | - | - | -- | -- | -- | - | - | - | - | - |
| Value |   |   | 12 | 22 | 32 |   |   |   |   |   |


### 🔍 Searching with Linear Probing

To find a key (say `32`):

1. Compute `h(32) = 2`
2. Check index 2 → not `32`
3. Check index 3 → not `32`
4. Check index 4 → found it ✅


### ❌ Deleting with Linear Probing

When you delete a key, you **can’t just mark the slot empty**, because it might break the search chain.
So instead, you mark it as **“deleted”** (often with a special marker like `-2`).
That way, searching continues through deleted spots until it either finds the key or hits a truly empty slot.


## 📊 Summary Table
| Concept                | Description                                                                          |
| ---------------------- | ------------------------------------------------------------------------------------ |
| **Open Addressing**    | All data stored in the same array; collisions resolved by finding another open slot. |
| **Linear Probing**     | Move linearly to the next slot until an empty one is found.                          |
| **Collision Handling** | Sequentially probe `(index + 1) % capacity`.                                         |
| **Advantages**         | Simple, cache-friendly, no extra memory for linked lists.                            |
| **Disadvantages**      | Can cause “clustering” (many items grouped together).                                |

---

```cpp

#include <iostream>
using namespace std;

class HashTable {
private:
    int* table;
    int capacity;
    int currentSize;

public:
    // Constructor
    HashTable(int size = 10) {
        capacity = size;
        currentSize = 0;
        table = new int[capacity];
        for (int i = 0; i < capacity; i++)
            table[i] = -1; // -1 indicates empty slot
    }

    // Destructor
    ~HashTable() {
        delete[] table;
    }

    // Hash function using division method
    int hashFunction(int key) {
        return key % capacity;
    }

    // Insert key using linear probing
    void insert(int key) {
        if (currentSize == capacity) {
            cout << "Hash Table is full! Cannot insert " << key << endl;
            return;
        }

        int index = hashFunction(key);
        int startIndex = index;

        while (table[index] != -1 && table[index] != -2) {
            index = (index + 1) % capacity;
            if (index == startIndex) {
                cout << "No empty slot found for key " << key << endl;
                return;
            }
        }

        table[index] = key;
        currentSize++;
    }

    // Search for a key
    bool search(int key) {
        int index = hashFunction(key);
        int startIndex = index;

        while (table[index] != -1) {
            if (table[index] == key)
                return true;
            index = (index + 1) % capacity;
            if (index == startIndex)
                return false;
        }
        return false;
    }

    // Remove a key
    void remove(int key) {
        int index = hashFunction(key);
        int startIndex = index;

        while (table[index] != -1) {
            if (table[index] == key) {
                table[index] = -2; // -2 indicates deleted slot
                currentSize--;
                cout << "Key " << key << " deleted\n";
                return;
            }
            index = (index + 1) % capacity;
            if (index == startIndex)
                break;
        }

        cout << "Key " << key << " not found\n";
    }

    // Display the hash table
    void display() {
        cout << "\nHash Table:\n";
        for (int i = 0; i < capacity; i++) {
            if (table[i] == -1)
                cout << i << " --> [empty]\n";
            else if (table[i] == -2)
                cout << i << " --> [deleted]\n";
            else
                cout << i << " --> " << table[i] << "\n";
        }
    }
};

int main() {
    HashTable ht;
    ht.insert(12);
    ht.insert(22);
    ht.insert(32);
    ht.insert(42);
    ht.display();

    cout << "\nSearching for 22: " << (ht.search(22) ? "Found" : "Not Found") << endl;
    cout << "Searching for 25: " << (ht.search(25) ? "Found" : "Not Found") << endl;

    ht.remove(22);
    ht.display();

    return 0;
}

```


```cpp
#include <iostream>
using namespace std;

class HashTable {
private:
    int* table;
    int capacity;
    const int EMPTY = -1;
    const int DELETED = -2;

public:
    HashTable(int size = 10) {
        capacity = size;
        table = new int[capacity];
        for (int i = 0; i < capacity; i++)
            table[i] = EMPTY;
    }

    ~HashTable() {
        delete[] table;
    }

    int hashFunction(int key) {
        return key % capacity;
    }

    // Insert using linear probing (allows duplicates)
    void insert(int key) {
        int index = hashFunction(key);

        for (int i = 0; i < capacity; i++) {
            int probe = (index + i) % capacity;

            if (table[probe] == EMPTY || table[probe] == DELETED) {
                table[probe] = key;
                return;
            }
        }

        cout << "Hash Table Full. Cannot insert " << key << endl;
    }

    // Search key (returns true if any instance is found)
    bool search(int key) {
        int index = hashFunction(key);

        for (int i = 0; i < capacity; i++) {
            int probe = (index + i) % capacity;

            if (table[probe] == EMPTY)
                return false; // Key not present

            if (table[probe] == key)
                return true;
        }

        return false;
    }

    // Remove only ONE occurrence
    void remove(int key) {
        int index = hashFunction(key);

        for (int i = 0; i < capacity; i++) {
            int probe = (index + i) % capacity;

            if (table[probe] == EMPTY) {
                cout << "Key " << key << " not found" << endl;
                return;
            }

            if (table[probe] == key) {
                table[probe] = DELETED;
                cout << "Deleted key: " << key << endl;
                return;
            }
        }

        cout << "Key " << key << " not found" << endl;
    }

    void display() {
        cout << "\nHash Table:\n";
        for (int i = 0; i < capacity; i++) {
            if (table[i] == EMPTY)
                cout << i << " --> [EMPTY]\n";
            else if (table[i] == DELETED)
                cout << i << " --> [DELETED]\n";
            else
                cout << i << " --> " << table[i] << "\n";
        }
    }
};

int main() {
    HashTable ht(10);

    ht.insert(12);
    ht.insert(22);
    ht.insert(32);
    ht.insert(42);
    ht.insert(22); // duplicate
    ht.insert(32); // duplicate

    ht.display();

    cout << "\nSearching for 22: " 
         << (ht.search(22) ? "Found" : "Not Found") << endl;

    cout << "Searching for 25: " 
         << (ht.search(25) ? "Found" : "Not Found") << endl;

    ht.remove(22);
    ht.remove(32);

    cout << "\nAfter deletions:\n";
    ht.display();

    return 0;
}


```

### 🧠 Overview of the Code

The class `HashTable` manages an integer hash table with these main features:

* **Hashing by division method:**
  `hashFunction(key) = key % capacity`
* **Collision resolution:** Linear probing
* **Markers:**

  * `-1` → empty slot
  * `-2` → deleted slot
* **Operations:**

  * `insert(int key)`
  * `search(int key)`
  * `remove(int key)`
  * `display()`

---

### 🧩 Step-by-step Execution

#### **1. Creation**

```cpp
HashTable ht;
```

Creates a table of size `10` (default) initialized with `-1` (empty).

---

#### **2. Insertions**

```cpp
ht.insert(12);
ht.insert(22);
ht.insert(32);
ht.insert(42);
```

**Hash calculations:**

| Key | hashFunction(key) | Slot                            | Action            |
| --- | ----------------- | ------------------------------- | ----------------- |
| 12  | 12 % 10 = 2       | 2                               | Insert at index 2 |
| 22  | 22 % 10 = 2       | 2 occupied → try 3              | Insert at index 3 |
| 32  | 32 % 10 = 2       | 2 occupied → 3 occupied → try 4 | Insert at index 4 |
| 42  | 42 % 10 = 2       | 2,3,4 occupied → try 5          | Insert at index 5 |

---

#### **3. Display**

```cpp
ht.display();
```

**Output:**

```
Hash Table:
0 --> [empty]
1 --> [empty]
2 --> 12
3 --> 22
4 --> 32
5 --> 42
6 --> [empty]
7 --> [empty]
8 --> [empty]
9 --> [empty]
```

---

#### **4. Search**

```cpp
ht.search(22); // Found
ht.search(25); // Not Found
```

**Output:**

```
Searching for 22: Found
Searching for 25: Not Found
```

---

#### **5. Remove**

```cpp
ht.remove(22);
```

Key `22` is found at index `3` → replaced by `-2` (deleted).

---

#### **6. Display again**

```cpp
ht.display();
```

**Output:**

```
Hash Table:
0 --> [empty]
1 --> [empty]
2 --> 12
3 --> [deleted]
4 --> 32
5 --> 42
6 --> [empty]
7 --> [empty]
8 --> [empty]
9 --> [empty]
```

---

### ✅ Final Program Output

Putting it all together, the program prints:

```
Hash Table:
0 --> [empty]
1 --> [empty]
2 --> 12
3 --> 22
4 --> 32
5 --> 42
6 --> [empty]
7 --> [empty]
8 --> [empty]
9 --> [empty]

Searching for 22: Found
Searching for 25: Not Found
Key 22 deleted

Hash Table:
0 --> [empty]
1 --> [empty]
2 --> 12
3 --> [deleted]
4 --> 32
5 --> 42
6 --> [empty]
7 --> [empty]
8 --> [empty]
9 --> [empty]
```

---

### 💡 Suggestions for Improvement

1. **Use constants or enums** for empty/deleted markers (`EMPTY = -1`, `DELETED = -2`) to improve readability.
2. **Dynamic resizing** could be added when the load factor gets high.
3. Handle **duplicate insertions** — currently, inserting the same key again will just place another copy.
4. Template the class to support different data types (e.g., `HashTable<T>`).

