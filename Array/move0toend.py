def moveZeroToEnd(arr):
    n = len(arr)
    pointer = 0
    
    # Move non-zero elements to the front
    for i in range(n):
        if arr[i] != 0:
            arr[pointer] = arr[i]
            pointer += 1
    
    # Fill the remaining elements with zeros
    while pointer < n:
        arr[pointer] = 0
        pointer += 1

# Test Cases
if __name__ == "__main__":
    # Test Case 1: Basic Case - Mixed Elements
    arr1 = [0, 1, 0, 3, 12]
    moveZeroToEnd(arr1)
    print("Test Case 1:", arr1)  # Expected Output: [1, 3, 12, 0, 0]
    
    # Test Case 2: All Zeros
    arr2 = [0, 0, 0, 0, 0]
    moveZeroToEnd(arr2)
    print("Test Case 2:", arr2)  # Expected Output: [0, 0, 0, 0, 0]
    
    # Test Case 3: No Zeros
    arr3 = [1, 2, 3, 4, 5]
    moveZeroToEnd(arr3)
    print("Test Case 3:", arr3)  # Expected Output: [1, 2, 3, 4, 5]
    
    # Test Case 4: Empty Array
    arr4 = []
    moveZeroToEnd(arr4)
    print("Test Case 4:", arr4)  # Expected Output: []
    
    # Test Case 5: Mixed Elements with Leading Zeros
    arr5 = [0, 0, 1, 0, 3, 12]
    moveZeroToEnd(arr5)
    print("Test Case 5:", arr5)  # Expected Output: [1, 3, 12, 0, 0, 0]
    
    # Test Case 6: Large Array with Random Numbers
    arr6 = [4, 2, 0, 1, 0, 3, 0, 12, 0]
    moveZeroToEnd(arr6)
    print("Test Case 6:", arr6)  # Expected Output: [4, 2, 1, 3, 12, 0, 0, 0, 0]
