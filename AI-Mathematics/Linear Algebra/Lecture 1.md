# **Lecture 1: The Geometry of Linear Equations** from MIT's 18.06 Linear Algebra course, taught by Professor Gilbert Strang

### 1. The Fundamental Problem

The lecture starts with a basic system of $n$ linear equations with $n$ unknowns. To illustrate, Professor Strang uses a $2 \times 2$ system ($2$ equations, $2$ unknowns):

$$\begin{aligned}
2x - y &= 0 \\
-x + 2y &= 3
\end{aligned}$$

---

### 2. The Row Picture

The Row Picture is the standard geometric interpretation taught in introductory algebra.

* **Concept:** You look at each equation in the system individually. In a 2D space, each equation represents a straight line.
* **Interpretation:** The solution to the system is the specific point where all the lines intersect.
* **Applying to the Example:**
* Equation 1 ($2x - y = 0$): A line passing through the origin $(0,0)$ with a slope of 2.
* Equation 2 ($-x + 2y = 3$): A line passing through the y-intercept $(0, 1.5)$ and x-intercept $(-3, 0)$.
* **Intersection:** Plotting both lines shows they cross exactly at the point **$(x=1, y=2)$**.



---

### 3. The Column Picture (The Crucial Shift)

Professor Strang emphasizes that the **Column Picture** is far more important for understanding Linear Algebra and scaling up to larger systems.

* **Concept:** Instead of looking at rows, you break the system apart into vertical column vectors.
* **Interpretation:** The system asks: *"Can we find a **linear combination** of the column vectors that equals the target vector $b$?"*
* **Applying to the Example:**
We rewrite the equations by pulling out the variables $x$ and $y$:

$$x \begin{bmatrix} 2 \\ -1 \end{bmatrix} + y \begin{bmatrix} -1 \\ 2 \end{bmatrix} = \begin{bmatrix} 0 \\ 3 \end{bmatrix}$$

* **Geometric Construction:**
* Vector 1 ($\text{col}_1$) goes over 2, down 1.
* Vector 2 ($\text{col}_2$) goes left 1, up 2.
* We need to scale $\text{col}_1$ by $x$ and $\text{col}_2$ by $y$ so that their tip-to-tail addition lands exactly on the vector $\begin{bmatrix} 0 \\ 3 \end{bmatrix}$ (which sits on the y-axis).
* If we take **$1$ of the first column** and **$2$ of the second column**:



$$1 \begin{bmatrix} 2 \\ -1 \end{bmatrix} + 2 \begin{bmatrix} -1 \\ 2 \end{bmatrix} = \begin{bmatrix} 2 - 2 \\ -1 + 4 \end{bmatrix} = \begin{bmatrix} 0 \\ 3 \end{bmatrix}$$

This perfectly confirms the solution $(x=1, y=2)$.

---

### 4. Scaling up to 3 Dimensions ($3 \times 3$ System)

The differences between the two pictures become stark when adding a third variable ($z$) and a third equation.

#### The 3D Row Picture:

* Each equation now represents a **flat plane** in 3D space.
* Two equations intersect to form a *line* (where two planes meet like the spine of an open book).
* The third equation (a third plane) cuts through that line at a **single point**.
* Visualizing three intersecting planes in your head is incredibly difficult, making the row picture highly impractical for dimensions higher than 3.

#### The 3D Column Picture:

* You are given three distinct column vectors in 3D space ($\mathbf{v_1}, \mathbf{v_2}, \mathbf{v_3}$).
* The problem remains straightforward: Find the scalar multipliers $(x, y, z)$ such that:

$$x\mathbf{v_1} + y\mathbf{v_2} + z\mathbf{v_3} = \mathbf{b}$$

* You are simply traveling along three directional vectors in space to reach a destination vector $\mathbf{b}$.

---

### 5. Matrix Form: $Ax = b$

The system can be neatly packaged into a single matrix equation.

$$\begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 3 \end{bmatrix}$$

Where:

* $A$ is the **Coefficient Matrix**.
* $x$ is the **Vector of Unknowns**.
* $b$ is the **Right-Hand Side Vector**.

#### Professor Strang's Definition of Matrix Multiplication ($Ax$):

The lecture highlights two ways to compute the product of a matrix $A$ and a vector $x$:

1. **By Rows (Dot Product):** The standard high school method. To get the first component of $Ax$, you multiply the first row of $A$ by the vector $x$: $(2 \cdot x) + (-1 \cdot y)$.
2. **By Columns (Linear Combination):** The preferred structural viewpoint. **$Ax$ is explicitly a linear combination of the columns of $A$.** The components of $x$ act as the weights/coefficients for those columns.

---

### 6. Key Theoretical Question: "Can we always solve $Ax = b$?"

Does a solution exist for *every* possible vector $b$?

