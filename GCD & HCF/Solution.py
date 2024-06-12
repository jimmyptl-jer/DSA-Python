def solution(a, b):
    if a < 0 or b < 0:
        return False  # If either a or b is negative, return False (assuming GCD is not defined for negative numbers)

    while a != b:
        if a > b:
            a = a - b  # If a is greater than b, subtract b from a
        else:
            b = b - a  # If b is greater than a, subtract a from b
    
    return a  # When a == b, return the GCD

# Test cases
print(solution(12, 8))  # Output: 4 (GCD of 12 and 8 is 4)
print(solution(17, 5))  # Output: 1 (GCD of 17 and 5 is 1)
print(solution(60, 48))  # Output: 12 (GCD of 60 and 48 is 12)


