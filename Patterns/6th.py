def solution(row,col):

    for i in range(row+1):
        for j in range(row-i):
            print(j+1,end="")
        print()

solution(5, 5)