# 🧠 1. Concept of Huffman Coding

### What It Is:

**Huffman Coding** is a **lossless data compression algorithm**.
It assigns **shorter binary codes** to **frequent characters** and **longer codes** to **rare characters**.

For example:

| Character | Frequency | Binary Code |
| --------- | --------- | ----------- |
| e         | 45        | 0           |
| f         | 13        | 111         |
| a         | 5         | 1100        |
| b         | 9         | 1101        |
| c         | 12        | 10          |

*(Codes are for illustration only — real output depends on tree shape.)*

### How It Works:

1. **Create a leaf node** for each character with its frequency.
2. **Insert all nodes** into a **min-heap** (priority queue) ordered by frequency.
3. **Repeat until one node remains**:

   * Extract two nodes with the **lowest frequencies**.
   * Create a new internal node with their combined frequency.
   * This new node’s left and right children are the two extracted nodes.
   * Push it back into the heap.
4. The final remaining node is the **root of the Huffman tree**.
5. Traverse:

   * Going **left → add '0'**
   * Going **right → add '1'**
   * Each leaf node’s path forms that character’s **Huffman code**.

---

## Given: Frequency 
---

## 🧩 2. Refined Code (clean, minimal, and explained)

```cpp
#include <iostream>
#include <queue>
#include <cstring>
using namespace std;

struct Node {
    char ch;
    int freq;
    Node *left, *right;
    Node(char c, int f) : ch(c), freq(f), left(NULL), right(NULL) {}
};

// Custom comparator for priority queue (min-heap)
struct Compare {
    bool operator()(Node* a, Node* b) {
        return a->freq > b->freq;
    }
};

// Build Huffman Tree
Node* buildHuffmanTree(char chars[], int freq[], int n) {
    priority_queue<Node*, vector<Node*>, Compare> pq;

    // Step 1: Push all characters into min-heap
    for (int i = 0; i < n; i++)
        pq.push(new Node(chars[i], freq[i]));

    // Step 2: Build the tree
    while (pq.size() > 1) {
        Node* left = pq.top(); pq.pop();
        Node* right = pq.top(); pq.pop();

        Node* merged = new Node('\0', left->freq + right->freq);
        merged->left = left;
        merged->right = right;
        pq.push(merged);
    }

    return pq.top(); // root node
}

// Generate Huffman Codes recursively
void generateCodes(Node* root, string code, char codes[256][256]) {
    if (!root) return;

    // If it's a leaf node (character node)
    if (!root->left && !root->right) {
        strcpy(codes[(unsigned char)root->ch], code.c_str());
        return;
    }

    generateCodes(root->left, code + "0", codes);
    generateCodes(root->right, code + "1", codes);
}

// Decode encoded string
void decode(Node* root, const string &encodedStr) {
    Node* current = root;
    cout << "\nDecoded string: ";

    for (char bit : encodedStr) {
        current = (bit == '0') ? current->left : current->right;

        if (!current->left && !current->right) {
            cout << current->ch;
            current = root;
        }
    }
    cout << endl;
}

// Main function to perform Huffman Encoding and Decoding
void huffmanCoding(char chars[], int freq[], int n, const string& textToEncode) {
    Node* root = buildHuffmanTree(chars, freq, n);

    char codes[256][256];
    memset(codes, 0, sizeof(codes));

    generateCodes(root, "", codes);

    cout << "Huffman Codes:\n";
    for (int i = 0; i < n; i++)
        cout << chars[i] << ": " << codes[(unsigned char)chars[i]] << endl;

    string encoded = "";
    for (char ch : textToEncode)
        encoded += codes[(unsigned char)ch];

    cout << "\nEncoded string:\n" << encoded << endl;
    decode(root, encoded);
}

int main() {
    char chars[] = { 'a', 'b', 'c', 'd', 'e', 'f' };
    int freq[] = { 5, 9, 12, 13, 16, 45 };
    int n = sizeof(chars) / sizeof(chars[0]);

    string textToEncode = "abcdef";
    cout << "Text to encode: " << textToEncode << "\n\n";

    huffmanCoding(chars, freq, n, textToEncode);
    return 0;
}
```

## 🧩 Full Manual Implementation (No STL queue, vector)

