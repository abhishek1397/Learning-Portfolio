# ✅  Matrix Multiplication Code in C++

```cpp
/*
    Matrix Multiplication in C++
    ----------------------------
    Multiplies two matrices entered by the user.
    Input and output are shown in matrix format (row-wise).

    Author: [Your Name]
    GitHub: [Your GitHub Link]
*/

#include <iostream>
using namespace std;

const int MAX = 10;

int main() {
    int a[MAX][MAX], b[MAX][MAX], result[MAX][MAX];
    int r1, c1, r2, c2;

    // --- Input matrix dimensions with validation ---
    do {
        cout << "Enter rows and columns of first matrix: ";
        cin >> r1 >> c1;

        cout << "Enter rows and columns of second matrix: ";
        cin >> r2 >> c2;

        if (c1 != r2)
            cout << " Error: Columns of first matrix must equal rows of second matrix.\n\n";
    } while (c1 != r2);

    // --- Input matrix A ---
    cout << "\nEnter elements of first matrix (" << r1 << "x" << c1 << ") row-wise:\n";
    for (int i = 0; i < r1; ++i) {
        for (int j = 0; j < c1; ++j) {
            cin >> a[i][j];
        }
    }

    // --- Input matrix B ---
    cout << "\nEnter elements of second matrix (" << r2 << "x" << c2 << ") row-wise:\n";
    for (int i = 0; i < r2; ++i) {
        for (int j = 0; j < c2; ++j) {
            cin >> b[i][j];
        }
    }

    // --- Initialize result matrix to 0 ---
    for (int i = 0; i < r1; ++i)
        for (int j = 0; j < c2; ++j)
            result[i][j] = 0;

    // --- Matrix multiplication ---
    for (int i = 0; i < r1; ++i) {
        for (int j = 0; j < c2; ++j) {
            for (int k = 0; k < c1; ++k) {
                result[i][j] += a[i][k] * b[k][j];
            }
        }
    }

    // --- Output result in matrix form ---
    cout << "\n Resultant Matrix (" << r1 << "x" << c2 << "):\n";
    for (int i = 0; i < r1; ++i) {
        for (int j = 0; j < c2; ++j) {
            cout << result[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
```

---

## 🧪 Sample Input/Output (as per your request)

### Input:

```
Enter rows and columns of first matrix: 3 3
Enter rows and columns of second matrix: 3 3

Enter elements of first matrix (3x3) row-wise:
1 2 3
4 5 6
7 8 9

Enter elements of second matrix (3x3) row-wise:
9 8 7
6 5 4
3 2 1
```

### Output:

```
✅ Resultant Matrix (3x3):
30 24 18
84 69 54
138 114 90
```

---

# 🔍 Step-by-Step Explanation


### 🔹 `#include <iostream>`

* This includes the **iostream** library, which allows us to use `cin` (for input) and `cout` (for output).

---

### 🔹 `using namespace std;`

* So we don't have to write `std::cin` and `std::cout` every time.
* This brings all standard library names into global scope.

---

### 🔹 `const int MAX = 10;`

* Defines a constant `MAX` which sets the **maximum size** of matrices.
* Each matrix can be at most 10x10.

---

### 🔹 `int a[MAX][MAX], b[MAX][MAX], result[MAX][MAX];`

* Declares **three 2D arrays**:

  * `a[][]` → first matrix
  * `b[][]` → second matrix
  * `result[][]` → to store the product of the two matrices

---

### 🔹 `int r1, c1, r2, c2;`

* Variables to store:

  * `r1` → number of rows in matrix A
  * `c1` → number of columns in matrix A
  * `r2` → number of rows in matrix B
  * `c2` → number of columns in matrix B

---

### 🔹 Input Matrix Dimensions (Validation)

```cpp
do {
    cout << "Enter rows and columns of first matrix: ";
    cin >> r1 >> c1;

    cout << "Enter rows and columns of second matrix: ";
    cin >> r2 >> c2;

    if (c1 != r2)
        cout << "❌ Error: Columns of first matrix must equal rows of second matrix.\n\n";
} while (c1 != r2);
```

* The user is asked to input matrix dimensions.
* Matrix multiplication is only possible if:

  ```
  columns of A == rows of B
  ```
* If this condition fails, an error is shown and input is repeated using a `do-while` loop.

---

### 🔹 Input Matrix A

```cpp
cout << "\nEnter elements of first matrix (" << r1 << "x" << c1 << ") row-wise:\n";
for (int i = 0; i < r1; ++i)
    for (int j = 0; j < c1; ++j)
        cin >> a[i][j];
```

* This loop asks the user to enter matrix A row by row.
* For example, if `r1 = 2` and `c1 = 3`, it expects 6 numbers:

  ```
  1 2 3
  4 5 6
  ```

---

### 🔹 Input Matrix B

```cpp
cout << "\nEnter elements of second matrix (" << r2 << "x" << c2 << ") row-wise:\n";
for (int i = 0; i < r2; ++i)
    for (int j = 0; j < c2; ++j)
        cin >> b[i][j];
```

* Same as above, but for matrix B.
* Ensures both matrices are filled before multiplying.

---

### 🔹 Initialize Result Matrix

```cpp
for (int i = 0; i < r1; ++i)
    for (int j = 0; j < c2; ++j)
        result[i][j] = 0;
```

* Before performing multiplication, we must **initialize** every value in `result` to 0.
* Otherwise, it might contain garbage values from memory.

---

### 🔹 Matrix Multiplication Logic

```cpp
for (int i = 0; i < r1; ++i)
    for (int j = 0; j < c2; ++j)
        for (int k = 0; k < c1; ++k)
            result[i][j] += a[i][k] * b[k][j];
```

This is the **core logic** of matrix multiplication.

**What’s happening here:**

* Outer loop (`i`) → iterates over each row of matrix A
* Middle loop (`j`) → iterates over each column of matrix B
* Inner loop (`k`) → performs the **dot product** of:

  * Row `i` from matrix A
  * Column `j` from matrix B

📌 Formula:

```
result[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j] + ... + a[i][c1-1] * b[c1-1][j]
```

---

### 🔹 Display Result in Matrix Form

```cpp
cout << "\n✅ Resultant Matrix (" << r1 << "x" << c2 << "):\n";
for (int i = 0; i < r1; ++i) {
    for (int j = 0; j < c2; ++j)
        cout << result[i][j] << " ";
    cout << endl;
}
```

* Neatly prints the result in matrix form.
* Each row is printed on its own line.
* Values are separated by spaces, like:

```
58 64
139 154
```

---

### 🔹 `return 0;`

* Indicates the program executed successfully and ends the `main()` function.

---

## ✅ Summary of Matrix Multiplication Flow:

1. **Input dimensions** and validate compatibility.
2. **Input matrix A** (row-wise).
3. **Input matrix B** (row-wise).
4. **Initialize result matrix** to zero.
5. **Perform multiplication** using three nested loops.
6. **Display result** in clean matrix format.

---

## ✅ Sample Output

```
Enter rows and columns of first matrix: 2 3
Enter rows and columns of second matrix: 3 2

Enter elements of first matrix (2x3) row-wise:
1 2 3
4 5 6

Enter elements of second matrix (3x2) row-wise:
7 8
9 10
11 12

✅ Resultant Matrix (2x2):
58 64
139 154
```

