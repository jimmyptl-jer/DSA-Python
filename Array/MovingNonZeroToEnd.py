def moveZeroToEnd(arr):
    j = 0

    for i in range(len(arr)):
        if (arr[i] != 0 and arr[j] == 0):
            temp = arr[i]
            print("Temp:", temp)
            arr[i] = arr[j]
            print("arr[i]: ",arr[i])
            arr[j] = temp
        
        if arr[j] != 0:
            print("prining J",j)
            j = j + 1

        print("Loop")
    return arr

# Test case
test_array = [0, 1, 0, 3, 12]
result = moveZeroToEnd(test_array)
print("Array after moving zeros to end:", result)
