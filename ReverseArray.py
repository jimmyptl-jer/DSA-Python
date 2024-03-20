def reverseArray(arr):
    start_arr = 0
    end_arr = len(arr) -1

    while start_arr < end_arr:
        print(start_arr)
        print(end_arr)
        temp = arr[start_arr]
        arr[start_arr] = arr[end_arr]
        arr[end_arr] = temp
        start_arr += 1 
        end_arr -= 1

    return arr


# Test case
test_array = [1, 2, 3, 4, 5]
result = reverseArray(test_array)
print(result)
