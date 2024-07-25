When dealing with rotated sorted arrays with duplicate elements, the binary search approach needs a slight adjustment to handle the cases where the presence of duplicates might disrupt the identification of the sorted halves. Specifically, when `arr[low] == arr[mid] == arr[high]`, it's not possible to determine which half is sorted. In such cases, we can simply increment `low` and decrement `high` to skip the duplicate values.

Here's the modified algorithm:

1. **Initialization:**
   - Initialize two pointers: `low` to 0 and `high` to the last index of the array.

2. **Iteration:**
   - Calculate the middle index `mid = (low + high) // 2`.
   - If `arr[mid] == target`, return `mid`.
   - If `arr[low] == arr[mid] == arr[high]`, increment `low` and decrement `high`.
   - If the left half is sorted (`arr[low] <= arr[mid]`):
     - If the target is within this sorted half (`arr[low] <= target < arr[mid]`), eliminate the right half by setting `high = mid - 1`.
     - Otherwise, eliminate the left half by setting `low = mid + 1`.
   - If the right half is sorted (`arr[mid] <= arr[high]`):
     - If the target is within this sorted half (`arr[mid] < target <= arr[high]`), eliminate the left half by setting `low = mid + 1`.
     - Otherwise, eliminate the right half by setting `high = mid - 1`.

Here's the complete Python code for the adjusted algorithm:

```python
def search_rotated_sorted_array_with_duplicates(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        
        # If duplicates are found at low, mid, and high, move pointers inward
        if arr[low] == arr[mid] == arr[high]:
            low += 1
            high -= 1
        elif arr[low] <= arr[mid]:
            # Left half is sorted
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            # Right half is sorted
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    
    return -1

# Example usage:
arr1 = [4, 5, 6, 7, 0, 1, 2, 3]
target1 = 0
print(f"The index of {target1} is: {search_rotated_sorted_array_with_duplicates(arr1, target1)}")

arr2 = [2, 5, 6, 0, 0, 1, 2]
target2 = 0
print(f"The index of {target2} is: {search_rotated_sorted_array_with_duplicates(arr2, target2)}")

arr3 = [2, 5, 6, 0, 0, 1, 2]
target3 = 3
print(f"The index of {target3} is: {search_rotated_sorted_array_with_duplicates(arr3, target3)}")
```

### Explanation of Code:
- The code initializes `low` and `high` pointers to the start and end of the array.
- It uses a loop to repeatedly calculate the middle index `mid` and compare the element at `mid` with the target.
- When encountering duplicates at `low`, `mid`, and `high`, it simply moves the `low` and `high` pointers inward.
- Depending on which half of the array is sorted and whether the target is in that half, it adjusts the `low` and `high` pointers to narrow down the search.
- If the target is found, it returns the index. If the loop completes without finding the target, it returns `-1`.
