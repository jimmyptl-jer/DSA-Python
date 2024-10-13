def unionOfSortedArrays(arr1, arr2):
    n, m = len(arr1), len(arr2)
    result = []
    
    i, j = 0, 0
    
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            if not result or result[-1] != arr1[i]:  # Avoid duplicates
                result.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            if not result or result[-1] != arr2[j]:  # Avoid duplicates
                result.append(arr2[j])
            j += 1
        else:  # Both are equal
            if not result or result[-1] != arr1[i]:  # Avoid duplicates
                result.append(arr1[i])
            i += 1
            j += 1
            
    # Add remaining elements of arr1
    while i < n:
        if not result or result[-1] != arr1[i]:  # Avoid duplicates
            result.append(arr1[i])
        i += 1
    
    # Add remaining elements of arr2
    while j < m:
        if not result or result[-1] != arr2[j]:  # Avoid duplicates
            result.append(arr2[j])
        j += 1
    
    return result

# Test Cases

# Test Case 1: Standard case
arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
print(unionOfSortedArrays(arr1, arr2))  # Output: [1, 2, 3, 4, 5, 6, 7]

# Test Case 2: One array is empty
arr1 = []
arr2 = [2, 3, 5, 7]
print(unionOfSortedArrays(arr1, arr2))  # Output: [2, 3, 5, 7]

# Test Case 3: Both arrays are empty
arr1 = []
arr2 = []
print(unionOfSortedArrays(arr1, arr2))  # Output: []

# Test Case 4: No common elements
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
print(unionOfSortedArrays(arr1, arr2))  # Output: [1, 2, 3, 4, 5, 6]

# Test Case 5: All elements are common
arr1 = [1, 2, 3]
arr2 = [1, 2, 3]
print(unionOfSortedArrays(arr1, arr2))  # Output: [1, 2, 3]

# Test Case 6: Duplicates in both arrays
arr1 = [1, 2, 2, 3]
arr2 = [2, 3, 4, 4]
print(unionOfSortedArrays(arr1, arr2))  # Output: [1, 2, 3, 4]

# Test Case 7: Large arrays
arr1 = [1, 3, 5, 7, 9]
arr2 = [2, 4, 6, 8, 10]
print(unionOfSortedArrays(arr1, arr2))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
