# C++ program for Merge Sort

```cpp
#include <iostream>
using namespace std;

// Function to merge two subarrays
void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1;  // size of left subarray
    int n2 = right - mid;     // size of right subarray

    // Create temp arrays
    int *L = new int[n1];
    int *R = new int[n2];

    // Copy data to temp arrays L[] and R[]
    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    // Merge the temp arrays back into arr[left..right]
    int i = 0; // Initial index of left subarray
    int j = 0; // Initial index of right subarray
    int k = left; // Initial index of merged subarray

    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    // Copy remaining elements of L[], if any
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    // Copy remaining elements of R[], if any
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }

    // Free memory
    delete[] L;
    delete[] R;
}

// Function to implement merge sort
void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        // Same as (l+r)/2, but avoids overflow for large l and r
        int mid = left + (right - left) / 2;

        // Sort first and second halves
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        // Merge the sorted halves
        merge(arr, left, mid, right);
    }
}

// Function to print array
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        cout << arr[i] << " ";
    cout << endl;
}

// Driver code
int main() {
    int arr[] = {12, 11, 13, 5, 6, 7};
    int size = sizeof(arr) / sizeof(arr[0]);

    cout << "Given array: ";
    printArray(arr, size);

    mergeSort(arr, 0, size - 1);

    cout << "Sorted array: ";
    printArray(arr, size);
    return 0;
}
```

 Here's an explanation of each line in the code:

### Preprocessor Directives:

```cpp
#include <iostream>
using namespace std;
```

* **`#include <iostream>`**: This includes the `iostream` library, which allows you to use standard input/output streams like `cout` (for printing) and `cin` (for input).
* **`using namespace std;`**: This allows you to use standard C++ library features (like `cout` and `endl`) without needing to prefix them with `std::`.

### Function to Merge Two Subarrays:

```cpp
void merge(int arr[], int left, int mid, int right) {
```

* **`merge(int arr[], int left, int mid, int right)`**: This function is responsible for merging two sorted subarrays (`arr[left..mid]` and `arr[mid+1..right]`) into a single sorted array.

The parameters `left`, `mid`, and `right` are **indexes** that specify the portion of the array .

### Meaning of the parameters:

* **`int left`**: The starting index of the subarray to be merged.
* **`int mid`**: The middle index, which separates the two halves that need to be merged.
* **`int right`**: The ending index of the subarray to be merged.

### Context (Merge Sort):

When performing merge sort, you divide the array recursively into two halves and then merge the sorted halves.

Let’s say we have an array:

```cpp
int arr[] = {2, 4, 1, 6, 8, 5, 3, 7};
```

Suppose we're merging the two sorted halves:

* Left subarray: `arr[left..mid]`
* Right subarray: `arr[mid+1..right]`

So, for example:

```cpp
left = 0
mid = 3
right = 7
```

Then:
* Left subarray: `arr[0..3] = {2, 4, 1, 6}`
* Right subarray: `arr[4..7] = {8, 5, 3, 7}`

The function will merge these two parts into a single sorted portion in `arr[0..7]`.


#### Inside the `merge` function:

```cpp
int n1 = mid - left + 1;  // size of left subarray
int n2 = right - mid;     // size of right subarray
```

* **`n1`** and **`n2`** calculate the sizes of the left and right subarrays.

```cpp
int *L = new int[n1];
int *R = new int[n2];
```

* Dynamically allocating memory for two temporary arrays `L` and `R` to hold the elements of the left and right subarrays.

   `n1` and `n2` are calculated **just before** allocating the arrays `L` and `R`. So a natural question arises:

> If `n1` and `n2` are known, why not just declare arrays like `int L[n1];` instead of using pointers and `new`?

Let’s clarify this step-by-step.

##### 🔍 The Real Reason: Where the Arrays Are Stored (Stack vs Heap)

Even though `n1` and `n2` are known at runtime **within the function**, they are **not constants** at compile-time. And that matters for how arrays are created.

##### ✅ In C++ (Standard C++):

You **cannot** do this:

```cpp
int n1 = mid - left + 1;
int L[n1]; // ❌ Error in standard C++
```

Why?

* Because standard C++ (pre-C++23) does **not support variable-length arrays (VLAs)** like C does.
* Array sizes must be **compile-time constants** unless you're using `new` or a container like `std::vector`.

So if you write:

```cpp
int *L = new int[n1];
```

You're telling the compiler:
* "I know `n1` at runtime, and I want memory for `n1` integers from the **heap**, not the stack."

---

```cpp
for (int i = 0; i < n1; i++)
    L[i] = arr[left + i];
for (int j = 0; j < n2; j++)
    R[j] = arr[mid + 1 + j];
```

* These loops copy the elements from the main array (`arr[]`) into the temporary arrays `L[]` and `R[]`.

