def findMinValue(arr):
    x = arr[0]

    for i in range(len(arr)):
        if arr[i] < x:
            x = arr[i]
    
    return x

# Test case
test_array = [9, 2, 5, 1, 7]
min_value = findMinValue(test_array)
print("Minimum value:", min_value)
