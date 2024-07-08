class Solution:
    def is_armstrong(self, x: int) -> int:
        original_num = x
        
        sum = 0
        while x > 0:
            last_digit = x % 10
            sum  = sum + last_digit * last_digit * last_digit
            x = x//10
        
        print(sum)
        if sum == original_num:
            return True
        else:
            return False


# Test cases
sol = Solution()

# Test case 1: Original number is 123
# Transformation: 1*3 + 2*3 + 3*3 = 3 + 6 + 9 = 18, which is not 123
print(f"Test case 1 - 123: {sol.is_armstrong(123)}")  # Expected: False

# Test case 2: Original number is 39
# Transformation: 3*3 + 9*3 = 9 + 27 = 36, which is not 39
print(f"Test case 2 - 39: {sol.is_armstrong(39)}")  # Expected: False

# Test case 3: Original number is 111
# Transformation: 1*3 + 1*3 + 1*3 = 3 + 3 + 3 = 9, which is not 111
print(f"Test case 3 - 111: {sol.is_armstrong(111)}")  # Expected: False

# Test case 4: Original number is 321
# Transformation: 3*3 + 2*3 + 1*3 = 9 + 6 + 3 = 18, which is not 321
print(f"Test case 4 - 321: {sol.is_armstrong(321)}")  # Expected: False

# Test case 5: Original number is 333
# Transformation: 3*3 + 3*3 + 3*3 = 9 + 9 + 9 = 27, which is not 333
print(f"Test case 5 - 333: {sol.is_armstrong(333)}")  # Expected: False

# Test case 6: Original number is 153
# Transformation: 1*3 + 5*3 + 3*3 = 3 + 15 + 9 = 27, which is not 153
print(f"Test case 6 - 153: {sol.is_armstrong(153)}")  # Expected: False

# Test case 7: Original number is 371
# Transformation: 3*3 + 7*3 + 1*3 = 9 + 21 + 3 = 33, which is not 371
print(f"Test case 7 - 371: {sol.is_armstrong(371)}")  # Expected: False