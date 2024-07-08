def solution(n):
    # Upper part of the pattern
    for i in range(n+1):
        # Print decreasing stars
        for j in range(n - i + 1):
            print("*", end=" ")
        
        # # Print increasing spaces
        for j in range(2 * i - 1):
            print(" ", end=" ")
        
        # Print decreasing stars again
        for j in range(n - i + 1):
            print("*", end=" ")
        
        # Move to the next line after completing the row
        print()
    
    # Lower part of the pattern
    for i in range(n+1, 0, -1):
        # Print increasing stars
        for j in range(n - i + 1):
            print("*", end=" ")
        
        # Print decreasing spaces
        for j in range(2 * i - 1):
            print(" ", end=" ")
        
        # Print increasing stars again
        for j in range(n - i + -1):
            print("*", end=" ")
        
        # Move to the next line after completing the row
        print()

# Test the function with n = 5
solution(5)
