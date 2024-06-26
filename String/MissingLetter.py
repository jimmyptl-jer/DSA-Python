class Solution:
    def missingPanagram(self, s):
        s = s.lower()
        
        all_letters = set('abcdefghijklmnopqrstuvwxyz')
        
        found_letters = set()
        
        for char in s:
            found_letters.add(char)
            
        missing_letters = all_letters - found_letters
        
        if missing_letters:
            return ''.join(sorted(missing_letters))
        else:
            return -1
        
    
# Example usage:
solution = Solution()

# Test cases
# Case 1: All letters present (pangram)
print(solution.missingPanagram("the quick brown fox jumps over the lazy dog"))  # Output: -1

# Case 2: Missing multiple letters
print(solution.missingPanagram("hello world"))  # Output: "abcfgijkmnpqtuvxyz"

# Case 3: Empty string
print(solution.missingPanagram(""))  # Output: "abcdefghijklmnopqrstuvwxyz"

# Case 4: String with no alphabetic characters
print(solution.missingPanagram("12345!@#$%"))  # Output: "abcdefghijklmnopqrstuvwxyz"

# Case 5: String with only one alphabetic character
print(solution.missingPanagram("a"))  # Output: "bcdefghijklmnopqrstuvwxyz"

# Case 6: String with some letters missing
print(solution.missingPanagram("the quick brown fox jumps over"))  # Output: "adglvyz"

# Case 7: String with all letters except one
print(solution.missingPanagram("abcdefghijklmnopqrstuvwxy"))  # Output: "z"

# Case 8: String with repeated letters but missing some
print(solution.missingPanagram("aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyy"))  # Output: "z"
