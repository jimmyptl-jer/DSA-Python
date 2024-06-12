def factorial(n):
    if n < 0:
        return None  # Factorial is not defined for negative numbers
    elif n == 0 or n == 1:
        return 1  # Base case: factorial of 0 and 1 is 1
    else:
        return n * factorial(n - 1)  # Recursive case: n! = n * (n-1)!

# Example usage:
num = 5
print(f"The factorial of {num} is: {factorial(num)}")