* **The Geometric Answer:** Yes, if the linear combinations of the columns of $A$ can fill the entire space ($\mathbb{R}^n$).
* **When does it fail? (Singular Matrix Case):**
* If the column vectors lie in the same line (2D) or the same flat plane (3D), they are **dependent**.
* If the columns are trapped in a single 2D plane inside a 3D space, you can only solve $Ax = b$ if the target vector $b$ happens to lie perfectly within that flat plane. If $b$ points out of that plane, the system is impossible to solve.
* In this scenario, the matrix $A$ is called **singular** or **not invertible**.



In this lecture, Professor Strang explores systems of linear equations through two critical perspectives: **the Row Picture** and **the Column Picture**, showing how equations transition into the matrix form $Ax = b$.

Implementing these mathematical operations and visualizing them can be done using **Python** (via `NumPy`) and **C++** (via `Eigen`). Below are the notes and implementation codes for both languages.

---

### Python Notes & Implementation (Using `NumPy`)

Python is widely recognized for data science and machine learning because libraries like `NumPy` handle vector and matrix operations efficiently under the hood via optimized C/Fortran libraries.

* **Key Concept:** Arrays (`np.array`) represent both vectors (1D arrays) and matrices (2D arrays).
* **Matrix Multiplication:** The `@` operator or `np.dot()` is used for matrix-vector multiplication ($Ax$).
* **Solving $Ax = b$:** `np.linalg.solve(A, b)` uses LAPACK routines (similar to Gaussian elimination) to compute the exact solution vector $x$ directly.

#### Code Example:

```python
import numpy as np

# 1. Define Matrix A and Vector b from the lecture example
# 2x -  y = 0
# -x + 2y = 3
A = np.array([[2, -1], 
              [-1, 2]])
b = np.array()

# ---- The Column Picture View ----
# Linear combination of columns: x * col1 + y * col2 = b
col1 = A[:, 0]
col2 = A[:, 1]

# If we know the solution is x=1, y=2:
x_sol, y_sol = 1, 2
combination = x_sol * col1 + y_sol * col2
print("Linear Combination Result:", combination)  # Output should match b:

# ---- Solving the System Matrix Form (Ax = b) ----
try:
    x = np.linalg.solve(A, b)
    print(True)
    print(f"Solution to Ax = b: x = {x}, y = {x}")
except np.linalg.LinAlgError:
    print("The system does not have a unique solution.")

```

---

### C++ Notes & Implementation (Using `Eigen`)

In C++, basic multi-dimensional arrays or standard vectors (`std::vector`) lack natively optimized linear algebra methods. Production code relies on **Eigen**, a high-performance, header-only C++ template library for linear algebra.

* **Key Concept:** Matrices and vectors are explicitly typed (`Eigen::Matrix2d` for a $2\times2$ double matrix, `Eigen::Vector2d` for a 2-element column vector).
* **Matrix Multiplication:** The standard multiplication operator `*` is overloaded to perform proper algebraic matrix/vector multiplication.
* **Solving $Ax = b$:** Solvers utilize decomposition methods. For a standard square, invertible matrix, `.colPivHouseholderQr().solve()` is highly reliable and fast.

#### Code Example:

```cpp
#include <iostream>
#include <Eigen/Dense> // Requires the Eigen library template headers

int main() {
    // 1. Define Matrix A and Vector b
    // 2x -  y = 0
    // -x + 2y = 3
    Eigen::Matrix2d A;
    A << 2, -1,
         -1, 2;
         
    Eigen::Vector2d b;
    b << 0, 
         3;

    // ---- The Column Picture View ----
    // Extracting columns
    Eigen::Vector2d col1 = A.col(0);
    Eigen::Vector2d col2 = A.col(1);
    
    // Testing the linear combination with the solution (1, 2)
    double x_sol = 1.0;
    double y_sol = 2.0;
    Eigen::Vector2d combination = x_sol * col1 + y_sol * col2;
    std::cout << "Linear Combination Result:\n" << combination << "\n\n";

    // ---- Solving the System Matrix Form (Ax = b) ----
    // We use a QR Decomposition solver to find vector x
    Eigen::Vector2d x = A.colPivHouseholderQr().solve(b);
    
    std::cout << "Solution to Ax = b:\n";
    std::cout << "x = " << x(0) << "\n";
    std::cout << "y = " << x(1) << "\n";

    return 0;
}

```

### Quick Comparison for Notebook Reference

| Operation | Python (`NumPy`) | C++ (`Eigen`) |
| --- | --- | --- |
| **Matrix Initialization** | `np.array([[2, -1], [-1, 2]])` | `Matrix2d A; A << 2, -1, -1, 2;` |
| **Column Slicing** | `A[:, 0]` | `A.col(0)` |
| **Matrix Multiply ($Ax$)** | `A @ x` | `A * x` |
| **Solve $Ax=b$** | `np.linalg.solve(A, b)` | `A.colPivHouseholderQr().solve(b)` |
