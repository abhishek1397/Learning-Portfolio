# MIT 18.06 Lecture 3 — Matrix Multiplication and Inverse Matrices

**Professor Gilbert Strang**

---

# Part 1: Four Different Ways to Multiply Matrices

Suppose:

```text
A is an m × n matrix

B is an n × p matrix
```

Then:

```text
C = AB
```

has size:

```text
m × p
```

The inner dimensions must match:

```text
(m × n)(n × p) = (m × p)
```

---

## 1. Standard Entry-by-Entry Method (Dot Product)

Each entry of C is computed by taking:

* Row i of A
* Column j of B

Formula:

```text
C[i,j] = Σ A[i,k] * B[k,j]
```

### Example

```text
A = | a  b |
    | c  d |

B = | e  f |
    | g  h |
```

Then:

```text
AB = | ae+bg   af+bh |
     | ce+dg   cf+dh |
```

---

## 2. Column Method

Write B as columns:

```text
B = [ b₁  b₂  ...  bₚ ]
```

Then:

```text
AB = [ Ab₁  Ab₂  ...  Abₚ ]
```

### Key Idea

The j-th column of C is:

```text
cj = A * bj
```

Every column of C is a linear combination of the columns of A.

---

## 3. Row Method

Write A as rows:

```text
      | a₁ᵀ |
A  =  | a₂ᵀ |
      | ... |
      | aₘᵀ |
```

Then:

```text
       | a₁ᵀB |
AB  =  | a₂ᵀB |
       |  ... |
       | aₘᵀB |
```

### Key Idea

The i-th row of C is:

```text
Row_i(C) = Row_i(A) × B
```

Every row of C is a linear combination of rows of B.

---

## 4. Columns × Rows (Outer Product Form)

Let:

```text
A = [ a₁  a₂  ...  aₙ ]
```

where aₖ are columns of A.

Let:

```text
      | b₁ᵀ |
B  =  | b₂ᵀ |
      | ... |
      | bₙᵀ |
```

where bₖᵀ are rows of B.

Then:

```text
AB = a₁b₁ᵀ + a₂b₂ᵀ + ... + aₙbₙᵀ
```

Each term:

```text
aₖbₖᵀ
```

is an outer product.

### Example

```text
a = |1|
    |2|

bᵀ = |3  4|
```

Outer product:

```text
abᵀ = |1| |3 4|
      |2|

     = |3 4|
       |6 8|
```

---

## Bonus: Block Multiplication

Suppose:

```text
A = | A11  A12 |
    | A21  A22 |

B = | B11  B12 |
    | B21  B22 |
```

Then:

```text
AB = | A11B11 + A12B21    A11B12 + A12B22 |
     | A21B11 + A22B21    A21B12 + A22B22 |
```

Blocks behave exactly like numbers as long as dimensions are compatible.

---

# Part 2: Inverse Matrices

For a square matrix A:

```text
A⁻¹A = I = AA⁻¹
```

Identity matrix:

```text
I = |1 0|
    |0 1|
```

---

## When Does an Inverse Not Exist?

A matrix without an inverse is called **singular**.

### 1. Determinant Test

```text
det(A) = 0
```

---

### 2. Column Dependence Test

Example:

```text
A = |1 2|
    |2 4|
```

because:

```text
Column₂ = 2 × Column₁
```

Columns are linearly dependent.

---

### 3. Nullspace Test (Strang's Favorite)

If there exists a nonzero vector x such that:

```text
Ax = 0
```

then A is singular.

#### Proof

Assume A⁻¹ exists.

Multiply by A⁻¹:

```text
A⁻¹(Ax) = A⁻¹0
```

Then:

```text
Ix = 0
```

Therefore:

```text
x = 0
```

Contradiction.

Hence A⁻¹ cannot exist.

---

# Part 3: Gauss-Jordan Elimination

Find the inverse of:

```text
A = |1 3|
    |2 7|
```

Start with the augmented matrix:

```text
[A | I]

|1 3 | 1 0|
|2 7 | 0 1|
```

---

## Step 1: Eliminate Below First Pivot

Operation:

```text
R₂ ← R₂ - 2R₁
```

Result:

```text
|1 3 |  1 0|
|0 1 | -2 1|
```

---

## Step 2: Eliminate Above Second Pivot

Operation:

```text
R₁ ← R₁ - 3R₂
```

Result:

```text
|1 0 |  7 -3|
|0 1 | -2  1|
```

---

## Final Result

The left side becomes the identity matrix:

```text
[I | A⁻¹]

|1 0 |  7 -3|
|0 1 | -2  1|
```

Therefore:

```text
A⁻¹ = | 7 -3|
      |-2  1|
```

---

## Why Gauss-Jordan Works

Every row operation corresponds to multiplication by an elimination matrix E.

After all operations:

```text
EA = I
```

Therefore:

```text
E = A⁻¹
```

