# 🧩 The Function Call Flow (Bird’s Eye View)

```
main()
 │
 ▼
huffmanCoding(text)
 │
 ├──► Step 1: Count frequencies
 │       └── fills → freq[], chars[], uniqueCount
 │
 ├──► Step 2: Prepare freqList[]
 │       └── maps each unique char → frequency
 │
 ├──► Step 3: Build Huffman Tree
 │       └── buildHuffmanTree(chars, freqList, uniqueCount)
 │             │
 │             ├── creates → Node objects for each char
 │             ├── findMin() → find 2 smallest frequency nodes
 │             ├── merges → left + right into parent
 │             └── returns → root node of Huffman tree
 │
 ├──► Step 4: Initialize codes[][] and temp array arr[]
 │       └── memset(codes, 0, sizeof(codes))
 │
 ├──► Step 5: Generate Huffman Codes
 │       └── generateCodes(root, arr, 0, codes)
 │             │
 │             ├── recursively traverse tree
 │             ├── add '0' for left, '1' for right
 │             └── when leaf → copy arr[] → codes[ch]
 │
 ├──► Step 6: Encode input text
 │       └── builds encoded string using codes[][]
 │
 └──► Step 7: Decode encoded string
         └── decode(root, encoded)
              │
              ├── traverse tree using bits ('0'→left, '1'→right)
              └── reconstruct original text
```

---

## 🧠 Detailed Visual Flow (Tree Diagram)

```
┌────────────────────────────────────────────────────┐
│                    main()                          │
└────────────────────────────────────────────────────┘
                         │
                         ▼
        ┌────────────────────────────────┐
        │        huffmanCoding(text)      │
        └────────────────────────────────┘
           │
           ├── Count frequency → fills freq[], chars[], uniqueCount
           │
           ├── Create freqList[i] = freq[chars[i]]
           │
           ├── Build Huffman Tree
           │      ▼
           │  ┌───────────────────────────────┐
           │  │ buildHuffmanTree(chars, freq, n) │
           │  └───────────────────────────────┘
           │       │
           │       ├── create Node for each char
           │       ├── findMin() twice
           │       │       ┌──────────────────────┐
           │       │       │ findMin(nodes, n)    │
           │       │       └──────────────────────┘
           │       ├── merge two smallest → new node
           │       └── repeat until one node left
           │
           ├── returns root → Node* root
           │
           ├── memset(codes, 0, sizeof(codes))
           │
           ├── Generate codes recursively
           │      ▼
           │  ┌──────────────────────────────────┐
           │  │ generateCodes(root, arr, 0, codes) │
           │  └──────────────────────────────────┘
           │       ├── go left → add '0'
           │       ├── go right → add '1'
           │       └── leaf → save code for character
           │
           ├── Encode input using codes[ch]
           │
           └── Decode back using tree
                  ▼
           ┌────────────────────────────┐
           │ decode(root, encodedText)  │
           └────────────────────────────┘
                   ├── read bit → move left/right
                   └── output character at leaf
```

---

## ⚙️ Data Flow Summary

| Function               | Input                        | Output                    | Purpose                   |
| ---------------------- | ---------------------------- | ------------------------- | ------------------------- |
| **huffmanCoding()**    | text (string)                | encoded + decoded output  | Main controller           |
| **buildHuffmanTree()** | chars[], freq[], uniqueCount | root (Node*)              | Build Huffman Tree        |
| **findMin()**          | nodes[], size                | index of smallest freq    | Helper for tree merge     |
| **generateCodes()**    | root, arr[], codes[][]       | fills codes for all chars | Recursive code generation |
| **decode()**           | root, encoded string         | decoded text              | Reverse the encoding      |

---

## 🧩 How Everything Connects

```
+---------------------------------------------------+
|                 huffmanCoding()                   |
|---------------------------------------------------|
|   ↓ count frequency → freq[], chars[]             |
|   ↓ prepare freqList[]                            |
|   ↓ buildHuffmanTree(chars, freqList, n) → root   |
|   ↓ generateCodes(root, arr, 0, codes)            |
|   ↓ encode text using codes                       |
|   ↓ decode(root, encoded)                         |
+---------------------------------------------------+
```

Each function builds on the result of the previous one — forming a **pipeline** like this:

```
Text → Frequencies → Huffman Tree → Codes → Encoded String → Decoded Text
```

---

## 🧠 TL;DR (Summary of Roles)

| Step | Function             | Core Task                                         |
| ---- | -------------------- | ------------------------------------------------- |
| 1    | `huffmanCoding()`    | Controls everything                               |
| 2    | Frequency loop       | Builds `freq[]`, `chars[]`, `uniqueCount`         |
| 3    | `buildHuffmanTree()` | Creates Huffman tree using Node struct            |
| 4    | `findMin()`          | Finds smallest frequency nodes for merging        |
| 5    | `generateCodes()`    | Recursively assigns 0/1 codes to each character   |
| 6    | Encoding loop        | Converts text → binary Huffman string             |
| 7    | `decode()`           | Converts binary string → original text using tree |

---

