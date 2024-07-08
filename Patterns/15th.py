def solution(n):
    for i in range(n,0,-1):
        start = 65
        for j in range(i):
            print(chr(start),end=" ")
            start = start + 1
        print()
        
    
solution(5)
        
    