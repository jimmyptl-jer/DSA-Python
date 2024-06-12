def solution(arr):
    if len(arr) <= 1:
        return True  # An array with 0 or 1 element is considered sorted.
    
    for i in range(len(arr) - 1):  # Use range(len(arr) - 1) to avoid index out of bounds error
        if arr[i] > arr[i + 1]:
            return False
    
    return True

def test_solution():
    # Test case 1: Empty array
    assert solution([]) == True, "Test case 1 failed"
    
    # Test case 2: Single element array
    assert solution([1]) == True, "Test case 2 failed"
    
    # Test case 3: Already sorted array
    assert solution([1, 2, 3, 4, 5]) == True, "Test case 3 failed"
    
    # Test case 4: Array with elements in descending order
    assert solution([5, 4, 3, 2, 1]) == False, "Test case 4 failed"
    
    # Test case 5: Array with elements in random order
    assert solution([3, 1, 4, 2, 5]) == False, "Test case 5 failed"
    
    # Test case 6: Array with repeated elements
    assert solution([1, 2, 2, 3, 3, 4, 4, 5]) == True, "Test case 6 failed"
    
    # Test case 7: Array with some elements out of order
    assert solution([1, 3, 2, 4, 5]) == False, "Test case 7 failed"
    
    # Test case 8: Large sorted array
    assert solution(list(range(1000))) == True, "Test case 8 failed"
    
    # Test case 9: Large unsorted array
    large_unsorted_array = list(range(1000))
    large_unsorted_array[500], large_unsorted_array[501] = large_unsorted_array[501], large_unsorted_array[500]
    assert solution(large_unsorted_array) == False, "Test case 9 failed"
    
    print("All test cases pass")

# Run the test cases
test_solution()
