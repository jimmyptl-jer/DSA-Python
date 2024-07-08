class Solution:
    def reverse(self, x: int) -> int:
        reverse_num = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)

        while x > 0:
            last_digit = x % 10
            reverse_num = reverse_num * 10 + last_digit
            x = x//10
        
        reverse_num = reverse_num * sign

        # Handle 32-bit signed integer overflow
        if reverse_num < -2**31 or reverse_num > 2**31 - 1:
            return 0
            
        return reverse_num