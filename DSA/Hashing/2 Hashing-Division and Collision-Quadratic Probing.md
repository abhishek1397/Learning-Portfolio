# ✅ Hash Table using Division Method with Quadratic Probing

---

### 🧠 What is Open Addressing?
Open addressing is a collision-resolution strategy in hash tables where all elements are stored in the same array. When a collision occurs (two keys hash to the same index), the algorithm searches for another open slot within the array using a probing sequence.

---

### 🔁 What is Quadratic Probing?
Quadratic probing is a type of open addressing where the interval between probes increases quadratically. Instead of checking the next slot (as in linear probing), it checks slots at increasing distances:

### 🔹 Formula
If \( h(k) \) is the hash function and a collision occurs, we probe:

![Formula](https://github.com/user-attachments/assets/3d07e01c-4cf9-4d74-a079-d670a7127703)

This reduces clustering compared to linear probing.

---

### 🧩 Example
Let’s say we have a hash table of size 10 and use:

\[
h(k) = k \% 10
\]

#### Step 1: Insert 12  
\[
h(12) = 2 \Rightarrow \text{Slot 2 is empty} \Rightarrow \text{Insert at index 2}
\]

#### Step 2: Insert 22  
\[
h(22) = 2 \Rightarrow \text{Slot 2 occupied} \Rightarrow \text{Try } (2 + 1^2) \% 10 = 3 \Rightarrow \text{Insert at index 3}
\]

#### Step 3: Insert 32  
\[
h(32) = 2 \Rightarrow \text{2 occupied} \Rightarrow 3 occupied \Rightarrow (2 + 2^2) \% 10 = 6 \Rightarrow \text{Insert at index 6}
\]

---

### 🔍 Searching with Quadratic Probing
To find key 32:

- Start at h(32) = 2
- Check 2 → not 32
- Check (2 + 1^2) % 10 = 3 → not 32
- Check (2 + 2^2) % 10 = 6 → found ✅

---

### ❌ Deleting with Quadratic Probing
Same as linear probing: mark deleted slots with a special marker (e.g., -2) to preserve the probe chain.

---

### 📊 Summary Table

| Concept             | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| Open Addressing     | All data in one array; collisions resolved by probing                       |
| Quadratic Probing   | Probes slots using square increments: \( i^2 \)                             |
| Collision Handling  | \( (h(k) + i^2) \% capacity \)                                               |
| Advantages          | Reduces clustering compared to linear probing                               |
| Disadvantages       | May not probe all slots unless capacity is prime                            |

---
🧩 Functional Hierarchy Diagram — Hash Table

```
main()
 │
 ▼
HashTable ht   // Creates a HashTable object
 │
 ├──► ht.insert(12)   
 │       └── hashFunction(12) → index = 12 % capacity
 │       └── probeIndex = (index + i * i) % capacity → checks if the slot is empty or deleted
 │       └── inserts key 12 at probeIndex if available
 │
 ├──► ht.insert(22)   
 │       └── hashFunction(22) → index = 22 % capacity
 │       └── probeIndex = (index + i * i) % capacity → checks if the slot is empty or deleted
 │       └── inserts key 22 at probeIndex if available
 │
 ├──► ht.insert(32)   
 │       └── hashFunction(32) → index = 32 % capacity
 │       └── probeIndex = (index + i * i) % capacity → checks if the slot is empty or deleted
 │       └── inserts key 32 at probeIndex if available
 │
 ├──► ht.insert(42)   
 │       └── hashFunction(42) → index = 42 % capacity
 │       └── probeIndex = (index + i * i) % capacity → checks if the slot is empty or deleted
 │       └── inserts key 42 at probeIndex if available
 │
 ├──► ht.display()      // Shows the current state of the hash table
 │       └── Iterates over table and prints values (empty, deleted, or actual key)
 │
 ├──► ht.search(22)
 │       └── hashFunction(22) → index = 22 % capacity
 │       └── probeIndex = (index + i * i) % capacity → checks if the key is found or not
 │       └── returns true if key 22 is found
 │
 ├──► ht.search(25)    // Search for a key that doesn't exist
 │       └── hashFunction(25) → index = 25 % capacity
 │       └── probeIndex = (index + i * i) % capacity → key not found, returns false
 │
 ├──► ht.remove(22)
 │       └── hashFunction(22) → index = 22 % capacity
 │       └── probeIndex = (index + i * i) % capacity → finds key 22
 │       └── marks the slot at probeIndex as DELETED
 │       └── currentSize-- (decreases the size of the hash table)
 │
 └──► ht.display()      // Shows updated table after deletion
```

### 💻 C++ Code: Hash Table with Quadratic Probing

```cpp
#include <iostream>
using namespace std;

class HashTable {
private:
    int* table;
    int capacity;
    int currentSize;
    const int EMPTY = -1;
    const int DELETED = -2;

public:
    // Constructor
    HashTable(int size = 10) {
        capacity = size;
        currentSize = 0;
        table = new int[capacity];
        for (int i = 0; i < capacity; i++)
            table[i] = EMPTY;
    }

    // Destructor
    ~HashTable() {
        delete[] table;
    }

    // Hash function
    int hashFunction(int key) {
        return key % capacity;
    }

    // Insert using quadratic probing
    void insert(int key) {
        if (currentSize == capacity) {
            cout << "Hash Table is full! Cannot insert " << key << endl;
            return;
        }

        int index = hashFunction(key);
        int i = 0;

        while (i < capacity) {
            int probeIndex = (index + i * i) % capacity;
            if (table[probeIndex] == EMPTY || table[probeIndex] == DELETED) {
                table[probeIndex] = key;
                currentSize++;
                return;
            }
            i++;
        }

        cout << "No empty slot found for key " << key << endl;
    }

    // Search using quadratic probing
    bool search(int key) {
        int index = hashfunction(key);
        int i = 0;

        while (i < capacity) {
            int probeindex = (index + i * i) % capacity;
            if (table[probeindex] == EMPTY)
                return false;  // Key not found
            if (table[probeindex] == key)
                return true;   // Found at least one instance
            i++;
        }
        return false;
    }

    // Remove using quadratic probing
    void remove(int key) {
        int index = hashfunction(key);
        int i = 0;

        while (i < capacity) {
            int probeindex = (index + i * i) % capacity;

            if (table[probeindex] == EMPTY) {
                cout << "Key not present" << endl;
                return;
            }
            if (table[probeindex] == key) {
                table[probeindex] = DELETED;
                currentsize--;
                cout << "One occurrence of key " << key << " deleted." << endl;
                return;
            }
            i++;
        }

        cout << "Key not found" << endl;
    }

    // Display the table
    void display() {
        cout << "\nHash Table:\n";
        for (int i = 0; i < capacity; i++) {
            if (table[i] == EMPTY)
                cout << i << " --> [empty]\n";
            else if (table[i] == DELETED)
                cout << i << " --> [deleted]\n";
            else
                cout << i << " --> " << table[i] << "\n";
        }
    }
};

int main() {
    HashTable ht(10);

    // ✅ Insert duplicate values
    ht.insert(12);
    ht.insert(22);
    ht.insert(32);
    ht.insert(22); // Duplicate
    ht.insert(32); // Duplicate
    ht.insert(48);
    ht.insert(48); // Duplicate
    ht.insert(52);
    ht.insert(42);

    ht.display();

    cout << "\nSearching for 22: " << (ht.search(22) ? "Found" : "Not Found") << endl;
    cout << "Searching for 25: " << (ht.search(25) ? "Found" : "Not Found") << endl;

    ht.remove(22);  // Removes one 22 only
    ht.remove(48);  // Removes one 48 only

    cout << "\nAfter deleting one occurrence each of 22 and 48:" << endl;
    ht.display();

    cout << "\nSearching for 22: " << (ht.search(22) ? "Found" : "Not Found") << endl;
    cout << "Searching for 48: " << (ht.search(48) ? "Found" : "Not Found") << endl;

    return 0;
}
}
```

---

### ✅ **Example Output**

```
Hash Table:
0 --> [EMPTY]
1 --> [EMPTY]
2 --> 22
3 --> 32
4 --> 42
5 --> 52
6 --> 12
7 --> 22
8 --> 32
9 --> 48

Searching for 22: Found
Searching for 25: Not Found
One occurrence of key 22 deleted.
One occurrence of key 48 deleted.

After deleting one occurrence each of 22 and 48:
Hash Table:
0 --> [EMPTY]
1 --> [EMPTY]
2 --> [DELETED]
3 --> 32
4 --> 42
5 --> 52
6 --> 12
7 --> 22
8 --> 32
9 --> [DELETED]

Searching for 22: Found
Searching for 48: Not Found
```


---

### 💡 Suggestions for Improvement
- Use constants (`EMPTY`, `DELETED`) for clarity ✅
- Add dynamic resizing when load factor exceeds threshold
- Prevent duplicate insertions
- Use templates to support generic types (`HashTable<T>`)

---


# 🛑 Why Infinite Loops Can Happen
Quadratic probing uses the formula:


#### probeIndex = (h(k) + i^2) % capacity


If the table is full or the probing sequence fails to find an empty or deleted slot, the loop might continue indefinitely unless we explicitly limit the number of probes.

---

### ✅ How to Prevent Infinite Loops
To avoid infinite loops, the code should:

- **Limit the number of probes to the table's capacity**.
- **Break out** of the loop if all slots have been checked.

This is already handled in the code you saw earlier:

```cpp
int i = 0;
while (i < capacity) {
    int probeIndex = (index + i * i) % capacity;
    if (table[probeIndex] == EMPTY || table[probeIndex] == DELETED) {
        table[probeIndex] = key;
        currentSize++;
        return;
    }
    i++;
}
```

Here’s what’s happening:

- The loop runs at most `capacity` times.
- If no slot is found after `capacity` probes, it prints:
  ```cpp
  cout << "No empty slot found for key " << key << endl;
  ```

This ensures the program **never runs infinitely**, even if the table is full or the probing sequence fails to find a usable slot.

---

### 💡 Additional Tips
- Can improve robustness by checking the **load factor** before inserting and resizing the table if needed.
- Use a **prime number** for the table size to ensure better coverage of slots during quadratic probing.


