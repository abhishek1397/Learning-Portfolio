# 🚀 Radix Sort in C++

This repository demonstrates **Radix Sort** implemented in **C++** with both **LSD (Least Significant Digit)** and **MSD (Most Significant Digit)** approaches.
We include versions using **vectors**, **raw arrays**, and also extend Radix Sort to **floating-point numbers**.

---

## 📌 What is Radix Sort?

Radix Sort is a **non-comparative sorting algorithm**. It processes the numbers digit by digit:

* **LSD**: Starts from the least significant digit (rightmost).
* **MSD**: Starts from the most significant digit (leftmost).

It uses a **stable subroutine** (usually Counting Sort or Bucketing) to sort numbers digit by digit.

---

# 🔹 1. LSD Radix Sort (Integers)

### ✅ With Vectors

```cpp
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int getMax(vector<int>& arr) {
    int mx = arr[0];
    for (int x : arr) if (x > mx) mx = x;
    return mx;
}

void countingSort(vector<int>& arr, int exp) {
    int n = arr.size();
    vector<int> output(n);
    int count[10] = {0};

    for (int i = 0; i < n; i++)
        count[(arr[i] / exp) % 10]++;

    for (int i = 1; i < 10; i++)
        count[i] += count[i - 1];

    for (int i = n - 1; i >= 0; i--) {
        output[count[(arr[i] / exp) % 10] - 1] = arr[i];
        count[(arr[i] / exp) % 10]--;
    }
    arr = output;
}

void radixSort(vector<int>& arr) {
    int m = getMax(arr);
    for (int exp = 1; m / exp > 0; exp *= 10)
        countingSort(arr, exp);
}

int main() {
    vector<int> arr = {170, 45, 75, 90, 802, 24, 2, 66};
    radixSort(arr);

    cout << "Sorted array (LSD, Vector): ";
    for (int x : arr) cout << x << " ";
    cout << endl;
}
```

---

### ✅ With Raw Arrays

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int getMax(int arr[], int n) {
    int mx = arr[0];
    for (int i = 1; i < n; i++)
        if (arr[i] > mx) mx = arr[i];
    return mx;
}

void countingSort(int arr[], int n, int exp) {
    int output[n];
    int count[10] = {0};

    for (int i = 0; i < n; i++)
        count[(arr[i] / exp) % 10]++;

    for (int i = 1; i < 10; i++)
        count[i] += count[i - 1];

    for (int i = n - 1; i >= 0; i--) {
        output[count[(arr[i] / exp) % 10] - 1] = arr[i];
        count[(arr[i] / exp) % 10]--;
    }
    for (int i = 0; i < n; i++)
        arr[i] = output[i];
}

void radixSort(int arr[], int n) {
    int m = getMax(arr, n);
    for (int exp = 1; m / exp > 0; exp *= 10)
        countingSort(arr, n, exp);
}

int main() {
    int arr[] = {170, 45, 75, 90, 802, 24, 2, 66};
    int n = sizeof(arr) / sizeof(arr[0]);
    radixSort(arr, n);

    cout << "Sorted array (LSD, Raw Array): ";
    for (int i = 0; i < n; i++) cout << arr[i] << " ";
    cout << endl;
}
```

---

# 🔹 2. MSD Radix Sort (Integers)

MSD works recursively, starting from the **most significant digit**.

### ✅ MSD with Vectors

```cpp
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

void MSDRadixSort(vector<int>& arr, int exp) {
    if (arr.size() <= 1 || exp == 0) return;

    vector<vector<int>> buckets(10);

    for (int x : arr)
        buckets[(x / exp) % 10].push_back(x);

    arr.clear();
    for (int i = 0; i < 10; i++) {
        MSDRadixSort(buckets[i], exp / 10);
        arr.insert(arr.end(), buckets[i].begin(), buckets[i].end());
    }
}

void radixSortMSD(vector<int>& arr) {
    int mx = *max_element(arr.begin(), arr.end());
    int exp = pow(10, (int)log10(mx));
    MSDRadixSort(arr, exp);
}

int main() {
    vector<int> arr = {170, 45, 75, 90, 802, 24, 2, 66};
    radixSortMSD(arr);

    cout << "Sorted array (MSD, Vector): ";
    for (int x : arr) cout << x << " ";
    cout << endl;
}
```

---

# 🔹 3. LSD Radix Sort (Floating Point)

For floating numbers:

* Scale all numbers by `10^decimalPlaces`
* Apply integer radix sort
* Scale back

```cpp
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

void countingSort(vector<int>& arr, int exp) {
    int n = arr.size();
    vector<int> output(n);
    int count[10] = {0};

    for (int i = 0; i < n; i++)
        count[(arr[i] / exp) % 10]++;

    for (int i = 1; i < 10; i++)
        count[i] += count[i - 1];

    for (int i = n - 1; i >= 0; i--) {
        output[count[(arr[i] / exp) % 10] - 1] = arr[i];
        count[(arr[i] / exp) % 10]--;
    }
    arr = output;
}

void radixSort(vector<int>& arr) {
    int m = *max_element(arr.begin(), arr.end());
    for (int exp = 1; m / exp > 0; exp *= 10)
        countingSort(arr, exp);
}

int main() {
    vector<double> floats = {3.14, 1.618, 2.71, 0.577, 10.01};
    int scale = 1000; // keep 3 decimals

    vector<int> scaled;
    for (double x : floats) scaled.push_back((int)(x * scale));

    radixSort(scaled);

    cout << "Sorted floats (LSD): ";
    for (int x : scaled) cout << (double)x / scale << " ";
    cout << endl;
}
```

---

# 🔹 4. MSD Radix Sort (Floating Point)

```cpp
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

void MSDRadixSort(vector<int>& arr, int exp) {
    if (arr.size() <= 1 || exp == 0) return;

    vector<vector<int>> buckets(10);
    for (int x : arr)
        buckets[(x / exp) % 10].push_back(x);

    arr.clear();
    for (int i = 0; i < 10; i++) {
        MSDRadixSort(buckets[i], exp / 10);
        arr.insert(arr.end(), buckets[i].begin(), buckets[i].end());
    }
}

void radixSortMSD(vector<int>& arr) {
    int mx = *max_element(arr.begin(), arr.end());
    int exp = pow(10, (int)log10(mx));
    MSDRadixSort(arr, exp);
}

int main() {
    vector<double> floats = {3.14, 1.618, 2.71, 0.577, 10.01};
    int scale = 1000; // keep 3 decimals

    vector<int> scaled;
    for (double x : floats) scaled.push_back((int)(x * scale));

    radixSortMSD(scaled);

    cout << "Sorted floats (MSD): ";
    for (int x : scaled) cout << (double)x / scale << " ";
    cout << endl;
}
```

---

# 📊 Summary

* **LSD**: Easier, iterative, stable, commonly used.
* **MSD**: Recursive, useful when data has varying digit lengths.
* **Floats**: Scale → Sort → Scale back.

