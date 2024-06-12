class Solution:
    def isPalindrome(self, x: int) -> bool:
        # If the number is negative, it is not a palindrome
        if x < 0:
            return False

        # Initialize the divisor to find the leftmost digit
        div = 1
        while x >= 10 * div:
            div *= 10

        # Loop to compare digits from both ends towards the center
        while x:
            # Get the leftmost digit
            left = x // div
            # Get the rightmost digit
            right = x % 10

            # If the digits from both ends are not the same, it's not a palindrome
            if left != right:
                return False

            # Remove the leftmost and rightmost digits from x
            x = (x % div) // 10
            # Adjust the divisor to account for the two removed digits
            div //= 100

        # If all pairs of digits matched, the number is a palindrome
        return True

# Example usage:
sol = Solution()
print(sol.isPalindrome(12321))  # True
print(sol.isPalindrome(12345))  # False
