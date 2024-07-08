def solution(n):
    start = 65
    for i in range(n):
        for j in range(i+1):
            print(chr(start),end=" ")
        print()
        start = start + 1
        
    
solution(5)
        
    