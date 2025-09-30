
# ✅ Matrix Addition Code in C++

```cpp
#include <iostream>
using namespace std;

const int MAX = 10;

int main() {
    int a[MAX][MAX], b[MAX][MAX], sum[MAX][MAX];
    int r1, c1, r2, c2;

    // --- Input matrix dimensions with validation ---
    do {
        cout << "Enter rows and columns of first matrix: ";
        cin >> r1 >> c1;

        cout << "Enter rows and columns of second matrix: ";
        cin >> r2 >> c2;

        if (r1 != r2 || c1 != c2)
            cout << " Error: Both matrices must have the same dimensions.\n\n";
    } while (r1 != r2 || c1 != c2);

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

    // --- Initialize sum matrix to 0 ---
    for (int i = 0; i < r1; ++i)
        for (int j = 0; j < c1; ++j)
            sum[i][j] = 0;

    // --- Matrix addition ---
    for (int i = 0; i < r1; ++i) {
        for (int j = 0; j < c1; ++j) {
            sum[i][j] = a[i][j] + b[i][j];
        }
    }

    // --- Output result in matrix form ---
    cout << "\n Resultant Matrix (" << r1 << "x" << c1 << "):\n";
    for (int i = 0; i < r1; ++i) {
        for (int j = 0; j < c1; ++j) {
            cout << sum[i][j] << " ";
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
Enter rows and columns of first matrix: 2 3
Enter rows and columns of second matrix: 2 3

Enter elements of first matrix (2x3) row-wise:
1 2 3
4 5 6

Enter elements of second matrix (2x3) row-wise:
7 8 9
10 11 12
```

### Output:

```
✅ Resultant Matrix (2x3):
8 10 12
14 16 18
```

---

## 🔍 Step-by-Step Explanation

### 🔹 `#include <iostream>`

* Includes the **iostream** library to enable input and output operations.
* `cin` is used for input and `cout` for output.

---

### 🔹 `using namespace std;`

* This avoids the need to write `std::cin` and `std::cout` repeatedly.
* It brings all standard library names into global scope.

---

### 🔹 `const int MAX = 10;`

* Defines a constant `MAX` to set the **maximum size** of matrices.
* Each matrix can be at most 10x10.

---

### 🔹 `int a[MAX][MAX], b[MAX][MAX], sum[MAX][MAX];`

* Declares **three 2D arrays**:

  * `a[][]` → the first matrix
  * `b[][]` → the second matrix
  * `sum[][]` → the matrix that will store the result of the addition

---

### 🔹 `int r1, c1, r2, c2;`

* Variables to store the dimensions of the matrices:

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

    if (r1 != r2 || c1 != c2)
        cout << " Error: Both matrices must have the same dimensions.\n\n";
} while (r1 != r2 || c1 != c2);
```

* The user is asked to input the dimensions of both matrices.
* Matrix addition is only possible if the matrices have **exactly the same dimensions** (same number of rows and columns).
* If this condition fails, an error message is shown and input is repeated using a `do-while` loop.

---

### 🔹 Input Matrix A

```cpp
cout << "\nEnter elements of first matrix (" << r1 << "x" << c1 << ") row-wise:\n";
for (int i = 0; i < r1; ++i) {
    for (int j = 0; j < c1; ++j) {
        cin >> a[i][j];
    }
}
```

* This loop prompts the user to enter matrix A row by row.
* For example, if `r1 = 2` and `c1 = 3`, it expects 6 numbers:

  ```
  1 2 3
  4 5 6
  ```

---

### 🔹 Input Matrix B

```cpp
cout << "\nEnter elements of second matrix (" << r2 << "x" << c2 << ") row-wise:\n";
for (int i = 0; i < r2; ++i) {
    for (int j = 0; j < c2; ++j) {
        cin >> b[i][j];
    }
}
```

* Same as above, but for matrix B.
* Ensures both matrices are filled before adding them.

---

### 🔹 Initialize Sum Matrix

```cpp
for (int i = 0; i < r1; ++i)
    for (int j = 0; j < c1; ++j)
        sum[i][j] = 0;
```

* Before performing the addition, **initialize** every element of `sum[][]` to 0.
* This ensures there are no leftover values from previous runs or memory garbage.

---

### 🔹 Matrix Addition Logic

```cpp
for (int i = 0; i < r1; ++i) {
    for (int j = 0; j < c1; ++j) {
        sum[i][j] = a[i][j] + b[i][j];
    }
}
```

* This is the **core logic** for matrix addition.
* The values in `sum[i][j]` are calculated by adding the corresponding values from `a[i][j]` and `b[i][j]`.

  * Formula: `sum[i][j] = a[i][j] + b[i][j]`.

---

### 🔹 Display Result in Matrix Form

```cpp
cout << "\n✅ Resultant Matrix (" << r1 << "x" << c1 << "):\n";
for (int i = 0; i < r1; ++i) {
    for (int j = 0; j < c1; ++j) {
        cout << sum[i][j] << " ";
    }
    cout << endl;
}
```

* Neatly prints the result in matrix form.
* Each row is printed on its own line, with values separated by spaces.

---

### 🔹 `return 0;`

* Indicates that the program ran successfully and ends the `main()` function.

---

## ✅ Summary of Matrix Addition Flow:

1. **Input dimensions** and validate they match for both matrices.
2. **Input matrix A** (row-wise).
3. **Input matrix B** (row-wise).
4. **Initialize result matrix** to zero.
5. **Perform addition** element-wise.
6. **Display result** in a clean matrix format.

---

## ✅ Sample Output

```
Enter rows and columns of first matrix: 2 3
Enter rows and columns of second matrix: 2 3

Enter elements of first matrix (2x3) row-wise:
1 2 3
4 5 6

Enter elements of second matrix (2x3) row-wise:
7 8 9
10 11 12

✅ Resultant Matrix (2x3):
8 10 12
14 16 18
```
