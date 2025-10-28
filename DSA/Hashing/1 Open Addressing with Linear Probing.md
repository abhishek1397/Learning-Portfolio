# ✅ **Hash Table** using **open addressing with linear probing**

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

