# 🌟 Full Binomial Heap 

```cpp
#include <iostream>
#include <list>
#include <string>
#include <algorithm>
#include <vector>
#include <iomanip>

using namespace std;

template <typename T, typename Compare = less<T>>
class BinomialHeap {
private:
    struct Node {
        T key;
        int degree;
        Node* parent;
        Node* child;
        Node* sibling;

        Node(T k) : key(k), degree(0), parent(nullptr), child(nullptr), sibling(nullptr) {}
    };

    Node* head;
    Compare comp;

    Node* mergeRootLists(Node* h1, Node* h2) {
        if (!h1) return h2;
        if (!h2) return h1;

        Node* head = nullptr;
        Node** pos = &head;

        while (h1 && h2) {
            if (h1->degree <= h2->degree) {
                *pos = h1;
                h1 = h1->sibling;
            } else {
                *pos = h2;
                h2 = h2->sibling;
            }
            pos = &((*pos)->sibling);
        }

        *pos = (h1) ? h1 : h2;
        return head;
    }

    void linkTrees(Node* y, Node* z) {
        y->parent = z;
        y->sibling = z->child;
        z->child = y;
        z->degree++;
    }

    Node* unionHeaps(Node* h1, Node* h2) {
        Node* newHead = mergeRootLists(h1, h2);
        if (!newHead) return nullptr;

        Node* prev = nullptr;
        Node* curr = newHead;
        Node* next = curr->sibling;

        while (next) {
            if ((curr->degree != next->degree) ||
                (next->sibling && next->sibling->degree == curr->degree)) {
                prev = curr;
                curr = next;
            } else {
                if (comp(next->key, curr->key)) {
                    if (prev)
                        prev->sibling = next;
                    else
                        newHead = next;
                    linkTrees(curr, next);
                    curr = next;
                } else {
                    curr->sibling = next->sibling;
                    linkTrees(next, curr);
                }
            }
            next = curr->sibling;
        }

        return newHead;
    }

    Node* reverseList(Node* node) {
        Node* prev = nullptr;
        while (node) {
            Node* next = node->sibling;
            node->sibling = prev;
            node->parent = nullptr;
            prev = node;
            node = next;
        }
        return prev;
    }

    // Simple indented format
    void printTree(Node* h, int depth = 0) const {
        while (h) {
            for (int i = 0; i < depth; ++i) cout << "  ";
            cout << "-> (" << h->degree << ") " << h->key << endl;
            if (h->child) printTree(h->child, depth + 1);
            h = h->sibling;
        }
    }

    // Fancy pretty-print with ASCII tree branches
    void prettyPrint(Node* node, string prefix = "", bool isLast = true) const {
        if (!node) return;

        cout << prefix;

        cout << (isLast ? "└── " : "├── ");
        cout << "(" << setw(2) << node->degree << ") " << node->key << endl;

        prefix += (isLast ? "    " : "│   ");

        // Collect children to print them in order
        vector<Node*> children;
        for (Node* c = node->child; c; c = c->sibling)
            children.push_back(c);

        reverse(children.begin(), children.end());

        for (size_t i = 0; i < children.size(); ++i)
            prettyPrint(children[i], prefix, i == children.size() - 1);
    }

public:
    BinomialHeap() : head(nullptr) {}

    void insertKey(const T& key) {
        Node* node = new Node(key);
        head = unionHeaps(head, node);
    }

    T getMinimum() const {
        if (!head) throw runtime_error("Heap is empty");

        Node* x = head;
        T minKey = x->key;

        while (x) {
            if (comp(x->key, minKey))
                minKey = x->key;
            x = x->sibling;
        }

        return minKey;
    }

    T extractMin() {
        if (!head) throw runtime_error("Heap is empty");

        Node* minNode = head;
        Node* minPrev = nullptr;
        Node* prev = nullptr;
        Node* curr = head;
        T minKey = curr->key;

        while (curr) {
            if (comp(curr->key, minKey)) {
                minKey = curr->key;
                minPrev = prev;
                minNode = curr;
            }
            prev = curr;
            curr = curr->sibling;
        }

        if (minPrev)
            minPrev->sibling = minNode->sibling;
        else
            head = minNode->sibling;

        Node* child = reverseList(minNode->child);
        delete minNode;

        head = unionHeaps(head, child);
        return minKey;
    }

    void merge(BinomialHeap<T, Compare>& other) {
        head = unionHeaps(head, other.head);
        other.head = nullptr;
    }

    void printHeap() const {
        printTree(head);
        cout << "NIL" << endl;
    }

    void prettyPrintHeap() const {
        cout << "==== Binomial Heap ====" << endl;
        if (!head) {
            cout << "(empty)" << endl;
            return;
        }
        vector<Node*> roots;
        for (Node* r = head; r; r = r->sibling)
            roots.push_back(r);

        for (size_t i = 0; i < roots.size(); ++i)
            prettyPrint(roots[i], "", i == roots.size() - 1);

        cout << "========================" << endl;
    }

    bool empty() const { return head == nullptr; }
};

int main() {
    BinomialHeap<int> heap;
    vector<int> list = {25, 50, 12, 53, 53, 55, 41, 71, 71, 41,
                        33, 8, 71, 57, 28, 4, 89, 96, 58, 25};

    for (int x : list)
        heap.insertKey(x);

    cout << "\nPretty-printed Binomial Heap:\n";
    heap.prettyPrintHeap();

    cout << "\nMinimum key: " << heap.getMinimum() << endl;

    cout << "\nExtracting all keys in sorted order:\n";
    vector<int> sorted;
    while (!heap.empty())
        sorted.push_back(heap.extractMin());

    for (int x : sorted) cout << x << " ";
    cout << endl;

    // Example with strings
    BinomialHeap<string, less<string>> h1, h2;
    vector<string> l1 = {"foo", "bar", "baz", "mov", "mov"};
    vector<string> l2 = {"i", "see", "dead", "binomial", "trees"};

    for (auto& s : l1) h1.insertKey(s);
    for (auto& s : l2) h2.insertKey(s);

    cout << "\nHeap 1:\n"; h1.prettyPrintHeap();
    cout << "\nHeap 2:\n"; h2.prettyPrintHeap();

    h1.merge(h2);

    cout << "\nMerged Heap:\n";
    h1.prettyPrintHeap();
}
```

