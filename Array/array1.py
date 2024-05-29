def solution(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                print("Target found:", arr[i], arr[j])
                return [arr[i], arr[j]]
    print("No pairs found that sum up to the target.")
    return None

# Test case
arr = [1, 2, 3, 4, 5]
target = 7
y =solution(arr, target)
print(y)