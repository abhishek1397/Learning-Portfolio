# Efficient Range Queries using Sparse Tables (Theory)

---

## 1. What is a Sparse Table?

A **Sparse Table** is a preprocessing-based data structure used to answer **range queries** efficiently on a **static array** (i.e., the array does not change after construction).

* Designed for **immutable data**
* Enables **constant-time queries** after preprocessing
* Best suited for **idempotent operations**

---

## 2. When and Why Sparse Tables Are Used

### Use Case

Sparse Tables are used when:

* The dataset is **fixed**
* The number of range queries is **large**
* Query speed is critical

### Typical Applications

* Range Minimum Query (RMQ)
* Range Maximum Query
* Range GCD Query

---

## 3. Mathematical Properties Required

Sparse Tables rely on **two key properties** of the operation:

### 1. Associativity

The operation must satisfy:

```
op(a, op(b, c)) = op(op(a, b), c)
```

This property allows ranges to be **combined hierarchically** during preprocessing.

### 2. Idempotence (Critical)

The operation must satisfy:

```
op(x, x) = x
```

This property allows **overlapping intervals** to be used during queries **without affecting correctness**.

### Supported Operations

* Minimum
* Maximum
* GCD

### Unsupported Operations

* Sum
* XOR
* Product

These fail because overlapping elements would be counted multiple times.

---

## 4. Core Idea Behind Sparse Tables

Instead of computing answers for all possible ranges, Sparse Tables:

* Precompute answers for ranges whose lengths are **powers of two**
* Use these precomputed results to answer **any arbitrary range query**

Any range `[L, R]` can be represented using **two overlapping power-of-two intervals**.

---

## 5. Sparse Table Structure

A Sparse Table is a **2D table**:

* First dimension: **Starting index of the range**
* Second dimension: **Exponent `j`, representing range length `2^j`**

### Meaning of an Entry

An entry stores the result of the operation applied to a subarray:

```
Starting at index i
Length = 2^j
```

---

## 6. Preprocessing Strategy

### Base Level

* Ranges of length `1`
* Each entry directly corresponds to a single array element

### Higher Levels

* Larger ranges are built by **combining two smaller ranges**
* A range of length `2^j` is formed using two adjacent ranges of length `2^(j−1)`

### Key Insight

This bottom-up construction ensures all possible power-of-two ranges are available.

---

## 7. Querying a Range [L, R]

### Step 1: Determine the Range Size

Compute:

```
Length = R − L + 1
```

### Step 2: Find the Largest Power of Two

Select the largest `2^k` such that:

```
2^k ≤ (R − L + 1)
```

### Step 3: Use Two Overlapping Intervals

The query range is covered using:

1. A block of length `2^k` starting at `L`
2. A block of length `2^k` ending at `R`

These blocks **overlap**, but overlap is safe due to **idempotence**.

---

## 8. Why Overlapping Works

Overlapping intervals cause some elements to be processed twice.

* For idempotent operations:

  ```
  op(x, x) = x
  ```
* Therefore, double-counting does **not change** the result

This is the **fundamental reason** Sparse Tables work.

---

## 9. Static Nature of Sparse Tables

Sparse Tables **do not support updates efficiently**.

* Changing one element affects multiple precomputed ranges
* Updating requires rebuilding the table
* Update cost becomes `O(n log n)`

### Consequence

Sparse Tables are unsuitable for **dynamic data**.

---

## 10. Time and Space Complexity

### Preprocessing

* Time: `O(n log n)`
* Space: `O(n log n)`

### Query

* Time: `O(1)`
* Space: Constant (no extra memory per query)

---

## 11. Comparison with Other Data Structures

| Feature       | Sparse Table              | Segment Tree |
| ------------- | ------------------------- | ------------ |
| Data updates  | ❌ Not supported           | ✔️ Supported |
| Query time    | **O(1)**                  | O(log n)     |
| Preprocessing | O(n log n)                | O(n)         |
| Memory usage  | High                      | Moderate     |
| Best use case | Static data, many queries | Dynamic data |

