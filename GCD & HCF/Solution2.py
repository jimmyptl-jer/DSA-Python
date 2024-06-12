def solution(a, b):
    if b == 0:
        return a  # Base case: if b is 0, return a as the GCD
    
    return solution(b, a % b)  # Recursive case: call solution recursively with (b, a % b)

# Test cases
print(solution(12, 8))   # Output: 4 (GCD of 12 and 8 is 4)
print(solution(17, 5))   # Output: 1 (GCD of 17 and 5 is 1)
print(solution(60, 48))  # Output: 12 (GCD of 60 and 48 is 12)
