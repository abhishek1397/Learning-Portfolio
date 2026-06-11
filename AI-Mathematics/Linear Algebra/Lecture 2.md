#  **MIT 18.06 Lecture 2: Elimination with Matrices**, taught by Professor Gilbert Strang.

---

### 1. The Goal: Forward Elimination ($A \rightarrow U$)

The lecture focuses on solving a system of linear equations $Ax = b$ using **Gaussian Elimination**. Rather than using determinants (which are mathematically inefficient for computers), elimination systematically simplifies a matrix into an upper triangular structure.

#### The Working Example:

Professor Strang introduces a $3 \times 3$ system of equations:

$$
\begin{aligned}
x + 2y + z &= 2 \\
3x + 8y + z &= 12 \\
4y + z &= 2
\end{aligned}
\quad \rightarrow \quad
A =
\begin{bmatrix}
1 & 2 & 1 \\
3 & 8 & 1 \\
0 & 4 & 1
\end{bmatrix},
\qquad
b =
\begin{bmatrix}
2 \\
12 \\
2
\end{bmatrix}
$$

#### Step-by-Step Breakdown:

1. **First Pivot ($1,1$ position):** The value at $(1,1)$ is $\mathbf{1}$ (pivots cannot be zero).
2. **Eliminating the 2,1 position:** To eliminate the $3x$ from the second row, we subtract $3 \times (\text{Row 1})$ from $\text{Row 2}$.
* **Multiplier:** $3$.
* This leaves a $0$ at the $(2,1)$ entry.


3. **Eliminating the 3,1 position:** The $(3,1)$ entry is already $0$, so no modification is needed (multiplier is $0$).
4. **Second Pivot ($2,2$ position):** The new matrix has a value of $\mathbf{2}$ at position $(2,2)$. This becomes our second pivot.
5. **Eliminating the 3,2 position:** The value below our second pivot is $4$. We subtract $2 \times (\text{Row 2})$ from $\text{Row 3}$.
* **Multiplier:** $2$.



#### The Resulting Upper Triangular Matrix ($U$):

After forward elimination, matrix $A$ becomes **$U$ (Upper Triangular)**:

$$
U =
\begin{bmatrix}
\mathbf{1} & 2 & 1 \\
0 & \mathbf{2} & -2 \\
0 & 0 & \mathbf{5}
\end{bmatrix}
$$

The three pivots are **$1$, $2$, and $5$**. *(An interesting side note: the product of the pivots equals the determinant of the matrix, which is $10$)*.

---

### 2. How Elimination Fails (Singular Matrices)

Elimination can hit hurdles depending on the structure of the matrix:

* **Temporary Failure (Row Exchange):** If a zero appears in a pivot position, but there are non-zero values beneath it, you can swap rows to keep going.
* **Permanent Failure:** If a zero appears in a pivot position and *all entries below it are also zero*, it is impossible to find a valid pivot. This means the matrix is **singular** (not invertible) and has no unique solution.

---

### 3. Back Substitution

To track the solution, we track what happens to the right-hand side vector $b$ alongside $A$ using an **Augmented Matrix** $[A \mid b]$.

Applying the exact same row multipliers to $b$ transforms it into a new vector $c = \begin{bmatrix} 2 \\ 6 \\ -10 \end{bmatrix}$. The system $Ux = c$ reads:

$$\begin{aligned}
1x + 2y + 1z &= 2 \\
2y - 2z &= 6 \\
5z &= -10
\end{aligned}$$

Using **Back Substitution** (solving from bottom to top):

1. From $5z = -10 \rightarrow \mathbf{z = -2}$.
2. Plug $z$ into row 2: $2y - 2(-2) = 6 \rightarrow 2y + 4 = 6 \rightarrow \mathbf{y = 1}$.
3. Plug $y$ and $z$ into row 1: $1x + 2(1) + 1(-2) = 2 \rightarrow \mathbf{x = 2}$.

---