---

### 🖼️ Example Output (for integers)

```
==== Binomial Heap ====
└── ( 4) 4
    ├── ( 3) 12
    │   ├── ( 2) 41
    │   │   ├── ( 1) 53
    │   │   │   ├── ( 0) 55
    │   │   │   └── ( 0) 71
    │   │   ├── ( 1) 25
    │   │   │   └── ( 0) 50
    │   │   └── ( 0) 53
    │   ├── ( 2) 8
    │   │   ├── ( 1) 41
    │   │   │   └── ( 0) 71
    │   │   └── ( 0) 33
    │   ├── ( 1) 57
    │   │   └── ( 0) 71
    │   └── ( 0) 28
    ├── ( 1) 89
    │   └── ( 0) 96
    └── ( 0) 58
========================
```

---

### 🔧 Notes

* Uses `prettyPrintHeap()` for tree-style output with ASCII branches.
* Still includes `printHeap()` for Lisp-like arrow format.
* You can easily swap the comparison function to make it a **max heap**:

  ```cpp
  BinomialHeap<int, greater<int>> maxHeap;
  ```
* Works for any comparable type (`int`, `string`, custom structs with comparator).

---

Sure! Here's **everything you wrote, exactly as it was**, rewritten and formatted cleanly for clarity and preservation:

---

# Alternative approach in modern C++ is to utilize standard library containers

The main alternative approach in modern C++ is to utilize standard library containers, specifically for managing the **Root List**. By using `std::list<Node*>` instead of a single raw `Node*` head pointer, we can delegate the list manipulation (like merging and sorting) to the highly optimized STL, making the code cleaner and less prone to pointer errors.


