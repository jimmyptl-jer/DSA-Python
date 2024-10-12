def merge_sort(arr):
    if len(arr) > 1:
        # Finding the middle of the array
        mid = len(arr) // 2
        
        # Dividing the array into two halves
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Recursive call on each half
        merge_sort(left_half)
        merge_sort(right_half)
        
        # Initialize pointers for left_half, right_half, and merged array
        i = j = k = 0
        
        # Merge the two halves back together
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        # Check if any elements were left in left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        # Check if any elements were left in right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# Test cases
def run_tests():
    # Test Case 1: Empty List
    arr1 = []
    expected1 = []
    print("Test Case 1 Passed" if merge_sort(arr1) == expected1 else "Test Case 1 Failed")
    
    # Test Case 2: Single Element List
    arr2 = [1]
    expected2 = [1]
    print("Test Case 2 Passed" if merge_sort(arr2) == expected2 else "Test Case 2 Failed")
    
    # Test Case 3: Already Sorted List
    arr3 = [1, 2, 3, 4, 5]
    expected3 = [1, 2, 3, 4, 5]
    print("Test Case 3 Passed" if merge_sort(arr3) == expected3 else "Test Case 3 Failed")
    
    # Test Case 4: Reverse Sorted List
    arr4 = [5, 4, 3, 2, 1]
    expected4 = [1, 2, 3, 4, 5]
    print("Test Case 4 Passed" if merge_sort(arr4) == expected4 else "Test Case 4 Failed")
    
    # Test Case 5: List with Duplicates
    arr5 = [4, 2, 4, 3, 1, 2]
    expected5 = [1, 2, 2, 3, 4, 4]
    print("Test Case 5 Passed" if merge_sort(arr5) == expected5 else "Test Case 5 Failed")
    
    # Test Case 6: Large List
    arr6 = [38, 27, 43, 3, 9, 82, 10]
    expected6 = [3, 9, 10, 27, 38, 43, 82]
    print("Test Case 6 Passed" if merge_sort(arr6) == expected6 else "Test Case 6 Failed")

# Run all tests
run_tests()