Applying the same operations to the identity matrix:

```text
EI = A⁻¹
```

Thus:

```text
[A | I]  →  [I | A⁻¹]
```

This is the fundamental idea behind the Gauss-Jordan method.

---

## Complete Python and C++ Implementations with Developer Notes

---

# Python Implementation (NumPy + SymPy)

## Overview

This example demonstrates:

1. Standard matrix multiplication
2. Column method
3. Row method
4. Outer-product (Columns × Rows) method
5. Matrix inverse
6. Gauss-Jordan elimination
7. Block operations

---

## Required Libraries

```bash
pip install numpy sympy
```

---

## Complete Python Code

```python
import numpy as np
import sympy as sp

# ============================================================
# MATRIX DEFINITIONS
# ============================================================

# Matrix A (3x2)
A = np.array([
    [2, 3],
    [4, 5],
    [6, 7]
])

# Matrix B (2x2)
B = np.array([
    [1, 6],
    [2, 0]
])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# ============================================================
# WAY 1: STANDARD MATRIX MULTIPLICATION
# ============================================================

print("\n==============================")
print("WAY 1: STANDARD MULTIPLICATION")
print("==============================")

C_standard = A @ B

print(C_standard)

# ============================================================
# WAY 2: COLUMN METHOD
# ============================================================

print("\n==============================")
print("WAY 2: COLUMN METHOD")
print("==============================")

columns = []

for j in range(B.shape[1]):
    bj = B[:, j]
    cj = A @ bj
    columns.append(cj)

C_column = np.column_stack(columns)

print(C_column)

# ============================================================
# WAY 3: ROW METHOD
# ============================================================

print("\n==============================")
print("WAY 3: ROW METHOD")
print("==============================")

rows = []

for i in range(A.shape[0]):
    ai = A[i, :]
    ci = ai @ B
    rows.append(ci)

C_row = np.vstack(rows)

print(C_row)

# ============================================================
# WAY 4: OUTER PRODUCT METHOD
# ============================================================

print("\n==============================")
print("WAY 4: OUTER PRODUCT METHOD")
print("==============================")

C_outer = np.zeros((A.shape[0], B.shape[1]))

for k in range(A.shape[1]):

    col_A = A[:, k]
    row_B = B[k, :]

    outer_matrix = np.outer(col_A, row_B)

    print(f"\nOuter Product {k + 1}:")
    print(outer_matrix)

    C_outer += outer_matrix

print("\nFinal Matrix:")
print(C_outer)

# ============================================================
# VERIFICATION
# ============================================================

print("\n==============================")
print("VERIFY ALL METHODS")
print("==============================")

print("Standard == Column:",
      np.array_equal(C_standard, C_column))

print("Standard == Row:",
      np.array_equal(C_standard, C_row))

print("Standard == Outer:",
      np.array_equal(C_standard, C_outer))

# ============================================================
# BLOCK OPERATIONS
# ============================================================

print("\n==============================")
print("BLOCK OPERATIONS")
print("==============================")

block = A[0:2, 0:2]

print(block)

# ============================================================
# INVERSE MATRIX
# ============================================================

print("\n==============================")
print("INVERSE MATRIX")
print("==============================")

A_inv_example = np.array([
    [1, 3],
    [2, 7]
])

A_inverse = np.linalg.inv(A_inv_example)

print(A_inverse)

# ============================================================
# GAUSS-JORDAN ELIMINATION
# ============================================================

print("\n==============================")
print("GAUSS-JORDAN ELIMINATION")
print("==============================")

augmented = sp.Matrix([
    [1, 3, 1, 0],
    [2, 7, 0, 1]
])

print("Augmented Matrix [A|I]:")
print(augmented)

rref_matrix, pivots = augmented.rref()

print("\nResult [I|A^-1]:")
print(rref_matrix)

inverse_from_rref = rref_matrix[:, 2:4]

print("\nInverse Matrix:")
print(inverse_from_rref)
```

---

# Python Developer Notes

## Matrix Dimensions

```python
A.shape
```

Returns:

```python
(rows, columns)
```

Example:

```python
A.shape
```

Output:

```python
(3, 2)
```

meaning:

```text
3 rows
2 columns
```

---

## Standard Multiplication

```python
C = A @ B
```

Equivalent to:

[
C_{ij}
======

\sum_{k=1}^{n}
A_{ik}B_{kj}
]

NumPy dispatches this operation to optimized BLAS routines.

---

## Column Method

```python
cj = A @ bj
```

Computes one output column at a time.

Lecture interpretation:

[
C =
[Ab_1;;Ab_2;;\cdots]
]

---

## Row Method

```python
ci = ai @ B
```

Computes one output row at a time.

Lecture interpretation:

[
C=
\begin{bmatrix}
a_1^TB\
a_2^TB\
\vdots
\end{bmatrix}
]

---

## Outer Product Method

