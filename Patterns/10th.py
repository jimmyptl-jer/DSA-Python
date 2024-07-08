def solution(row,col):

    for i in range(row+1):
        for j in range(i):
            print("*",end="")
        print()
    for i in range(row-1,0,-1):
        for j in range(i):
            print("*",end="")
        print()

solution(5, 5)