# 📌 Definition: Pointer to an Array

In C++, the notation:

```cpp
int (*ptr)[N];
```

means:

* `ptr` is a **pointer to an array** of `N` integers.
* It points to **the entire block** of the array, not just a single element.

💡 **Breakdown**:

* `*ptr` → dereferences to the array
* `(*ptr)[i]` → accesses the `i`-th element inside the array

---

## 🧠 Difference: `int (*ptr)[N]` vs `int* ptr`

| Feature                | `int* ptr`                                      | `int (*ptr)[N]`                         |
| ---------------------- | ----------------------------------------------- | --------------------------------------- |
| Points to              | A single `int` (usually first element of array) | A full array of `N` integers            |
| Pointer arithmetic     | Moves 1 `int` at a time                         | Moves entire arrays (N * sizeof(int))   |
| Use of `&array`        | Not needed (`arr` decays to `int*`)             | Required to get pointer to entire array |
| Dereference and access | `ptr[i]`                                        | `(*ptr)[i]`                             |

---

## 📊 Use Cases of Pointer to an Array

1. ✅ **Passing entire arrays to functions**
   Ensures the size of the array is known to the function.

2. ✅ **Multidimensional arrays**
   Pointer to an array helps manage rows or columns cleanly.

3. ✅ **Structured data manipulation**
   Especially useful when dealing with blocks of data (e.g., sensor readings, matrix processing, etc.).

---

## 🧩 Simple Program Example

Here's a **minimal program** that demonstrates a **pointer to an array**:

```cpp
#include <iostream>
using namespace std;

int main() {
    int numbers[5] = {10, 20, 30, 40, 50};

    // Pointer to the entire array of 5 integers
    int (*ptr)[5] = &numbers;

    cout << "Accessing array elements using pointer to array:\n";

    for (int i = 0; i < 5; ++i) {
        cout << "Element " << i << ": " << (*ptr)[i] << endl;
    }

    return 0;
}
```

### 🔍 Output:

```
Accessing array elements using pointer to array:
Element 0: 10
Element 1: 20
Element 2: 30
Element 3: 40
Element 4: 50
```

### 🧠 What’s Happening:

* `ptr` points to the entire array `numbers`.
* `(*ptr)[i]` accesses the `i`-th element.
* We use `&numbers` (not `numbers`) to assign to `ptr`, since `numbers` is of type `int[5]`.

---

## 💡 Tips for Using `int (*ptr)[N]`

* ✅ Always assign with `&array`, not just `array`:

  ```cpp
  int arr[5];
  int (*ptr)[5] = &arr;  // ✅ correct
  ```

* ✅ Use `(*ptr)[i]` to access elements.

* ❌ Don’t confuse with `int* ptr = arr;` — that's just a pointer to first element.

* ✅ Excellent for passing arrays to functions while preserving size info.

---

## ✅ TL;DR

| Concept                     | Use                            |
| --------------------------- | ------------------------------ |
| `int* ptr`                  | Pointer to an integer          |
| `int (*ptr)[5]`             | Pointer to an array of 5 ints  |
| Use `&arr` with `(*ptr)[N]` | To get pointer to entire array |
| Access with `(*ptr)[i]`     | Dereference and index safely   |

---
