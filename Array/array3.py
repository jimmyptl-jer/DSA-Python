def solution(arr, target):
    result = []
    for i in range(len(arr)):
        if arr[i] != target:
            result.append(arr[i])
            
    
    return result

# Test case
arr = [1, 2, 3, 4, 5, 5, 6]
target = 5
print(solution(arr, target))  # Expected output: [1, 2, 3, 4, 5, 6]