```cpp
int i = 0; // Initial index of left subarray
int j = 0; // Initial index of right subarray
int k = left; // Initial index of merged subarray
```

* **`i`**, **`j`**, and **`k`** are indices for traversing the left subarray (`L`), the right subarray (`R`), and the main array (`arr[]`) respectively.

```cpp
while (i < n1 && j < n2) {
    if (L[i] <= R[j]) {
        arr[k] = L[i];
        i++;
    } else {
        arr[k] = R[j];
        j++;
    }
    k++;
}
```

* This is the main merging process: it compares the elements in `L[]` and `R[]` and places the smaller element into the correct position in `arr[]`. This loop continues until one of the subarrays (`L[]` or `R[]`) is exhausted.

```cpp
while (i < n1) {
    arr[k] = L[i];
    i++;
    k++;
}
```

* After the first loop, if any elements remain in `L[]` (i.e., `i < n1`), they are copied into the merged array `arr[]`.

```cpp
while (j < n2) {
    arr[k] = R[j];
    j++;
    k++;
}
```

* Similarly, if any elements remain in `R[]` (i.e., `j < n2`), they are copied into `arr[]`.

```cpp
delete[] L;
delete[] R;
```

* Finally, the dynamically allocated memory for `L[]` and `R[]` is freed using `delete[]`.

### Function to Perform Merge Sort:

```cpp
void mergeSort(int arr[], int left, int right) {
```

* **`mergeSort(int arr[], int left, int right)`**: This function is used to recursively divide the array into smaller subarrays and then merge them back together in sorted order.

#### Inside the `mergeSort` function:

```cpp
if (left < right) {
```

* The base condition of the recursion: If there is more than one element, we divide the array further. If `left >= right`, it's a single-element array (base case), and no further division is needed.

```cpp
int mid = left + (right - left) / 2;
```

* **`mid`** is the index of the middle element, calculated as the average of `left` and `right`. This formula avoids overflow that could occur when `left + right` is too large.

```cpp
mergeSort(arr, left, mid);
mergeSort(arr, mid + 1, right);
```

* These two recursive calls split the array into two halves: one from `left` to `mid`, and the other from `mid+1` to `right`.

These two recursive calls do the following:

1. **`mergeSort(arr, left, mid);`**
   * This call sorts the **left half** of the array.
   * It breaks down the portion of the array from index `left` to `mid`.

2. **`mergeSort(arr, mid + 1, right);`**
   * This call sorts the **right half** of the array.
   * It breaks down the portion from index `mid + 1` to `right`.

### Why we call it twice:
Merge Sort recursively splits the array into **two halves**, sorts them **independently**, and then **merges** them in sorted order.

##### Example:
If you have an array:
`[8, 4, 5, 2, 9, 1]`

1. First split:
   * Left half: `[8, 4, 5]`
   * Right half: `[2, 9, 1]`

2. Recursively sort each:
   * Sort `[8, 4, 5]` → `[4, 5, 8]`
   * Sort `[2, 9, 1]` → `[1, 2, 9]`

3. Merge the two sorted halves:
   * Merge `[4, 5, 8]` and `[1, 2, 9]` → `[1, 2, 4, 5, 8, 9]`
     
---
```cpp
merge(arr, left, mid, right);
```

* After the array has been divided into individual elements, the `merge` function is called to combine them into a sorted array.

### Function to Print the Array:

```cpp
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        cout << arr[i] << " ";
    cout << endl;
}
```

* **`printArray(int arr[], int size)`**: This function prints the elements of the array. It loops through the array from `0` to `size - 1` and prints each element, followed by a space.

### Driver Code:

```cpp
int main() {
```

* The entry point of the program.

```cpp
int arr[] = {12, 11, 13, 5, 6, 7};
```

* The array `arr[]` is initialized with unsorted values to be sorted by the merge sort algorithm.

```cpp
int size = sizeof(arr) / sizeof(arr[0]);
```

* **`size`** calculates the number of elements in the array by dividing the total size of the array by the size of a single element.

```cpp
cout << "Given array: ";
printArray(arr, size);
```

* This prints the initial (unsorted) array.

```cpp
mergeSort(arr, 0, size - 1);
```

* Calls the `mergeSort` function to sort the array `arr[]` from index `0` to `size - 1`.

```cpp
cout << "Sorted array: ";
printArray(arr, size);
```

* Prints the array after it has been sorted.

```cpp
return 0;
```

* Returns `0` to indicate the program has executed successfully.

### Summary:

This is an implementation of the **Merge Sort** algorithm, which is a **divide-and-conquer** algorithm. It recursively divides the array into two halves, sorts each half, and then merges them back together. The merge operation ensures that the array remains sorted as it is combined. The program also prints the array before and after sorting to demonstrate the result.

Hope this clears things up! Let me know if you have any more questions.

