def matchingStrings(stringList, queries):
    # Write your code here
    
    m = len(stringList)
    n = len(queries)
    
    y = []

    for i in range(n):
        count = 0
        for j in range(m):   
            if queries[i] == stringList[j]:
                count = count + 1
        
        print(count)
        y.append(count)
    
    return y
            
stringList = ["ab", "ab", "abc"]
queries = ["ab", "abc", "bc"]
result = matchingStrings(stringList, queries)
print("Result:", result)
