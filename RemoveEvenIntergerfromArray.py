def removeEvenElement(arr):
    x = []
    y= []

    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            x.append(arr[i])
        else:
            y.append(arr[i])
    return x,y


# Test cases
test1 = [1, 2, 3, 4, 5, 6]
test2 = [2, 4, 6, 8, 10]
test3 = [1, 3, 5, 7, 9]
test4 = [2, 3, 6, 7, 9]


print(removeEvenElement(test1))  # Output should be [1, 3, 5]
print(removeEvenElement(test2))  # Output should be an empty list, as all elements are even
print(removeEvenElement(test3))  # Output should be the same as the input list, as there are no even elements
print(removeEvenElement(test4))  # Output should be [3, 7, 9]

