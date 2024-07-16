def findMissingNumber(arr):
    n = len(arr)
    pointer = arr[0]
    
    for i in arr:
        if i != pointer:
            return pointer
        pointer += 1

# Test Cases
if __name__ == "__main__":
    # Test Case 1: Missing number at the beginning
    arr1 = [2, 3, 4, 5, 6]
    print("Test Case 1:", findMissingNumber(arr1))  # Expected Output: 2
    
    # Test Case 2: Missing number at the end
    arr2 = [1, 2, 3, 4, 6]
    print("Test Case 2:", findMissingNumber(arr2))  # Expected Output: 5
    
    # Test Case 3: Missing number in the middle
    arr3 = [1, 2, 4, 5, 6]
    print("Test Case 3:", findMissingNumber(arr3))  # Expected Output: 3
    
    # Test Case 4: All numbers present
    arr4 = [1, 2, 3, 4, 5]
    print("Test Case 4:", findMissingNumber(arr4))  # Expected Output: None (or no missing number)
    
    # Test Case 5: Single element array
    arr5 = [3]
    print("Test Case 5:", findMissingNumber(arr5))  # Expected Output: None (or no missing number)
    
    # Test Case 6: Large array with missing number
    arr6 = [100, 101, 102, 104, 105, 106, 107, 108]
    print("Test Case 6:", findMissingNumber(arr6))  # Expected Output: 103
