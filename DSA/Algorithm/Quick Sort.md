# C++ program for Quick Sort

## 🧩 High-Level Flow of the Program

### 🔹 1️⃣ **main()**

* Creates an array: `{10, 7, 8, 9, 1, 5}`
* Calculates size `n`
* Prints original array via `printArray()`
* Calls:

  ```cpp
  quickSort(arr, 0, n - 1);
  ```
* After sorting, prints the final array.

---

### 🔹 2️⃣ **quickSort(arr, low, high)**

Recursive function responsible for sorting.

#### Inside quickSort:

1. Check if the current subarray is valid (`low < high`)
2. Partition the array:

   ```cpp
   int pi = partition(arr, low, high);
   ```

   * This rearranges the subarray and returns the **pivot index**.
3. Recursively sort:

   * Left subarray (`low → pi-1`)
   * Right subarray (`pi+1 → high`)

So conceptually:

```
quickSort(arr, low, high)
    ├── partition() → divides array
    ├── quickSort(left)
    └── quickSort(right)
```

---

### 🔹 3️⃣ **partition(arr, low, high)**

This is the core step.

#### Process:

1. Picks the **pivot** = `arr[high]`
2. Keeps index `i` to track the smaller elements’ boundary.
3. Loops `j` from `low` → `high-1`:

   * If `arr[j] <= pivot`:
     increment `i` and `swap(arr[i], arr[j])`
4. Finally, put pivot in correct position:

   ```cpp
   swap(arr[i + 1], arr[high]);
   ```
5. Return `i + 1` → the final pivot index.

After partition:

* Elements left of pivot → smaller
* Elements right of pivot → larger

---

### 🔹 4️⃣ **printArray(arr, size)**

Simple utility to display array contents.

---

## ⚙️ Example Flow (Dry-Run Visualization)

For array `{10, 7, 8, 9, 1, 5}`

```
quickSort(arr, 0, 5)
 │
 ├─► partition(0, 5)
 │     pivot = 5
 │     → places pivot at index 1
 │     returns 1
 │
 ├─► quickSort(0, 0)   (left side)  → only one element → stop
 │
 └─► quickSort(2, 5)   (right side)
       │
       ├─► partition(2, 5)
       │     pivot = 10
       │     places pivot at index 5
       │     returns 5
       │
       ├─► quickSort(2, 4)
       │       ├─► partition(2, 4)
       │       │     pivot = 9
       │       │     places pivot at index 4
       │       ├─► quickSort(2,3)
       │       └─► quickSort(5,4) stop
       │
       └─► quickSort(6,5) stop
```

Finally → Sorted array: `{1, 5, 7, 8, 9, 10}`

---

## 🧩 Functional Hierarchy Diagram

```
main()
 ├── printArray()              # Show original
 ├── quickSort(arr,0,n-1)
 │      ├── partition()
 │      │       └── swap()    # Built-in, swaps elements
 │      ├── quickSort(left)
 │      │      ├── partition()
 │      │      └── ...
 │      └── quickSort(right)
 │             ├── partition()
 │             └── ...
 └── printArray()              # Show sorted
```

---


```cpp
#include <iostream>
using namespace std;

// Function to partition the array
int partition(int arr[], int low, int high) {
    int pivot = arr[high];  // Choose the last element as pivot
    int i = low - 1;        // Index of smaller element

    for (int j = low; j < high; j++) {
        // If current element is smaller than or equal to pivot
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);  // Swap arr[i] and arr[j]
        }
    }
    swap(arr[i + 1], arr[high]);  // Place pivot in correct position
    return i + 1;                 // Return pivot index
}

// Quick Sort function
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        // Partition index
        int pi = partition(arr, low, high);

        // Recursively sort elements before and after partition
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

// Utility function to print array
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        cout << arr[i] << " ";
    cout << endl;
}

// Driver code
int main() {
    int arr[] = {10, 7, 8, 9, 1, 5};
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "Original array: ";
    printArray(arr, n);

    quickSort(arr, 0, n - 1);

    cout << "Sorted array: ";
    printArray(arr, n);

    return 0;
}
```

### ✅ Example Output:

```
Original array: 10 7 8 9 1 5 
Sorted array: 1 5 7 8 9 10 
```

## Let's break down each line to explain what's happening:

### Preprocessor Directives:

```cpp
#include <iostream>
using namespace std;
```

* **`#include <iostream>`**: This includes the `iostream` library, which allows you to use standard input/output streams like `cout` (for printing) and `cin` (for input).
* **`using namespace std;`**: This allows you to use standard C++ library features (like `cout` and `endl`) without needing to prefix them with `std::`.

### Function to Partition the Array:

```cpp
int partition(int arr[], int low, int high) {
```

* **`partition(int arr[], int low, int high)`**: This function is used to divide the array into two parts: elements smaller than or equal to the pivot (to the left) and elements larger than the pivot (to the right).