### 4. Elimination Expressed via Matrix Multiplication

The core mathematical takeaway of the lecture is expressing these systemic row operations as standalone matrices.

#### Linear Combinations of Columns vs. Rows

* **Multiplying on the Right ($Ax$):** A matrix multiplied by a column vector creates a **linear combination of the columns** of the matrix.
* **Multiplying on the Left ($xA$):** A row vector multiplied by a matrix creates a **linear combination of the rows** of the matrix.

#### Elementary (Elimination) Matrices

To execute row operations programmatically, we apply modifications to the **Identity Matrix ($I$)**.

* **To eliminate position $(2,1)$:** We need an elementary matrix $E_{21}$ that subtracts $3 \times (\text{Row 1})$ from $\text{Row 2}$:

$$
E_{21} =
\begin{bmatrix}
1 & 0 & 0 \\
-3 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

* **To eliminate position $(3,2)$:** We create $E_{32}$ to subtract $2 \times (\text{Row 2})$ from $\text{Row 3}$:

$$
E_{32} =
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & -2 & 1
\end{bmatrix}
$$

Putting it all together, the entire sequence of forward elimination is neatly compressed into:

$$E_{32} (E_{21} A) = U$$

---

### 5. Matrix Properties: Order Matters

* **Associative Law Holds:** You can shift parentheses without breaking the math: $E_{32}(E_{21}A) = (E_{32}E_{21})A$. The combined entity $(E_{32}E_{21})$ yields a single matrix that performs all of elimination in one shot.
* **Commutative Law Fails ($AB \neq BA$):** You **cannot** change the order of the matrices. They must remain in their strict chronological execution order.
* **Row vs. Column Operations:** Left-multiplying performs row operations. Right-multiplying performs column operations.

---

### 6. Permutation Matrices ($P$)

If elimination encounters a zero in a pivot zone and requires a row exchange, we use a **Permutation Matrix ($P$)**. A permutation matrix is simply an identity matrix with its rows swapped.

* Multiplying a 2x2 matrix by
  $$
\begin{bmatrix}
0 & 1 \\
1 & 0
\end{bmatrix}
$$ on the left swaps Row 1 and Row 2.

---

### 7. Introduction to Inverses ($E^{-1}$)
The lecture concludes with a preview of how to undo elimination steps using **Inverse Matrices**.

- If $E_{21}$ subtracts $3 \times (\text{Row 1})$ from $\text{Row 2}$, its inverse $E_{21}^{-1}$ must **add** $3 \times (\text{Row 1})$ back to $\text{Row 2}$.

$$
E_{21} =
\begin{bmatrix}
1 & 0 & 0 \\
-3 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
\;\longrightarrow\;
E_{21}^{-1} =
\begin{bmatrix}
1 & 0 & 0 \\
\mathbf{3} & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

Multiplying a matrix by its inverse returns the identity matrix ($E^{-1}E = I$).


Building on the mathematical concepts from Lecture 2, here are the code implementations and structural notes for both **Python** and **C++**.

In professional software development and scientific computing, you rarely write raw elimination loops from scratch. Instead, you rely on highly optimized linear algebra libraries that execute these matrix transformations efficiently behind the scenes.

---

### Python Notes & Implementation (Using `NumPy` & `SciPy`)

While `NumPy` can solve the system directly using `np.linalg.solve`, the exact physical representation of Lecture 2's matrix reduction ($A = LU$) is handled via the `scipy.linalg` library.

* **Key Concept:** Matrix multiplication for elementary matrices uses the `@` operator.
* **LU Decomposition:** To get the exact upper triangular matrix $U$ discussed by Professor Strang, we use `scipy.linalg.lu`. By setting `permute_l=True`, it handles any necessary row exchanges automatically.

