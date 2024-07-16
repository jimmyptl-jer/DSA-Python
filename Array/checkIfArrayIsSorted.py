def solution(arr):
    n = len(arr)
    
    if n == 0:
        return True  # An empty array can be considered sorted
    elif n == 1:
        return True
    else:
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True

# Test case 1: Normal case with sorted elements
arr1 = [1, 2, 3, 4, 5]
print(solution(arr1))  # Expected output: True

# Test case 2: Normal case with unsorted elements
arr2 = [5, 3, 4, 2, 1]
print(solution(arr2))  # Expected output: False

# Test case 3: Empty array
arr3 = []
print(solution(arr3))  # Expected output: True

# Test case 4: Array with one element
arr4 = [10]
print(solution(arr4))  # Expected output: True

# Test case 5: Array with duplicate elements
arr5 = [1, 2, 2, 3, 3, 4, 4, 5]
print(solution(arr5))  # Expected output: True

# Test case 6: Array with negative numbers sorted
arr6 = [-10, -5, 0, 5, 10]
print(solution(arr6))  # Expected output: True

# Test case 7: Array with negative numbers unsorted
arr7 = [-10, -5, 0, 10, 5]
print(solution(arr7))  # Expected output: False

# Test case 8: Array with all elements the same
arr8 = [10, 10, 10]
print(solution(arr8))  # Expected output: True
