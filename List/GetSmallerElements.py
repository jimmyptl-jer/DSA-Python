def getSmallerElements(arr, n, x):
    res = []
    for e in arr:
        if e < x:
            res.append(e)
            
    return res    
	

arr = [1, 12, 4, 25, 8, 10]
x = 11
n = len(arr)
print(getSmallerElements(arr, n, x), end ="")