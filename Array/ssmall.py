def ssmall(arr):
    
    if len(arr) < 2:
        return -1
    
    smallest = arr[0]
    second_smallest = -1
    
    for i in arr:
        
        if i < smallest:
            second_smallest = smallest
            smallest = i
        elif i < second_smallest and i!= smallest:
            second_smallest = i
    
    return second_smallest

# Test case 1: Normal case with distinct elements
arr1 = [10, 20, 4, 45, 99]
print(ssmall(arr1))  # Expected output: 10

# Test case 2: Array with duplicate elements
arr2 = [10, 10, 20, 20, 4, 4, 45, 45, 99, 99]
print(ssmall(arr2))  # Expected output: 10

# Test case 3: Array with only one element
arr3 = [10]
print(ssmall(arr3))  # Expected output: None


# Test case 5: Array with all elements the same
arr5 = [10, 10, 10]
print(ssmall(arr5))  # Expected output: None

