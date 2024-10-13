def findSecondLargest(arr):

    n = len(arr)

    if n < 2:
        return None
    
    max = secondMax = float('-inf')

    for num in arr:
        if num > max:
            secondMax = max
            max = num
        elif num > secondMax and num < max:
            secondMax = num
        
    if secondMax == float('-inf'):
        return None  # No second largest found
    
    return secondMax

arr = [10, 5, 20, 15]
print(findSecondLargest(arr))  # Output: 15

arr = [20, 20, 15, 15]
print(findSecondLargest(arr))  # Output: 15

arr = [5, 5, 5, 5]
print(findSecondLargest(arr))  # Output: None

arr = [5]
print(findSecondLargest(arr))  # Output: None

arr = [-1, -5, -10, -3]
print(findSecondLargest(arr))  # Output: -3


