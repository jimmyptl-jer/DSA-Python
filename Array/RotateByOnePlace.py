def leftRotateByOne(arr):
    n = len(arr)
    if n <= 1:
        return arr
    
    temp = arr[0]  # Store the first element
    for i in range(1, n):
        arr[i-1] = arr[i]  # Shift elements to the left
    
    arr[n-1] = temp  # Place the first element at the end
    return arr


# Test case 1: Normal case
arr1 = [1, 2, 3, 4, 5]
print(leftRotateByOne(arr1))  # Expected output: [2, 3, 4, 5, 1]

# Test case 2: Array with one element
arr2 = [1]
print(leftRotateByOne(arr2))  # Expected output: [1]

# Test case 3: Empty array
arr3 = []
print(leftRotateByOne(arr3))  # Expected output: []

# Test case 4: Array with all elements the same
arr4 = [10, 10, 10, 10]
print(leftRotateByOne(arr4))  # Expected output: [10, 10, 10, 10]

# Test case 5: Array with negative numbers
arr5 = [-1, -2, -3, -4, -5]
print(leftRotateByOne(arr5))  # Expected output: [-2, -3, -4, -5, -1]