---

## 12. Conceptual Analogy

Think of covering a long interval with **two large tiles** placed from opposite ends.

* Tiles overlap in the middle
* Overlap doesn’t matter because repeating the same operation gives the same result

This overlap strategy enables **constant-time querying**.

---

## 13. Key Takeaways (Exam-Ready)

* Sparse Tables optimize **query time** at the cost of **preprocessing and memory**
* They require **associative and idempotent operations**
* They work only on **static datasets**
* Ideal when **queries are frequent and updates are absent**

---


## Problem recap

* Array size: 1≤N≤105
* Queries:1<Q≤105
* Each query: find **maximum** in range ([L, R])
* Array (1-indexed for simplicity):

```
Index:  1  2  3  4  5  6  7  8  9
Array:  3  5 12  8 25 15 16 20  6
```

---

## Sparse Table idea

* Preprocessing time: **O(N log N)**
* Each query: **O(1)**
* Works for **static arrays** (no updates)

---

## Step 1: Build the Sparse Table

Let
`st[i][j]` = maximum value in the range starting at index `i` with length (2^j)

### Base case (j = 0)

Intervals of length (2^0 = 1)

```
st[i][0] = array[i]
```

| i | st[i][0] |
| - | -------- |
| 1 | 3        |
| 2 | 5        |
| 3 | 12       |
| 4 | 8        |
| 5 | 25       |
| 6 | 15       |
| 7 | 16       |
| 8 | 20       |
| 9 | 6        |

---

### j = 1 (length = 2)

```
st[i][1] = max(st[i][0], st[i+1][0])
```

| i | st[i][1]      |
| - | ------------- |
| 1 | max(3,5)=5    |
| 2 | max(5,12)=12  |
| 3 | max(12,8)=12  |
| 4 | max(8,25)=25  |
| 5 | max(25,15)=25 |
| 6 | max(15,16)=16 |
| 7 | max(16,20)=20 |
| 8 | max(20,6)=20  |

---

### j = 2 (length = 4)

```
st[i][2] = max(st[i][1], st[i+2][1])
```

| i | st[i][2]      |
| - | ------------- |
| 1 | max(5,12)=12  |
| 2 | max(12,25)=25 |
| 3 | max(12,25)=25 |
| 4 | max(25,16)=25 |
| 5 | max(25,20)=25 |
| 6 | max(16,20)=20 |

---

### j = 3 (length = 8)

```
st[i][3] = max(st[i][2], st[i+4][2])
```

| i | st[i][3]      |
| - | ------------- |
| 1 | max(12,25)=25 |
| 2 | max(25,20)=25 |

---

## Step 2: Precompute logarithms

Create an array `log[]` where:

```
log[i] = floor(log2(i))
```

Example:

```
log[1]=0, log[2]=1, log[3]=1, log[4]=2, log[5]=2 ...
```

---

## Step 3: Answering a Query [L, R]

Let:

```
len = R - L + 1
k = log[len]
```

Answer:

```
max( st[L][k], st[R - 2^k + 1][k] )
```

---

## Example Queries

### Query 1: L = 2, R = 6

Subarray: `[5, 12, 8, 25, 15]`

```
len = 5
k = log[5] = 2
```

Use two blocks of length (2^2 = 4):

```
max(st[2][2], st[6 - 4 + 1][2])
= max(25, 25)
= 25
```

✅ Answer: **25**

---

### Query 2: L = 4, R = 9

Subarray: `[8, 25, 15, 16, 20, 6]`

```
len = 6
k = log[6] = 2
```

```
max(st[4][2], st[9 - 4 + 1][2])
= max(25, 20)
= 25
```

✅ Answer: **25**



If you want, I can also:

* Write full C++ / Java code
* Show how to compute `log[]`
* Compare with Segment Tree
