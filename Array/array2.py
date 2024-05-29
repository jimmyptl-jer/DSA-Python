def solution(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                arr.remove(arr[j])
                break  # Exiting the loop after deleting the duplicate to avoid index out of range error
    return arr

# Test case
arr = [1, 1,2,2,3,3]
print(solution(arr))  # Expected output: [1, 2, 3, 4, 5]
