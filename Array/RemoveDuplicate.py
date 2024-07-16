def removeDuplicate(arr):
    n = len(arr)
    pointer = 1
    
    for i in range(1,n):
            if arr[i - 1] != arr[i]:
                arr[pointer] = arr[i]
                pointer = pointer + 1
    
    return arr[:pointer]

# Test case 1: Normal case with duplicates
arr1 = [1, 2, 2, 3, 4, 4, 5]
print(removeDuplicate(arr1))  # Expected output: [1, 2, 3, 4, 5]

# Test case 2: Array with no duplicates
arr2 = [1, 2, 3, 4, 5]
print(removeDuplicate(arr2))  # Expected output: [1, 2, 3, 4, 5]

# Test case 3: Empty array
arr3 = []
print(removeDuplicate(arr3))  # Expected output: []

# Test case 4: Array with all elements the same
arr4 = [10, 10, 10, 10]
print(removeDuplicate(arr4))  # Expected output: [10]

# Test case 5: Array with negative numbers
arr5 = [-1, -2, -2, -3, -4, -4, -5]
print(removeDuplicate(arr5))  # Expected output: [-1, -2, -3, -4, -5]


