A **Binary Heap** is a complete binary tree that satisfies the heap property. It is commonly used to implement priority queues due to its efficient insertion and extraction operations.

### Types of Binary Heaps:
1. **Max Heap:** 
   - The value of the parent node is always greater than or equal to the values of its child nodes.
   - The largest element is always at the root.
   
2. **Min Heap:**
   - The value of the parent node is always less than or equal to the values of its child nodes.
   - The smallest element is always at the root.

### Key Properties of a Binary Heap:
1. **Complete Binary Tree:**
   A binary heap is always a complete binary tree, meaning that all levels of the tree are completely filled except possibly the last level, which is filled from left to right.

2. **Heap Property:**
   - In a **Max Heap**, for every node `i`, the value of `i` is greater than or equal to its children.
   - In a **Min Heap**, for every node `i`, the value of `i` is less than or equal to its children.

### Representation of a Binary Heap:
Binary heaps are often implemented using **arrays**. For a node at index `i`:
   - The parent is at index `(i-1) // 2`.
   - The left child is at index `2*i + 1`.
   - The right child is at index `2*i + 2`.

This array-based representation simplifies the implementation and manipulation of the heap.

### Basic Operations:

1. **Insert:** 
   - Insert the new element at the end of the heap (maintain the complete tree property).
   - Then, "heapify" (or bubble up) the element by comparing it with its parent and swapping if necessary (to maintain the heap property).

2. **Extract Max (or Min):**
   - Remove the root (maximum for a max heap, minimum for a min heap).
   - Move the last element in the heap to the root.
   - Then, "heapify" (or bubble down) the root to restore the heap property.

3. **Heapify (Downward):**
   - Starting from the root, swap the current node with the larger (in max heap) or smaller (in min heap) of its children until the heap property is restored.

### Applications of Binary Heaps:
- **Priority Queues:** Binary heaps are commonly used to implement priority queues, where the element with the highest or lowest priority is always efficiently extracted.
- **Heapsort:** A sorting algorithm based on binary heaps, which has a time complexity of **O(n log n)**.
- **Graph Algorithms:** Binary heaps are used in algorithms like Dijkstra's shortest path algorithm and Prim's Minimum Spanning Tree (MST) algorithm to extract minimum-weight edges.

### Example: Max Heap

If you insert the following numbers into a Max Heap: 10, 20, 15, 30, 40, the tree would look like this:

```
        40
       /  \
     30    15
    /  \
  10    20
```

In array representation:
```
[40, 30, 15, 10, 20]
```