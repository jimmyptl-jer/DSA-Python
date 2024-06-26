def partition(arr):
    n = len(arr)
    low = 0
    high = n - 1
    left = []
    right = []

    while low <= high:
        mid = (low+high)//2
    
    for i in range(0, mid + 1):  # Including mid in the left sublist
        left.append(arr[i])
        
    for j in range(mid + 1, n):  # Starting right sublist from mid+1
        right.append(arr[j])
    
    return left, right

# Test cases
test_cases = [
    ([1, 2, 3, 4], ([1, 2], [3, 4])),  # Even number of elements
    ([1, 2, 3, 4, 5], ([1, 2, 3], [4, 5])),  # Odd number of elements
    ([1], ([1], [])),  # Single element
    ([], ([], [])),  # Empty list
]

# Run test cases
for i, (input_arr, expected) in enumerate(test_cases):
    result = partition(input_arr)
    assert result == expected, f"Test case {i+1} failed: {result} != {expected}"
    print(f"Test case {i+1} passed!")

# If all test cases pass
print("All test cases passed!")
