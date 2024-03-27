def solution(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 

# Test case
arr = [1, 2, 3, 4, 5, 6]
target = 4
print(solution(arr, target))  # Expected output: 3
