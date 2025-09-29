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
            cout << "❌ Error: Columns of first matrix must equal rows of second matrix.\n\n";
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
    cout << "\n✅ Resultant Matrix (" << r1 << "x" << c2 << "):\n";
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

