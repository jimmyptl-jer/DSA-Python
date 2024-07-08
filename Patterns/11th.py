def solution(n):


    for i in range(n+1):
        if i % 2 == 0:
            start = 0
        else:
            start = 1
        

        for j in range(i):
            print(start,end="")
            start = 1 - start
        print()
        
        


solution(5)
        
    