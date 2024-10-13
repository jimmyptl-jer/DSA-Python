def moveZero(arr):
    n = len(arr)

    if n <= 1:
        return arr
    
    j = 0

    for i in range(n):
        if arr[i] != 0:
            arr[j] = arr[i]
            j += 1

    while j < n:
        arr[j] = 0
        j += 1

    return arr

# Test Cases
# Test Case 1: Array with multiple zeros
arr1 = [0, 1, 0, 3, 12]
print(moveZero(arr1))  # Output: [1, 3, 12, 0, 0]

# Test Case 2: Array with all zeros
arr2 = [0, 0, 0, 0]
print(moveZero(arr2))  # Output: [0, 0, 0, 0]

# Test Case 3: Array with no zeros
arr3 = [5, 7, 9, 10]
print(moveZero(arr3))  # Output: [5, 7, 9, 10]

# Test Case 4: Empty array
arr4 = []
print(moveZero(arr4))  # Output: []

# Test Case 5: Single element array
arr5 = [0]
print(moveZero(arr5))  # Output: [0]

# Test Case 6: Array with non-zero followed by zeros
arr6 = [1, 2, 0, 0, 3]
print(moveZero(arr6))  # Output: [1, 2, 3, 0, 0]

# Test Case 7: Array with zeros at the beginning
arr7 = [0, 0, 1, 2, 3]
print(moveZero(arr7))  # Output: [1, 2, 3, 0, 0]

# Test Case 8: Mixed elements with zeros
arr8 = [4, 0, 5, 0, 6, 0, 7]
print(moveZero(arr8))  # Output: [4, 5, 6, 7, 0, 0, 0]