```python
np.outer(col_A, row_B)
```

Computes:

[
a_k b_k^T
]

and then sums all such matrices:

[
AB
==

a_1b_1^T
+
a_2b_2^T
+\cdots
]

---

## Gauss-Jordan

```python
rref()
```

Computes Reduced Row Echelon Form.

Transforms:

[
[A|I]
]

into:

[
[I|A^{-1}]
]

---

# C++ Implementation (Eigen)

## Installation

Ubuntu:

```bash
sudo apt install libeigen3-dev
```

Compile:

```bash
g++ main.cpp -I /usr/include/eigen3 -O2
```

---

## Complete C++ Code

```cpp
#include <iostream>
#include <Eigen/Dense>

using namespace std;

int main()
{
    // =====================================================
    // MATRIX DEFINITIONS
    // =====================================================

    Eigen::Matrix<double, 3, 2> A;

    A << 2, 3,
         4, 5,
         6, 7;

    Eigen::Matrix2d B;

    B << 1, 6,
         2, 0;

    cout << "Matrix A\n";
    cout << A << "\n\n";

    cout << "Matrix B\n";
    cout << B << "\n\n";

    // =====================================================
    // WAY 1: STANDARD MULTIPLICATION
    // =====================================================

    auto C_standard = A * B;

    cout << "WAY 1\n";
    cout << C_standard << "\n\n";

    // =====================================================
    // WAY 2: COLUMN METHOD
    // =====================================================

    Eigen::Matrix<double, 3, 2> C_column;

    for(int j = 0; j < B.cols(); j++)
    {
        C_column.col(j) = A * B.col(j);
    }

    cout << "WAY 2\n";
    cout << C_column << "\n\n";

    // =====================================================
    // WAY 3: ROW METHOD
    // =====================================================

    Eigen::Matrix<double, 3, 2> C_row;

    for(int i = 0; i < A.rows(); i++)
    {
        C_row.row(i) = A.row(i) * B;
    }

    cout << "WAY 3\n";
    cout << C_row << "\n\n";

    // =====================================================
    // WAY 4: OUTER PRODUCTS
    // =====================================================

    Eigen::MatrixXd C_outer =
        Eigen::MatrixXd::Zero(3, 2);

    for(int k = 0; k < A.cols(); k++)
    {
        Eigen::Vector3d colA = A.col(k);

        Eigen::RowVector2d rowB = B.row(k);

        Eigen::MatrixXd outer =
            colA * rowB;

        cout << "Outer Product "
             << k + 1 << "\n";

        cout << outer << "\n\n";

        C_outer += outer;
    }

    cout << "WAY 4 RESULT\n";
    cout << C_outer << "\n\n";

    // =====================================================
    // VERIFY
    // =====================================================

    cout << "Verification\n";

    cout << ((C_standard == C_column)
             ? "Column OK"
             : "Column FAIL")
         << "\n";

    cout << ((C_standard == C_row)
             ? "Row OK"
             : "Row FAIL")
         << "\n\n";

    // =====================================================
    // BLOCK OPERATION
    // =====================================================

    cout << "2x2 Block from A\n";

    cout << A.block(0, 0, 2, 2)
         << "\n\n";

    // =====================================================
    // INVERSE
    // =====================================================

    Eigen::Matrix2d M;

    M << 1, 3,
         2, 7;

    cout << "Inverse\n";

    cout << M.inverse()
         << "\n\n";

    return 0;
}
```

---

# C++ Developer Notes

## Standard Multiplication

```cpp
C = A * B;
```

Uses Eigen's expression templates and optimized kernels.

---

## Column Method

```cpp
C.col(j) = A * B.col(j);
```

Computes one output column at a time.

[
c_j = Ab_j
]

---

## Row Method

```cpp
C.row(i) = A.row(i) * B;
```

Computes one output row at a time.

[
\text{Row}_i(C)
===============

\text{Row}_i(A)B
]

---

## Outer Product

```cpp
colA * rowB
```

Dimensions:

```text
(3×1)(1×2)
=
(3×2)
```

Produces:

[
a_kb_k^T
]

---

## Block Operations

```cpp
A.block(row, col, rows, cols)
```

Example:

```cpp
A.block(0,0,2,2)
```

Extracts:

```text
top-left 2×2 block
```

---

## Inverse

```cpp
M.inverse()
```

Computes:

[
A^{-1}
]

such that

[
A^{-1}A
=======

I
]

---

## Performance Notes

For production:

Prefer

```cpp
C = A * B;
```

instead of manually summing outer products.

Reason:

* Better cache locality
* SIMD vectorization
* Fewer temporary matrices
* Uses highly optimized BLAS-like kernels

The outer-product method is primarily valuable for understanding the structure of matrix multiplication and for specialized numerical algorithms.

This document gives complete, runnable Python and C++ implementations corresponding to all major concepts from MIT 18.06 Lecture 3.
