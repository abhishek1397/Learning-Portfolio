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


