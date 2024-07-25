Sure! Let's go through the algorithm step by step with an example to find the target in a rotated sorted array. We'll use the example where `arr = [4, 5, 6, 7, 0, 1, 2, 3]` and `target = 0`.

### Step-by-Step Explanation:

1. **Initialization:**
   - Initialize two pointers: `low` to 0 and `high` to the last index of the array (7 in this case).

2. **First Iteration:**
   - Calculate the middle index `mid = (low + high) // 2`. For the initial values, `mid = (0 + 7) // 2 = 3`.
   - Check if `arr[mid] == target`. Here, `arr[3] = 7` which is not equal to 0.
   - Determine which half of the array is sorted:
     - Since `arr[low] <= arr[mid]` (`arr[0] = 4` and `arr[3] = 7`), the left half `[4, 5, 6, 7]` is sorted.
     - Check if the target is in this sorted half by verifying if `arr[low] <= target <= arr[mid]`. Since `0` is not in the range `[4, 7]`, eliminate the left half by setting `low = mid + 1`. Now, `low = 4`.

3. **Second Iteration:**
   - Calculate the new middle index `mid = (low + high) // 2 = (4 + 7) // 2 = 5`.
   - Check if `arr[mid] == target`. Here, `arr[5] = 1` which is not equal to 0.
   - Determine which half of the array is sorted:
     - Since `arr[low] <= arr[mid]` (`arr[4] = 0` and `arr[5] = 1`), the left half `[0, 1]` is sorted.
     - Check if the target is in this sorted half by verifying if `arr[low] <= target <= arr[mid]`. Since `0` is in the range `[0, 1]`, eliminate the right half by setting `high = mid - 1`. Now, `high = 4`.

4. **Third Iteration:**
   - Calculate the new middle index `mid = (low + high) // 2 = (4 + 4) // 2 = 4`.
   - Check if `arr[mid] == target`. Here, `arr[4] = 0` which is equal to 0.

Since `arr[mid]` is equal to the target, return the index `mid = 4`.

### Complete Python Code:

```python
def search_rotated_sorted_array(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        
        # Determine which half is sorted
        if arr[low] <= arr[mid]:
            # Left half is sorted
            if arr[low] <= target <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            # Right half is sorted
            if arr[mid] <= target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    
    return -1

# Example usage:
arr = [4, 5, 6, 7, 0, 1, 2, 3]
target = 0
print(f"The index of {target} is: {search_rotated_sorted_array(arr, target)}")

target = 3
print(f"The index of {target} is: {search_rotated_sorted_array(arr, target)}")
```

### Explanation of Code:
- The code initializes `low` and `high` pointers to the start and end of the array.
- It uses a loop to repeatedly calculate the middle index `mid` and compare the element at `mid` with the target.
- Depending on which half of the array is sorted and whether the target is in that half, it adjusts the `low` and `high` pointers to narrow down the search.
- If the target is found, it returns the index. If the loop completes without finding the target, it returns `-1`.
