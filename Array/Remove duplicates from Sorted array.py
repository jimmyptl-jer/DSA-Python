def removeDuplicate(arr):
    n = len(arr)

    if n <=1:
        return arr
    
    unique_arr = []
    for i in arr:
        if i not in unique_arr:
            unique_arr.append(i)

    return unique_arr

arr = [1, 2, 2, 3, 4, 4, 5]
print(removeDuplicate(arr))  # Output: [1, 2, 3, 4, 5]

arr = [10, 20, 30, 40, 50]
print(removeDuplicate(arr))  # Output: [10, 20, 30, 40, 50]


arr = []
print(removeDuplicate(arr))  # Output: []

arr = [99]
print(removeDuplicate(arr))  # Output: [99]

arr = [5, 5, 5, 5, 5]
print(removeDuplicate(arr))  # Output: [5]

arr = [7, 2, 5, 2, 5, 9, 1]
print(removeDuplicate(arr))  # Output: [7, 2, 5, 9, 1]