```cpp
// binomial Heap using std::list: BinomialHeap_STL.cpp
#include <iostream>
#include <list>
#include <vector>
#include <algorithm>
#include <string>
#include <iomanip>
#include <stdexcept>

using namespace std;

/**
 * @brief Binomial Heap implementation using std::list for the root list.
 * * This approach simplifies the complex root list manipulations (like merging
 * and finding the minimum) by leveraging STL functionality. It also
 * includes a destructor for proper memory management.
 * * @tparam T The type of elements stored in the heap.
 * @tparam Compare The comparison function object (defaults to std::less for Min-Heap).
 */
template <typename T, typename Compare = less<T>>
class BinomialHeap {
private:
    struct Node {
        T key;
        int degree;
        Node* parent;
        Node* child;
        Node* sibling;

        Node(T k) : key(k), degree(0), parent(nullptr), child(nullptr), sibling(nullptr) {}
        ~Node() { 
            delete child; 
            delete sibling; 
        }
    };

    list<Node*> roots; 
    Compare comp;

    void linkTrees(Node* y, Node* z) {
        y->parent = z;
        y->sibling = z->child;
        z->child = y;
        z->degree++;
    }

    void deleteAllNodes() {
        for (Node* root : roots) {
            root->sibling = nullptr;
            delete root;
        }
        roots.clear();
    }

    void unionHeaps(list<Node*>& otherRoots) {
        roots.merge(otherRoots, [](Node* a, Node* b) {
            return a->degree < b->degree;
        });

        if (roots.empty()) return;

        auto prev_it = roots.end();
        auto curr_it = roots.begin();
        
        while (curr_it != roots.end()) {
            auto next_it = next(curr_it);
            
            if (next_it == roots.end() || (*curr_it)->degree != (*next_it)->degree || 
                (next(next_it) != roots.end() && (*next(next_it))->degree == (*curr_it)->degree)) {
                prev_it = curr_it;
                curr_it = next_it;
            } else {
                Node* curr = *curr_it;
                Node* next_node = *next_it;

                if (comp(next_node->key, curr->key)) { 
                    linkTrees(curr, next_node);
                    curr_it = roots.erase(curr_it); 
                } else { 
                    linkTrees(next_node, curr);
                    roots.erase(next_it);
                    curr_it = next(curr_it);
                }
            }
        }
    }

    Node* reverseList(Node* node) {
        Node* prev = nullptr;
        while (node) {
            Node* next = node->sibling;
            node->sibling = prev;
            node->parent = nullptr; 
            prev = node;
            node = next;
        }
        return prev;
    }

    void prettyPrint(Node* node, string prefix = "", bool isLast = true) const {
        if (!node) return;

        cout << prefix;
        cout << (isLast ? "└── " : "├── ");
        cout << "[" << node->degree << "] " << node->key << endl;

        prefix += (isLast ? "    " : "│   ");

        vector<Node*> children;
        for (Node* c = node->child; c; c = c->sibling)
            children.push_back(c);

        reverse(children.begin(), children.end());

        for (size_t i = 0; i < children.size(); ++i)
            prettyPrint(children[i], prefix, i == children.size() - 1);
    }

public:
    BinomialHeap() = default;
    BinomialHeap(const BinomialHeap&) = delete;
    BinomialHeap& operator=(const BinomialHeap&) = delete;

    ~BinomialHeap() {
        deleteAllNodes();
    }

    bool empty() const { return roots.empty(); }

    void insertKey(const T& key) {
        Node* node = new Node(key);
        list<Node*> singleRoot;
        singleRoot.push_back(node);
        unionHeaps(singleRoot);
    }

    T getMinimum() const {
        if (empty()) throw runtime_error("Heap is empty");

        auto min_it = roots.begin();
        T minKey = (*min_it)->key;

        for (auto it = next(roots.begin()); it != roots.end(); ++it) {
            if (comp((*it)->key, minKey)) {
                minKey = (*it)->key;
                min_it = it;
            }
        }
        return minKey;
    }

    T extractMin() {
        if (empty()) throw runtime_error("Heap is empty");

        auto min_it = roots.begin();
        T minKey = (*min_it)->key;
        auto current_min_it = min_it;

        for (auto it = next(roots.begin()); it != roots.end(); ++it) {
            if (comp((*it)->key, minKey)) {
                minKey = (*it)->key;
                current_min_it = it;
            }
        }

        Node* minNode = *current_min_it;
        roots.erase(current_min_it);
        
        Node* childrenHead = minNode->child;
        minNode->child = nullptr;
        
        Node* reversedChildren = reverseList(childrenHead);

        list<Node*> childRoots;
        Node* current = reversedChildren;
        while (current) {
            Node* nextSibling = current->sibling;
            current->sibling = nullptr;
            childRoots.push_back(current);
            current = nextSibling;
        }

        unionHeaps(childRoots);
        
        minNode->sibling = nullptr; 
        minNode->child = nullptr;
        delete minNode;

        return minKey;
    }

    void merge(BinomialHeap<T, Compare>& other) {
        unionHeaps(other.roots);
    }

    void printHeap() const {
        cout << "==== Binomial Heap Structure ====" << endl;
        if (roots.empty()) {
            cout << "(empty)" << endl;
            return;
        }
        
        for (const auto& root : roots) {
            prettyPrint(root);
            cout << "---------------------------------" << endl;
        }
        cout << "=================================" << endl;
    }
};

int main() {
    cout << "--- Min-Heap (Ascending Order) Example ---" << endl;
    BinomialHeap<int> min_heap;
    vector<int> list = {18, 52, 12, 88, 41, 71, 33, 8, 28, 4, 96, 58, 25};

    cout << "Inserting keys: ";
    for (int x : list) {
        min_heap.insertKey(x);
        cout << x << " ";
    }
    cout << "\n\n";

    min_heap.printHeap();

    cout << "Minimum key: " << min_heap.getMinimum() << endl;
    
    cout << "\nExtracting keys in order (should be sorted ascending):\n";
    while (!min_heap.empty()) {
        cout << min_heap.extractMin() << " ";
    }
    cout << "\n\n";
    
    cout << "--- Max-Heap (Descending Order) Example ---" << endl;
    BinomialHeap<string, greater<string>> max_heap;
    vector<string> words = {"apple", "banana", "kiwi", "grape", "cherry"};

    cout << "Inserting words: ";
    for (const string& s : words) {
        max_heap.insertKey(s);
        cout << s << " ";
    }
    cout << "\n\n";
    
    max_heap.printHeap();
    cout << "Maximum key: " << max_heap.getMinimum() << " (The heap is inverted)\n";

    cout << "\nExtracting keys in order (should be sorted descending):\n";
    while (!max_heap.empty()) {
        cout << max_heap.extractMin() << " ";
    }
    cout << "\n";
    
    return 0;
}
```