#### Inside the `partition` function:

```cpp
int pivot = arr[high];  // Choose the last element as pivot
```

* **`pivot`**: The pivot element is chosen to be the last element in the current subarray (`arr[high]`).

```cpp
int i = low - 1;        // Index of smaller element
```

* **`i`**: `i` is the index that tracks the position of the last element that is smaller than or equal to the pivot. Initially, it is set to one position before the first element (`low - 1`).

```cpp
for (int j = low; j < high; j++) {
    // If current element is smaller than or equal to pivot
    if (arr[j] <= pivot) {
        i++;
        swap(arr[i], arr[j]);  // Swap arr[i] and arr[j]
    }
}
```

* **Loop (`for (int j = low; j < high; j++)`)**: This loop iterates through the array from index `low` to `high - 1`.
* **`if (arr[j] <= pivot)`**: If the current element is smaller than or equal to the pivot, we increment `i` and swap the elements `arr[i]` and `arr[j]`. This ensures that all elements smaller than or equal to the pivot are moved to the left of the pivot.

```cpp
swap(arr[i + 1], arr[high]);  // Place pivot in correct position
```

* After the loop finishes, the pivot needs to be placed in its correct position in the sorted array. It should be placed at index `i + 1`, which is the boundary between elements smaller than the pivot and elements larger than the pivot. So we swap the pivot (`arr[high]`) with `arr[i + 1]`.

```cpp
return i + 1;                 // Return pivot index
```

* Finally, the function returns the index of the pivot (`i + 1`), which is now in its correct position. This index will be used to divide the array into two subarrays: one to the left of the pivot and one to the right.

### Quick Sort Function:

```cpp
void quickSort(int arr[], int low, int high) {
```

* **`quickSort(int arr[], int low, int high)`**: This is the main function that implements the **Quick Sort** algorithm. It recursively sorts the subarrays.

#### Inside the `quickSort` function:

```cpp
if (low < high) {
```

* The base case for recursion. If the subarray has more than one element (`low < high`), the function proceeds to partition and sort the array. If there is only one element (`low >= high`), no sorting is needed.

```cpp
int pi = partition(arr, low, high);
```

* **`pi`**: Calls the `partition` function to partition the array and get the pivot's correct index. The pivot is now in its final position, and the elements are divided into two subarrays: one to the left and one to the right of the pivot.

```cpp
quickSort(arr, low, pi - 1);  // Recursively sort elements before the pivot
quickSort(arr, pi + 1, high); // Recursively sort elements after the pivot
```

* The array is now divided into two parts: the elements before the pivot (`low` to `pi - 1`) and the elements after the pivot (`pi + 1` to `high`).
* The `quickSort` function is recursively called on these two subarrays to sort them.

### Utility Function to Print the Array:

```cpp
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        cout << arr[i] << " ";
    cout << endl;
}
```

* **`printArray(int arr[], int size)`**: This function prints the elements of the array `arr[]` from index `0` to `size - 1`.
* The `for` loop iterates over the array and prints each element, followed by a space. Finally, `endl` is used to print a newline after the array.

### Driver Code:

```cpp
int main() {
```

* The entry point of the program.

```cpp
int arr[] = {10, 7, 8, 9, 1, 5};
```

* **`arr[]`**: The array to be sorted is initialized with some unsorted values.

```cpp
int n = sizeof(arr) / sizeof(arr[0]);
```

* **`n`**: The size of the array is calculated by dividing the total size of the array (`sizeof(arr)`) by the size of a single element (`sizeof(arr[0])`).

```cpp
cout << "Original array: ";
printArray(arr, n);
```

* This prints the original (unsorted) array using the `printArray` function.

```cpp
quickSort(arr, 0, n - 1);
```

* The `quickSort` function is called to sort the array `arr[]` from index `0` to `n - 1`.

```cpp
cout << "Sorted array: ";
printArray(arr, n);
```

* This prints the sorted array after the `quickSort` function has completed.

```cpp
return 0;
```

* The program returns `0`, which indicates successful execution.

### Quick Sort Overview:

* **Quick Sort** is a **divide-and-conquer** algorithm. It works by selecting a "pivot" element, then partitioning the array such that elements smaller than the pivot are on the left, and elements larger than the pivot are on the right. The process is recursively repeated on the subarrays formed by partitioning.
* The key operations are:

  1. **Partitioning**: Reordering the array such that all elements smaller than the pivot are on one side, and all elements greater than the pivot are on the other side.
  2. **Recursive Sorting**: The same process is applied recursively to the subarrays formed by dividing the array at the pivot.

### Time Complexity of Quick Sort:

* The **average time complexity** of Quick Sort is **O(n log n)**, where `n` is the number of elements in the array. However, in the worst case (when the pivot is always the smallest or largest element), it can degrade to **O(n²)**.

That's a detailed explanation of how this Quick Sort algorithm works!

