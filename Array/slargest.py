def slargest(arr):
    
    if len(arr) < 2:
        return -1
    
    largest = arr[0]
    slargest = -1
    
    for i in arr:
        if  i > largest:
            slargest = largest
            largest = i
        elif i > slargest and i != largest:
            slargest = i
    
    return slargest

# Test case 1: Normal case with distinct elements
arr1 = [10, 20, 4, 45, 99]
print(slargest(arr1))  # Expected output: 45

# Test case 2: Array with duplicate elements
arr2 = [10, 10, 20, 20, 4, 4, 45, 45, 99, 99]
print(slargest(arr2))  # Expected output: 45

# Test case 3: Array with only one element
arr3 = [10]
print(slargest(arr3))  # Expected output: None

# Test case 4: Array with two elements
arr4 = [10, 20]
print(slargest(arr4))  # Expected output: 10

# Test case 5: Array with all elements the same
arr5 = [10, 10, 10]
print(slargest(arr5))  # Expected output: None

# Test case 6: Array with negative numbers
arr6 = [-10, -20, -4, -45, -99]
print(slargest(arr6))  # Expected output: -10