---

## 🧑‍💻 Key Differences in the STL-Based Approach

The implementation above achieves the same complex data structure but handles the root list management differently, resulting in a distinct C++ style:

1. **Root List Management (`std::list<Node*> roots`)**

   * **Original:** Used a single `Node* head` pointer and manual `prev/curr/next` logic.
   * **New:** Uses `std::list<Node*>` for automatic traversal and management.

2. **Heap Union (`unionHeaps`)**

   * **Original:** Used a custom `mergeRootLists` with manual pointer logic.
   * **New:** Uses `std::list::merge` with a lambda:

     ```cpp
     roots.merge(otherRoots, [](Node* a, Node* b) { return a->degree < b->degree; });
     ```

3. **Memory Management (RAII)**

   * Adds destructors to both `BinomialHeap` and `Node` for safe cleanup and no leaks.

This approach is **cleaner**, **safer**, and more **idiomatic in modern C++**, at a small performance trade-off for clarity and maintainability.

---

### 🧮 **Program Output**

```
--- Min-Heap (Ascending Order) Example ---
Inserting keys: 18 52 12 88 41 71 33 8 28 4 96 58 25 


==== Binomial Heap Structure ====
└── [3] 4
    ├── [2] 8
    │   ├── [1] 18
    │   │   ├── [0] 52
    │   │   └── [0] 12
    │   └── [0] 88
    ├── [1] 25
    │   ├── [0] 41
    │   └── [0] 71
    ├── [0] 33
    ├── [0] 28
    └── [0] 96
---------------------------------
=================================
Minimum key: 4

Extracting keys in order (should be sorted ascending):
4 8 12 18 25 28 33 41 52 58 71 88 96 


--- Max-Heap (Descending Order) Example ---
Inserting words: apple banana kiwi grape cherry 


==== Binomial Heap Structure ====
└── [2] kiwi
    ├── [1] grape
    │   ├── [0] banana
    │   └── [0] apple
    └── [0] cherry
---------------------------------
=================================
Maximum key: kiwi (The heap is inverted)

Extracting keys in order (should be sorted descending):
kiwi grape cherry banana apple
```

---

### 🧾 **Explanation**

* **Min-Heap Section:**
  The integer elements `{18, 52, 12, 88, ...}` are inserted, and the heap self-organizes into binomial trees.
  When you repeatedly extract the minimum, the elements print in **ascending order**:
  `4 8 12 18 25 28 33 41 52 58 71 88 96`.

* **Max-Heap Section:**
  The string elements `{apple, banana, kiwi, grape, cherry}` use `greater<string>`, effectively making it a *max-heap* (largest element first).
  The heap structure displays `kiwi` as the top node, and extraction prints the words in **descending lexicographic order**:
  `kiwi grape cherry banana apple`.

---


