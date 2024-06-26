class Solution:
    def isPanagram(self,s):
        #your code here
        s = s.lower()
        string=s.replace(" ","")
        print(string)
        count = [0] * 256
        
        for char in string:
            count[ord(char)] = count[ord(char)] + 1 
        
       # Iterate through all lowercase alphabets
        for i in range(ord('a'), ord('z') + 1):
            if count[i] == 0:
                return 0
        
        return 1               


solution = Solution()


# Test case 2: Lowercase pangram
test_case2 = "the quick brown fox jumps over the lazy dog"
print(solution.isPanagram(test_case2))  # Output: 1

# Test case 3: Uppercase pangram
test_case3 = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
print(solution.isPanagram(test_case3))  # Output: 1

# Test case 4: Non-pangram string
test_case4 = "hello world"
print(solution.isPanagram(test_case4))  # Output: 0

# Test case 5: All alphabets present, but not pangram
test_case5 = "OqgPmuVccvfWDxHGSbqYtTPrpZJlrNSyhSmZVudpTvXZXIZlYGbEHKybgaVJuZvYYSxVvUtbaJladMtvNWsTdDiCgqkDfE"
print(solution.isPanagram(test_case5))  # Output: 0
