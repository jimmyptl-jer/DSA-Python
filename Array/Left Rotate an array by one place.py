def rotateByOne(arr):
    n = len(arr)

    if n <= 1:
        return arr
    
    temp = arr[0]  # Store the first element

    # Shift elements to the left
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    
    arr[n - 1] = temp  # Move the first element to the end

    return arr

arr = [1, 2, 3, 4, 5]
print(rotateByOne(arr))  # Output: [2, 3, 4, 5, 1]

arr = [5]
print(rotateByOne(arr))  # Output: [5]  # No change, since it has only one element

