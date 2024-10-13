def checkArrayIsSorted(arr):

    n = len(arr)

    if n <= 1:
        return True
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return False
        else:
            return True

arr = [1, 2, 3, 4, 5]
print(checkArrayIsSorted(arr))  # Output: True

arr = [5, 1, 3, 4]
print(checkArrayIsSorted(arr))  # Output: False

arr = [10]
print(checkArrayIsSorted(arr))  # Output: True

arr = [1, 2, 2, 4]
print(checkArrayIsSorted(arr))  # Output: True

arr = [5, 4, 3, 2, 1]
print(checkArrayIsSorted(arr))  # Output: False

arr = []
print(checkArrayIsSorted(arr))  # Output: True
