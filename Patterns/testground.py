def solution(n):
    # Upper part of the pattern
    star = 1
    for i in range(1,n+1):
        # Print decreasing stars
        for j in range(n - i + 1):
            print("*", end=" ")
       
         # # Print increasing spaces
        for j in range(star - 1):
            print(" ", end=" ")

        for j in range(n - i + 1):
            print("*", end=" ")
        print()
        star = star + 2

    for i in range(n, 0, -1):
        # Print increasing stars
        for j in range(n - i + 1):
            print("*", end=" ")
        
        
        for j in range(2*i-2):
            print(" ", end=" ")
        
        for j in range(n - i + 1):
            print("*", end=" ")
        
        
        print()
solution(5)