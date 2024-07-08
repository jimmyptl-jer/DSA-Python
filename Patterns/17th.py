def solution(n):
    # Outer loop to handle the number of rows
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        
        char = 65  # ASCII value for 'A'
        breakpoint = 2 * i // 2  # Determine the breakpoint for character increment and decrement
        
        # Inner loop to handle the number of characters in each row
        for j in range(2 * i - 1):
            print(chr(char), end="")
            if j < breakpoint-1:  # Increment character until the midpoint
                char += 1
            else:  # Decrement character after the midpoint
                char -= 1
        
        # Print trailing spaces (not needed, can be removed)
        for j in range(n - i):
            print(" ", end="")
        
        # Move to the next line after each row
        print()

# Test the function with n = 5
solution(5)
