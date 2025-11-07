# ✅ Hash Table using Open Addressing with Quadratic Probing

---

### 🧠 What is Open Addressing?
Open addressing is a collision-resolution strategy in hash tables where all elements are stored in the same array. When a collision occurs (two keys hash to the same index), the algorithm searches for another open slot within the array using a probing sequence.

---

### 🔁 What is Quadratic Probing?
Quadratic probing is a type of open addressing where the interval between probes increases quadratically. Instead of checking the next slot (as in linear probing), it checks slots at increasing distances:

### 🔹 Formula
If \( h(k) \) is the hash function and a collision occurs, we probe:

\[
h(k),\ (h(k) + 1^2) \% capacity,\ (h(k) + 2^2) \% capacity,\ (h(k) + 3^2) \% capacity,\ \ldots
\]

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
 ├── HashTable ht
 │      └── HashTable()              # constructor
 │
 ├── ht.insert()
 │      ├── hashFunction()
 │      └── quadratic probing loop
 │
 ├── ht.insert()
 │      ├── hashFunction()
 │      └── quadratic probing loop
 │
 ├── ht.insert()
 │      ├── hashFunction()
 │      └── quadratic probing loop
 │
 ├── ht.insert()
 │      ├── hashFunction()
 │      └── quadratic probing loop
 │
 ├── ht.display()
 │      └── print table
 │
 ├── ht.search()
 │      ├── hashFunction()
 │      └── probing loop
 │
 ├── ht.search()
 │      ├── hashFunction()
 │      └── probing loop
 │
 ├── ht.remove()
 │      ├── hashFunction()
 │      └── probing loop
 │
 ├── ht.display()
 │      └── print table
 │
 └── ~HashTable()                   # destructor
        └── delete[] table
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
        int index = hashFunction(key);
        int i = 0;

        while (i < capacity) {
            int probeIndex = (index + i * i) % capacity;
            if (table[probeIndex] == EMPTY)
                return false;
            if (table[probeIndex] == key)
                return true;
            i++;
        }

        return false;
    }

    // Remove using quadratic probing
    void remove(int key) {
        int index = hashFunction(key);
        int i = 0;

        while (i < capacity) {
            int probeIndex = (index + i * i) % capacity;
            if (table[probeIndex] == EMPTY)
                break;
            if (table[probeIndex] == key) {
                table[probeIndex] = DELETED;
                currentSize--;
                cout << "Key " << key << " deleted\n";
                return;
            }
            i++;
        }

        cout << "Key " << key << " not found\n";
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

---

### 🧩 Step-by-step Execution

#### 1. Creation
```cpp
HashTable ht;
```
Creates a table of size 10 initialized with -1 (empty).

#### 2. Insertions
```cpp
ht.insert(12); // h(12) = 2 → insert at 2
ht.insert(22); // h(22) = 2 → 2 occupied → try 3 → insert at 3
ht.insert(32); // h(32) = 2 → 2,3 occupied → try 6 → insert at 6
ht.insert(42); // h(42) = 2 → 2,3,6 occupied → try 1 → insert at 1
```

#### 3. Display
```cpp
ht.display();
```

**Output:**
```
0 --> [empty]
1 --> 42
2 --> 12
3 --> 22
4 --> [empty]
5 --> [empty]
6 --> 32
7 --> [empty]
8 --> [empty]
9 --> [empty]
```

#### 4. Search
```cpp
ht.search(22); // Found
ht.search(25); // Not Found
```

#### 5. Remove
```cpp
ht.remove(22); // Mark index 3 as deleted
```

#### 6. Display again
```cpp
ht.display();
```

**Output:**
```
0 --> [empty]
1 --> 42
2 --> 12
3 --> [deleted]
4 --> [empty]
5 --> [empty]
6 --> 32
7 --> [empty]
8 --> [empty]
9 --> [empty]
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