```cpp
#include <iostream>
#include <cstring>
using namespace std;

struct Node {
    char ch;
    int freq;
    Node *left, *right;
    Node(char c, int f) : ch(c), freq(f), left(NULL), right(NULL) {}
};

// Find index of smallest frequency node that is not NULL
int findMin(Node* nodes[], int n) {
    int minIndex = -1;
    for (int i = 0; i < n; i++) {
        if (nodes[i] != NULL) {
            if (minIndex == -1 || nodes[i]->freq < nodes[minIndex]->freq)
                minIndex = i;
        }
    }
    return minIndex;
}

// Build Huffman Tree manually
Node* buildHuffmanTree(char chars[], int freq[], int n) {
    Node* nodes[256];  // support up to 256 chars
    for (int i = 0; i < n; i++)
        nodes[i] = new Node(chars[i], freq[i]);
    for (int i = n; i < 256; i++)
        nodes[i] = NULL;

    int activeCount = n; // active nodes count

    while (activeCount > 1) {
        // find smallest 1
        int min1 = findMin(nodes, 256);
        Node* left = nodes[min1];
        nodes[min1] = NULL;

        // find smallest 2
        int min2 = findMin(nodes, 256);
        Node* right = nodes[min2];
        nodes[min2] = NULL;

        // merge them
        Node* merged = new Node('\0', left->freq + right->freq);
        merged->left = left;
        merged->right = right;

        // store merged node in place of one of them
        nodes[min1] = merged;
        activeCount--;
    }

    // return last non-null node
    for (int i = 0; i < 256; i++)
        if (nodes[i] != NULL)
            return nodes[i];
    return NULL;
}

// Recursively generate Huffman codes
void generateCodes(Node* root, char code[], int top, char codes[256][256]) {
    if (root->left) {
        code[top] = '0';
        generateCodes(root->left, code, top + 1, codes);
    }
    if (root->right) {
        code[top] = '1';
        generateCodes(root->right, code, top + 1, codes);
    }

    // If leaf node
    if (!root->left && !root->right) {
        code[top] = '\0';
        strcpy(codes[(unsigned char)root->ch], code);
    }
}

// Decode encoded string using the Huffman Tree
void decode(Node* root, const string& encoded) {
    Node* current = root;
    cout << "\nDecoded string: ";
    for (size_t i = 0; i < encoded.size(); i++) {
        if (encoded[i] == '0')
            current = current->left;
        else
            current = current->right;

        if (!current->left && !current->right) {
            cout << current->ch;
            current = root;
        }
    }
    cout << endl;
}

void huffmanCoding(char chars[], int freq[], int n, const string& text) {
    Node* root = buildHuffmanTree(chars, freq, n);

    char codes[256][256];
    char arr[256];
    memset(codes, 0, sizeof(codes));

    generateCodes(root, arr, 0, codes);

    cout << "Huffman Codes:\n";
    for (int i = 0; i < n; i++)
        cout << chars[i] << ": " << codes[(unsigned char)chars[i]] << endl;

    // Encode text
    string encoded = "";
    for (size_t i = 0; i < text.size(); i++)
        encoded += codes[(unsigned char)text[i]];

    cout << "\nEncoded string:\n" << encoded << endl;

    // Decode
    decode(root, encoded);
}

int main() {
    char chars[] = { 'a', 'b', 'c', 'd', 'e', 'f' };
    int freq[] = { 5, 9, 12, 13, 16, 45 };
    int n = sizeof(chars) / sizeof(chars[0]);

    string text = "abcdef";
    cout << "Text to encode: " << text << "\n\n";

    huffmanCoding(chars, freq, n, text);
    return 0;
}


---

## 🖼️ 3. Visual Explanation of Output

### Given input:

```
chars = {a, b, c, d, e, f}
freq  = {5, 9, 12, 13, 16, 45}
textToEncode = "abcdef"
```

---

### Step 1. Build Huffman Tree

We start with leaf nodes:

```
a(5), b(9), c(12), d(13), e(16), f(45)
```

**Process:**

1️⃣ Combine smallest (a=5) + (b=9) → Node(14)
Heap: [c(12), d(13), e(16), f(45), 14]

2️⃣ Combine smallest (c=12) + (d=13) → Node(25)
Heap: [14, e(16), f(45), 25]

3️⃣ Combine smallest (14) + (e=16) → Node(30)
Heap: [25, f(45), 30]

4️⃣ Combine smallest (25) + (30) → Node(55)
Heap: [f(45), 55]

5️⃣ Combine last two (f=45) + (55) → Node(100) = Root

---

### Step 2. Huffman Tree (schematic)

```
                [100]
               /     \
          [45:f]     [55]
                    /    \
                 [25]    [30]
                /   \    /   \
           [12:c][13:d][14] [16:e]
                        / \
                    [5:a][9:b]
```

---

### Step 3. Generate Codes

Follow **Left = 0**, **Right = 1**:

| Character | Code |
| --------- | ---- |
| f         | 0    |
| c         | 100  |
| d         | 101  |
| a         | 1100 |
| b         | 1101 |
| e         | 111  |

---

### Step 4. Encoding `abcdef`

```
a → 1100
b → 1101
c → 100
d → 101
e → 111
f → 0
-----------------
Encoded = 110011011001011110
```

---

### Step 5. Decoding

The code `110011011001011110` is traversed bit by bit along the tree:

* `1100` → a
* `1101` → b
* `100`  → c
* `101`  → d
* `111`  → e
* `0`    → f

✅ **Decoded Output:** `abcdef`

---

## 🧩 Final Output Example

```
Text to encode: abcdef

Huffman Codes:
a: 1100
b: 1101
c: 100
d: 101
e: 111
f: 0

Encoded string:
110011011001011110

Decoded string: abcdef
```

---

Would you like me to also show a **step-by-step heap state visualization** (how the priority queue changes at each iteration)? That makes it crystal clear how merging happens.
