def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        print( 'Iteration',i)
        for j in range (n-1):
            print (arr[j],arr[j+1])
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr        
        
      

print(bubble_sort([1, 5, 3, 2]))  # Output: [1, 2, 3, 5]
print(bubble_sort([3, 1])) 