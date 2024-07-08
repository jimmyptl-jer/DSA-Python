def solution(n):
    num = 1
    for i in range(n+1):
        for j in range(i):
            print(num,end=" ")
            num = num + 1
        print()
        
    
solution(5)
        
    