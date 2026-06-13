# MIT 18.06 Linear Algebra — Lecture 4: Factorization into A = LU

**Professor:** Gilbert Strang
**Topic:** LU Factorization

---

# 1. Core Philosophy of the Lecture

The main goal of this lecture is to reinterpret Gaussian elimination as a matrix factorization problem.

Instead of viewing elimination as a sequence of row operations, we represent the process as the decomposition of a matrix into two simpler matrices:

* L = Lower Triangular Matrix
* U = Upper Triangular Matrix

The central idea is:

A = LU

## Why is this important?

Suppose we need to solve:

Ax = b

many times with different vectors b.

Rather than performing elimination repeatedly:

1. Factor A once into L and U.
2. Solve Ly = b.
3. Solve Ux = y.

This is computationally much more efficient and is widely used in scientific computing, engineering simulations, and numerical linear algebra.

---

# 2. Deriving A = LU (2×2 Example)

Consider:

A =

| 2 | 1 |
| - | - |
| 8 | 7 |

## Step 1: Elimination

To eliminate the entry 8 below the first pivot:

Multiplier:

m21 = 8 / 2 = 4

Subtract:

Row2 ← Row2 − 4 × Row1

The elimination matrix is:

E21 =

| 1  | 0 |
| -- | - |
| -4 | 1 |

Applying elimination:

E21A = U

U =

| 2 | 1 |
| - | - |
| 0 | 3 |

---

## Step 2: Recover A

Since:

E21A = U

Multiply both sides by E21^(-1):

A = E21^(-1)U

The inverse simply reverses the elimination:

L = E21^(-1)

=

| 1 | 0 |
| - | - |
| 4 | 1 |

Therefore:

A = LU

=

| 1 | 0 |
| - | - |
| 4 | 1 |

×

| 2 | 1 |
| - | - |
| 0 | 3 |

---

# 3. Three-Factor Form: A = LDU

Sometimes it is useful to separate the pivots from U.

## Diagonal Matrix D

Collect all pivot values into a diagonal matrix:

D =

| 2 | 0 |
| - | - |
| 0 | 3 |

---

## Normalized Upper Triangular Matrix

Divide each row of U by its pivot.

Result:

U_normalized =

| 1 | 0.5 |
| - | --- |
| 0 | 1   |

Now:

A = LDU

where:

* L contains elimination multipliers.
* D contains pivots.
* U has ones on the diagonal.

This form is often useful for theoretical analysis.

---

# 4. The Structure of L in Larger Systems

For a 3×3 matrix, elimination requires multiple steps:

* E21
* E31
* E32

The upper-triangular matrix U is obtained by:

U = E32 E31 E21 A

---

## Why E Becomes Complicated

If we combine all elimination matrices:

E = E32 E31 E21

the multipliers interact with one another.

The resulting entries no longer directly reveal the original elimination multipliers.

---

## Why L is Beautiful

Consider the inverse product:

L = E21^(-1) E31^(-1) E32^(-1)

A remarkable fact emerges:

**The elimination multipliers appear directly inside L.**

If:

* Row2 ← Row2 − 3 × Row1

then:

L(2,1) = 3

If:

* Row3 ← Row3 + 2 × Row2

then:

L(3,2) = -2

The structure becomes:

L =

| 1   | 0   | 0 |
| --- | --- | - |
| m21 | 1   | 0 |
| m31 | m32 | 1 |

where:

* m21 = multiplier used on row 2
* m31 = multiplier used on row 3
* m32 = multiplier used on row 3 during the second elimination stage

---

# 5. Computational Cost of Elimination

For an n × n matrix:

## Computing U

Transforming:

A → U

requires approximately:

(1/3)n^3

multiplication and subtraction operations.

This dominates the computational cost.

---

## Updating b

Transforming:

b → modified b

requires approximately:

n^2

operations.

Compared with n^3, this cost is relatively small for large matrices.

---

# 6. Row Exchanges and Permutation Matrices

The factorization:

A = LU

works only when every pivot is nonzero.

---

## What Happens if a Pivot is Zero?

Example:

| 0 | 1 |
| - | - |
| 2 | 3 |

The first pivot is zero.

Elimination cannot proceed unless rows are exchanged.

---

## Permutation Matrix P

A permutation matrix is obtained by rearranging rows of the identity matrix.

Example:

P =

| 0 | 1 |
| - | - |
| 1 | 0 |

Multiplying by P swaps rows.

---

## General Factorization

When row exchanges are required:

PA = LU

This is the standard factorization used in practical numerical algorithms.

---

# Key Takeaways

1. Gaussian elimination can be expressed as matrix factorization.

   A = LU

2. L stores elimination multipliers.

3. U stores the resulting upper-triangular system.

4. Factoring A once allows efficient solution of many systems Ax = b.

5. A refined factorization is:

   A = LDU

   where D contains the pivots.

6. Without row exchanges, multipliers appear directly inside L.

7. For large matrices, elimination costs roughly:

   (1/3)n^3 operations.

8. If row swaps are needed, use:

   PA = LU

9. LU factorization is one of the foundational algorithms of numerical linear algebra and scientific computing.

---

If you're thinking like a quant developer, the goal is not merely "making LU work." The goal is:

* Numerical stability
* Cache efficiency
* Reusability
* Separation of factorization and solve phases
* Ability to solve many `Ax = b` problems after one factorization
* Support for partial pivoting (`PA = LU`)

