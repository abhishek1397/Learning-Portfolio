# C++ program for Heap Sort

```cpp
#include <iostream>
using namespace std;

// Function to heapify a subtree rooted at index i
// n is the size of the heap
void heapify(int arr[], int n, int i) {
    int largest = i;        // Initialize largest as root
    int left = 2 * i + 1;   // left child index
    int right = 2 * i + 2;  // right child index

    // If left child is larger than root
    if (left < n && arr[left] > arr[largest])
        largest = left;

    // If right child is larger than largest so far
    if (right < n && arr[right] > arr[largest])
        largest = right;

    // If largest is not root
    if (largest != i) {
        swap(arr[i], arr[largest]); // Swap root with largest child

        // Recursively heapify the affected subtree
        heapify(arr, n, largest);
    }
}

// Main function to do Heap Sort
void heapSort(int arr[], int n) {
    // Step 1: Build max heap
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    // Step 2: Extract elements from heap one by one
    for (int i = n - 1; i > 0; i--) {
        // Move current root (largest) to end
        swap(arr[0], arr[i]);

        // Call max heapify on the reduced heap
        heapify(arr, i, 0);
    }
}

// Utility function to print array
void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
}

// Driver code
int main() {
    int arr[] = {12, 11, 13, 5, 6, 7};
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "Original array: ";
    printArray(arr, n);

    heapSort(arr, n);

    cout << "Sorted array: ";
    printArray(arr, n);

    return 0;
}
```

### ✅ Example Output:

```
Original array: 12 11 13 5 6 7 
Sorted array: 5 6 7 11 12 13 
```

## Let’s break down each part of the code.

### Preprocessor Directives:

```cpp
#include <iostream>
using namespace std;
```

* **`#include <iostream>`**: This includes the `iostream` library, which is necessary for input/output operations, specifically for printing with `cout`.
* **`using namespace std;`**: This allows us to use the standard C++ library features like `cout` without needing to prefix them with `std::`.

### Heapify Function:

```cpp
void heapify(int arr[], int n, int i) {
```

* **`heapify(int arr[], int n, int i)`**: This function is used to maintain the **heap property** of the heap. Specifically, it ensures that the subtree rooted at index `i` is a **max heap**. A max heap is a binary tree where the parent node is larger than or equal to its children.

#### Inside the `heapify` function:

```cpp
int largest = i;        // Initialize largest as root
int left = 2 * i + 1;   // left child index
int right = 2 * i + 2;  // right child index
```

* **`largest`**: This keeps track of the largest element among the root, left child, and right child.
* **`left`** and **`right`**: These calculate the indices of the left and right children of the current node using the formulas for a binary heap structure. For any element at index `i`:

  * Left child index = `2 * i + 1`
  * Right child index = `2 * i + 2`

```cpp
if (left < n && arr[left] > arr[largest])
    largest = left;
```

* This checks if the left child exists (`left < n`) and if it is larger than the current largest element. If so, we update `largest` to be the index of the left child.

```cpp
if (right < n && arr[right] > arr[largest])
    largest = right;
```

* Similarly, this checks if the right child exists (`right < n`) and if it is larger than the current largest element. If so, we update `largest` to be the index of the right child.

```cpp
if (largest != i) {
    swap(arr[i], arr[largest]); // Swap root with largest child
    heapify(arr, n, largest);   // Recursively heapify the affected subtree
}
```

* **`if (largest != i)`**: If the largest element is not the root (index `i`), we swap the root with the largest child.
* **`heapify(arr, n, largest)`**: After the swap, the affected subtree might no longer be a heap, so we recursively call `heapify` on the subtree rooted at `largest`.

### Heap Sort Function:

```cpp
void heapSort(int arr[], int n) {
```

* **`heapSort(int arr[], int n)`**: This is the main function for **Heap Sort**. It first builds a max heap and then sorts the array by repeatedly extracting the root (the maximum element) and placing it at the end of the array.

#### Inside the `heapSort` function:

```cpp
for (int i = n / 2 - 1; i >= 0; i--)
    heapify(arr, n, i);
```

* This loop is used to **build the max heap**. It starts from the last non-leaf node (`n / 2 - 1`) and moves upwards to the root (index `0`).
* **`heapify(arr, n, i)`** is called to ensure the subtree rooted at each node satisfies the heap property.

```cpp
for (int i = n - 1; i > 0; i--) {
    swap(arr[0], arr[i]);  // Move current root (largest) to end
    heapify(arr, i, 0);     // Call max heapify on the reduced heap
}
```

* This second loop is responsible for **sorting the heap**. It extracts the largest element (root) of the heap and moves it to the end of the array. Then, it reduces the heap size by 1 and calls `heapify` to restore the heap property on the remaining part of the array.

  * **`swap(arr[0], arr[i])`**: Swap the root (largest element) with the last element in the array. Now the root is in its correct position.
  * **`heapify(arr, i, 0)`**: After the swap, the root might not satisfy the heap property anymore. Therefore, we call `heapify` on the root (index `0`) of the reduced heap.

### Utility Function to Print the Array:

```cpp
void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
}
```

* **`printArray(int arr[], int n)`**: This function prints the array. It loops through the array and prints each element followed by a space. After printing all elements, it prints a newline (`endl`).

### Driver Code:

```cpp
int main() {
```

* The entry point of the program.

```cpp
int arr[] = {12, 11, 13, 5, 6, 7};
```

* **`arr[]`**: The array to be sorted is initialized with unsorted values.

```cpp
int n = sizeof(arr) / sizeof(arr[0]);
```

* **`n`**: This calculates the number of elements in the array. It divides the total size of the array by the size of one element to get the number of elements.

```cpp
cout << "Original array: ";
printArray(arr, n);
```

* This prints the original (unsorted) array using the `printArray` function.

```cpp
heapSort(arr, n);
```

* The `heapSort` function is called to sort the array `arr[]`.

```cpp
cout << "Sorted array: ";
printArray(arr, n);
```

* This prints the sorted array after the `heapSort` function has completed.

```cpp
return 0;
```

* The program returns `0`, indicating successful execution.

### Heap Sort Overview:

* **Heap Sort** is a **comparison-based** sorting algorithm that works by leveraging a **binary heap** data structure. It has two main stages:

  1. **Building the max heap**: The array is rearranged to satisfy the heap property (where every parent node is greater than or equal to its child nodes).
  2. **Sorting**: The largest element (root of the heap) is repeatedly swapped with the last element of the heap and the heap size is reduced. After each extraction, the heap is reheapified to maintain the heap property.

### Time Complexity of Heap Sort:

* **Building the max heap**: This takes **O(n)** time, as the heapify operation is called for each non-leaf node.
* **Extracting elements**: Each extraction requires **O(log n)** time for reheapifying. Since there are `n` elements, this gives a total of **O(n log n)** time complexity for sorting.

Thus, the overall time complexity of Heap Sort is **O(n log n)** in both the worst and average cases, making it efficient for large datasets.

### Space Complexity:

* **Heap Sort** has a space complexity of **O(1)** because it is an **in-place** sorting algorithm (it doesn't require any extra space for a separate data structure like quicksort or mergesort).



