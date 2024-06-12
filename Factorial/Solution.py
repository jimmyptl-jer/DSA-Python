def factorial(n):
    if n < 0:
        return None  # Factorial is not defined for negative numbers
    fact = 1  # Initialize fact to 1
    while n > 0:
        fact *= n  # Multiply fact by n
        n -= 1  # Decrement n
    return fact

# Example usage:
num = 5
print(f"The factorial of {num} is: {factorial(num)}")
