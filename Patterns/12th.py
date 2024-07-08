def solution(n):
    for i in range(n,0,-1):
        for j in range(n - i):
            print(j+1, end="")
        for j in range(2 * i - 1):
            print(" ", end="")
        for j in range(n - i ,0,-1):
            print(j, end="")
        print()

# Test cases for the corrected function
solution(6)
 