```python
import numpy as np
import scipy.linalg as la

# 1. Define Matrix A and Vector b from Lecture 2
A = np.array([[1.0, 2.0, 1.0],
              [3.0, 8.0, 1.0],
              [0.0, 4.0, 1.0]])

b = np.array([2.0, 12.0, 2.0])

# ---- Elementary Matrices (Step-by-Step Elimination) ----
# E21: Subtracts 3 times Row 1 from Row 2
E21 = np.array([[1.0,  0.0, 0.0],
                [-3.0, 1.0, 0.0],
                [0.0,  0.0, 1.0]])

# E32: Subtracts 2 times Row 2 from Row 3
E32 = np.array([[1.0, 0.0,  0.0],
                [0.0, 1.0,  0.0],
                [0.0, -2.0, 1.0]])

# Combined Elimination Matrix E (using associative law: E32 @ E21)
E = E32 @ E21
U_step = E @ A

print("U calculated via step-by-step Elementary Matrices:")
print(U_step)

# ---- Direct Production Solving ----
# In practice, we solve Ax = b directly using optimized algorithms
x = np.linalg.solve(A, b)
print(f"\nSolution Vector x: {x}") # Output: [2. 1. -2.]

```

---

### C++ Notes & Implementation (Using `Eigen`)

In C++, implementing Gaussian elimination manually with nested loops is prone to floating-point errors. The industry standard **Eigen** library wraps these exact execution steps into optimized geometric solvers.

* **Key Concept:** `Eigen::Matrix3d` represents a static $3 \times 3$ matrix of doubles.
* **PartialPivLU:** This built-in solver performs the exact Gaussian elimination with partial pivoting (row exchanges) described in the lecture.
* **Matrix Operations:** Operators like `*` are naturally overloaded to handle both Elementary matrix chaining (`E32 * E21 * A`) and Matrix-Vector computation.

```cpp
#include <iostream>
#include <Eigen/Dense>

int main() {
    // 1. Define Matrix A and Vector b
    Eigen::Matrix3d A;
    A << 1.0, 2.0, 1.0,
         3.0, 8.0, 1.0,
         0.0, 4.0, 1.0;

    Eigen::Vector3d b;
    b << 2.0, 12.0, 2.0;

    // ---- Modeling Elementary Matrices ----
    Eigen::Matrix3d E21;
    E21 << 1.0,  0.0, 0.0,
          -3.0,  1.0, 0.0,
           0.0,  0.0, 1.0;

    Eigen::Matrix3d E32;
    E32 << 1.0,  0.0, 0.0,
           0.0,  1.0, 0.0,
           0.0, -2.0, 1.0;

    // Compute Upper Triangular Matrix U manually via elimination chaining
    Eigen::Matrix3d U = E32 * E21 * A;
    std::cout << "Upper Triangular Matrix U:\n" << U << "\n\n";

    // ---- Solving Ax = b via LU Decomposition ----
    // This executes forward elimination and back substitution under the hood
    Eigen::Vector3d x = A.partialPivLu().solve(b);

    std::cout << "Solution Vector x:\n" << x << std::endl;

    return 0;
}

```

---

### Key Takeaways for Notebook Reference

| Programming Concept | Python (`NumPy` / `SciPy`) | C++ (`Eigen`) |
| --- | --- | --- |
| **Matrix Type** | `np.array` (float64 by default) | `Eigen::Matrix3d` (fixed $3 \times 3$ double) |
| **Matrix Multiplication** | `@` operator (`A @ B`) | `*` operator (`A * B`) |
| **Elimination Engine** | `scipy.linalg.lu(A)` | `A.partialPivLu()` |
| **Back Substitution/Solve** | `np.linalg.solve(A, b)` | `A.colPivHouseholderQr().solve(b)` |

#### Computer Science Note on Efficiency:

While multiplying elementary matrices ($E_{32} \times E_{21} \times A$) is useful for proofs and structural understanding, libraries like `NumPy` and `Eigen` **do not** create these large identity-like matrices explicitly during runtime. They modify the original rows of matrix $A$ directly in computer memory using in-place indexing offsets to conserve RAM and CPU cycles.
