# 🧠 Huffman Coding Theory

It is based on the idea of using **variable-length prefix codes** to represent characters in a way that minimizes the total number of bits used. Huffman coding is a lossless data compression algorithm that assigns shorter codes to more frequent characters and longer codes to less frequent ones. Below is a detailed explanation followed by Python code and its breakdown.

### Key Concepts:
- **Prefix Code**: No code is a prefix of another. This ensures unambiguous decoding.
- **Frequency-Based**: Characters with higher frequency get shorter codes.
- **Binary Tree**: Huffman coding builds a binary tree where each leaf node represents a character.

### Steps:
1. **Count frequency** of each character in the input.
2. **Build a priority queue** (min-heap) of nodes based on frequency.
3. **Construct the Huffman Tree**:
   - Remove two nodes with the lowest frequency.
   - Create a new node with these two as children and combined frequency.
   - Repeat until one node remains (the root).
4. **Generate codes** by traversing the tree:
   - Left edge → add '0'
   - Right edge → add '1'
5. **Encode the input** using the generated codes.
6. **Decode** using the tree.

---

## 🧑‍💻 Huffman Coding in Python

```cpp
#include <iostream>
using namespace std;

const int MAX = 100;

struct Node {
    char ch;
    int freq;
    Node* left;
    Node* right;
};

// Create a node
Node* createNode(char ch, int freq, Node* left = nullptr, Node* right = nullptr) {
    Node* node = new Node;
    node->ch = ch;
    node->freq = freq;
    node->left = left;
    node->right = right;
    return node;
}

// Find two smallest nodes
void findTwoMin(Node* arr[], int size, int& min1, int& min2) {
    min1 = min2 = -1;
    for (int i = 0; i < size; ++i) {
        if (arr[i] == nullptr) continue;
        if (min1 == -1 || arr[i]->freq < arr[min1]->freq) {
            min2 = min1;
            min1 = i;
        } else if (min2 == -1 || arr[i]->freq < arr[min2]->freq) {
            min2 = i;
        }
    }
}

// Build Huffman Tree
Node* buildTree(char chars[], int freqs[], int n) {
    Node* arr[MAX] = {nullptr};
    for (int i = 0; i < n; ++i)
        arr[i] = createNode(chars[i], freqs[i]);

    int size = n;
    while (true) {
        int i, j;
        findTwoMin(arr, size, i, j);
        if (j == -1) break;

        Node* merged = createNode('\0', arr[i]->freq + arr[j]->freq, arr[i], arr[j]);
        arr[i] = merged;
        arr[j] = nullptr;
    }

    for (int i = 0; i < size; ++i)
        if (arr[i]) return arr[i];
    return nullptr;
}

// Print Huffman Codes
void printCodes(Node* root, char code[], int depth) {
    if (!root) return;
    if (root->ch != '\0') {
        cout << root->ch << ": ";
        for (int i = 0; i < depth; ++i)
            cout << code[i];
        cout << endl;
    }
    code[depth] = '0';
    printCodes(root->left, code, depth + 1);
    code[depth] = '1';
    printCodes(root->right, code, depth + 1);
}

int main() {
    char chars[] = {'a', 'b', 'c', 'd', 'e'};
    int freqs[] = {5, 9, 12, 13, 16};
    int n = sizeof(chars) / sizeof(chars[0]);

    Node* root = buildTree(chars, freqs, n);
    char code[MAX];
    cout << "Huffman Codes:\n";
    printCodes(root, code, 0);

    return 0;
}
```

---

## 🔍 Code Explanation

- **Node struct**: Represents a character and its frequency, plus left/right children.
- **createNode**: Allocates and initializes a node.
- **findTwoMin**: Finds indices of two nodes with smallest frequencies in the array.
- **buildTree**:
  - Initializes an array of nodes.
  - Repeatedly merges two smallest nodes until one remains.
- **printCodes**:
  - Recursively traverses the tree.
  - Builds the binary code in a `char[]` array.
  - Prints code when a leaf node is reached.

---
