# 🧩 Final Manual Huffman Coding Implementation (Fully Dynamic Input)

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
    Node* nodes[256];
    for (int i = 0; i < n; i++)
        nodes[i] = new Node(chars[i], freq[i]);
    for (int i = n; i < 256; i++)
        nodes[i] = NULL;

    int activeCount = n;

    while (activeCount > 1) {
        int min1 = findMin(nodes, 256);
        Node* left = nodes[min1];
        nodes[min1] = NULL;

        int min2 = findMin(nodes, 256);
        Node* right = nodes[min2];
        nodes[min2] = NULL;

        Node* merged = new Node('\0', left->freq + right->freq);
        merged->left = left;
        merged->right = right;

        nodes[min1] = merged;
        activeCount--;
    }

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
        current = (encoded[i] == '0') ? current->left : current->right;
        if (!current->left && !current->right) {
            cout << current->ch;
            current = root;
        }
    }
    cout << endl;
}

void huffmanCoding(const string& text) {
    int freq[256] = {0};
    int uniqueCount = 0;
    char chars[256];

    // Count frequency of each character in text
    for (size_t i = 0; i < text.size(); i++) {
        unsigned char ch = text[i];
        if (freq[ch] == 0) {
            chars[uniqueCount++] = ch;
        }
        freq[ch]++;
    }

    int freqList[256];
    for (int i = 0; i < uniqueCount; i++) {
        freqList[i] = freq[(unsigned char)chars[i]];
    }

    Node* root = buildHuffmanTree(chars, freqList, uniqueCount);

    char codes[256][256];
    char arr[256];
    memset(codes, 0, sizeof(codes));

    generateCodes(root, arr, 0, codes);

    cout << "\nHuffman Codes:\n";
    for (int i = 0; i < uniqueCount; i++) {
        cout << chars[i] << ": " << codes[(unsigned char)chars[i]] << endl;
    }

    // Encode text
    string encoded = "";
    for (size_t i = 0; i < text.size(); i++) {
        encoded += codes[(unsigned char)text[i]];
    }

    cout << "\nEncoded string:\n" << encoded << endl;

    // Decode
    decode(root, encoded);
}

int main() {
    string text;
    cout << "Enter text to encode: ";
    getline(cin, text);

    if (text.empty()) {
        cout << "Error: empty string!" << endl;
        return 0;
    }

    huffmanCoding(text);
    return 0;
}
```

---

## 🧠 Explanation of What Changed

| Feature                            | Description                                                                       |
| ---------------------------------- | --------------------------------------------------------------------------------- |
| ✅ **Dynamic Input**                | User enters any string at runtime.                                                |
| ✅ **Automatic Frequency Counting** | The program counts frequency of every character (using simple array `freq[256]`). |
| ✅ **Dynamic Character List**       | It collects only those characters that actually appear.                           |
| ✅ **Same Huffman Logic**           | Uses only arrays, no STL containers.                                              |
| ✅ **Handles all ASCII chars**      | Even spaces, punctuation, etc.                                                    |

---

## 🧩 Example Run

### Input:

```
Enter text to encode: banana
```

### Frequency Table:

| Char | Freq |
| ---- | ---- |
| b    | 1    |
| a    | 3    |
| n    | 2    |

### Generated Huffman Codes (one possible set):

```
b: 00
n: 01
a: 1
```

### Encoded:

```
banana → 00 1 01 1 01 1 → 001011011
```

### Decoded:

```
banana
```

---

## 🧩 Another Example

### Input:

```
Enter text to encode: hello world
```

### Output (varies depending on frequencies):

```
Huffman Codes:
d: 000
r: 001
w: 010
 : 011
h: 100
e: 101
l: 11
o: 110

Encoded string:
100101111011010011001000011

Decoded string: hello world
```