A production-quality implementation stores **L and U in the same matrix**, exactly as LAPACK and many trading/risk systems do.

---

# Python (Quant Style)

```python
import numpy as np

class LUFactorization:
    def __init__(self, A):
        self.n = A.shape[0]
        self.LU = A.astype(np.float64).copy()
        self.pivots = np.arange(self.n)

        self._factorize()

    def _factorize(self):
        n = self.n
        LU = self.LU

        for k in range(n):

            pivot_row = np.argmax(np.abs(LU[k:, k])) + k

            if abs(LU[pivot_row, k]) < 1e-12:
                raise ValueError("Matrix is singular")

            if pivot_row != k:
                LU[[k, pivot_row]] = LU[[pivot_row, k]]
                self.pivots[[k, pivot_row]] = \
                    self.pivots[[pivot_row, k]]

            for i in range(k + 1, n):

                LU[i, k] /= LU[k, k]

                LU[i, k + 1:] -= \
                    LU[i, k] * LU[k, k + 1:]

    def solve(self, b):

        b = np.asarray(b, dtype=np.float64)
        x = b[self.pivots].copy()

        n = self.n

        # Forward substitution

        for i in range(n):
            x[i + 1:] -= self.LU[i + 1:, i] * x[i]

        # Backward substitution

        for i in range(n - 1, -1, -1):
            x[i] -= np.dot(
                self.LU[i, i + 1:],
                x[i + 1:]
            )
            x[i] /= self.LU[i, i]

        return x

    def L(self):
        return np.tril(self.LU, -1) + np.eye(self.n)

    def U(self):
        return np.triu(self.LU)
```

---

## Usage

```python
A = np.array([
    [2, 1, 1],
    [4, -6, 0],
    [-2, 7, 2]
])

b = np.array([5, -2, 9])

lu = LUFactorization(A)

x = lu.solve(b)

print("L")
print(lu.L())

print("\nU")
print(lu.U())

print("\nSolution")
print(x)
```

---

# C++ (Quant Style)

This resembles what you'd write in pricing engines, risk systems, or low-latency infrastructure.

```cpp
#include <vector>
#include <cmath>
#include <stdexcept>
#include <algorithm>

class LUFactorization
{
private:

    std::vector<std::vector<double>> lu_;
    std::vector<int> pivot_;
    int n_;

public:

    explicit LUFactorization(
        const std::vector<std::vector<double>>& A)
    {
        n_ = A.size();

        lu_ = A;

        pivot_.resize(n_);

        for(int i = 0; i < n_; ++i)
            pivot_[i] = i;

        factorize();
    }

private:

    void factorize()
    {
        for(int k = 0; k < n_; ++k)
        {
            int pivotRow = k;
            double maxVal = std::abs(lu_[k][k]);

            for(int i = k + 1; i < n_; ++i)
            {
                if(std::abs(lu_[i][k]) > maxVal)
                {
                    maxVal = std::abs(lu_[i][k]);
                    pivotRow = i;
                }
            }

            if(maxVal < 1e-12)
            {
                throw std::runtime_error(
                    "Singular matrix");
            }

            if(pivotRow != k)
            {
                std::swap(
                    lu_[k],
                    lu_[pivotRow]
                );

                std::swap(
                    pivot_[k],
                    pivot_[pivotRow]
                );
            }

            for(int i = k + 1; i < n_; ++i)
            {
                lu_[i][k] /= lu_[k][k];

                for(int j = k + 1; j < n_; ++j)
                {
                    lu_[i][j] -=
                        lu_[i][k] * lu_[k][j];
                }
            }
        }
    }

public:

    std::vector<double>
    solve(const std::vector<double>& b) const
    {
        std::vector<double> x(n_);

        for(int i = 0; i < n_; ++i)
        {
            x[i] = b[pivot_[i]];
        }

        // Forward substitution

        for(int i = 0; i < n_; ++i)
        {
            for(int j = 0; j < i; ++j)
            {
                x[i] -= lu_[i][j] * x[j];
            }
        }

        // Backward substitution

        for(int i = n_ - 1; i >= 0; --i)
        {
            for(int j = i + 1; j < n_; ++j)
            {
                x[i] -= lu_[i][j] * x[j];
            }

            x[i] /= lu_[i][i];
        }

        return x;
    }
};
```

---

## Why a Quant Would Write It This Way

### Academic Version

Store:

```
L
U
```

as separate matrices.

Memory:

```
O(2n²)
```

---

### Quant Version

Store both inside one matrix:

```
| U U U |
| L U U |
| L L U |
```

Example:

```
[ 2   1   1 ]
[ 2  -8  -2 ]
[-1  -1   1 ]
```

Lower triangle stores multipliers.

Upper triangle stores pivots and upper matrix.

Memory:

```
O(n²)
```

instead of

```
O(2n²)
```

which matters for large risk systems.

---

### Connection to Lecture 4

Lecture 4's core insight is:

```
Elimination multipliers
        ↓
        L

Remaining matrix
        ↓
        U
```

A quant implementation simply stores both objects in the same memory block and records row swaps through a pivot vector:

```
PA = LU
```

This is essentially the idea behind classic numerical libraries such as LAPACK and much of the dense linear algebra infrastructure used in pricing, portfolio optimization, and risk engines.
