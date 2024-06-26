def printIntersection(arr1, arr2, m, n):
    intersection = []
    i, j = 0, 0

    while i < m and j < n:
        if i > 0 and arr1[i] == arr1[i-1]:
            i = i + 1
            continue
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        else:
            # If elements are equal, add to intersection and move both pointers
            intersection.append(arr1[i])
            i += 1
            j += 1


    # Print the intersection array with spaces in between elements
    print(" ".join(map(str, intersection)))
    return intersection

# Driver program to test above function
arr1 = [1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 6]
arr2 = [2, 2, 3, 5, 7]
m = len(arr1)
n = len(arr2)
y = printIntersection(arr1, arr2, m, n)
print(y)
