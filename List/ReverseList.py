def solution(arr):

    if len(arr) <=1:
        return arr
    
    left = 0
    right = len(arr) -1

    while left < right:
        arr[left],arr[right] = arr[right],arr[left]

        left = left + 1
        right = right -1
    
    return arr

def test_case_3():
    assert solution([1, 2]) == [2, 1], "Test case 3 failed"
    print("Test case 3 passed")

def test_solution():
    # Test case 1: Empty array
    assert solution([]) == [], "Test case 1 failed"
    
    # Test case 2: Single element array
    assert solution([1]) == [1], "Test case 2 failed"
    
    # Test case 3: Array with two elements
    assert solution([1, 2]) == [2, 1], "Test case 3 failed"
    
    # Test case 4: Array with multiple elements
    assert solution([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1], "Test case 4 failed"
    
    # Test case 5: Array with repeated elements
    assert solution([1, 2, 2, 3, 3, 4, 4, 5]) == [5, 4, 4, 3, 3, 2, 2, 1], "Test case 5 failed"
    
    # Test case 6: Array with all elements the same
    assert solution([1, 1, 1, 1]) == [1, 1, 1, 1], "Test case 6 failed"
    
    # Test case 7: Array with odd number of elements
    assert solution([1, 2, 3]) == [3, 2, 1], "Test case 7 failed"
    
    # Test case 8: Large array
    assert solution(list(range(1000))) == list(range(999, -1, -1)), "Test case 8 failed"
    
    print("All test cases pass")

# Run the test cases
test_solution()
