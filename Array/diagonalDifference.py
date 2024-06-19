def diagonalDifference(arr):
    # Write your code here
    
    sumLeftToRight = 0
    sumRightToLeft = 0
 
    for i in range(len(arr)):
        sumLeftToRight = sumLeftToRight + arr[i][i]
        # print(arr[i][len(arr)- i - 1])
        sumRightToLeft = sumRightToLeft + arr[i][len(arr)- i - 1]
        

    print(sumLeftToRight)
    print(sumRightToLeft)
    return abs(sumLeftToRight - sumRightToLeft)

arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
y =diagonalDifference(arr)
print(y)