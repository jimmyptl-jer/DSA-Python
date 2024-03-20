def findMaxValue(arr):
    x = arr[0]

    for i in range(len(arr)):
        if arr[i] > x:
            x = arr[i]
    
    return x

def findSecondMaxValue(arr):
    x = arr[0]
    y = 0

    for i in range(len(arr)):
        if arr[i] > x:
            y = x
            x = arr[i]
        elif arr[i] > y and arr[i] != x:
            y = arr[i]
    
    return y

# Test case
test_array = [9, 2, 5, 1, 7, 9]
max_value = findMaxValue(test_array)
second_max_value = findSecondMaxValue(test_array)
print("Second Max Value:", second_max_value)
print("Maximum value:", max_value)
