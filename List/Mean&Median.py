class Solution:
    # Function to find median of the array elements.
    def median(self, A, N):
        A.sort()
        
        if N % 2 == 1:
            return (A[N // 2])
        else:
            return (A[(N // 2) - 1] + A[N // 2]) / 2
    
    # Function to find mean of the array elements.   
    def mean(self, A, N):
        sum_arr = sum(A)
        return int(sum_arr / N)


if __name__ == '__main__':
    sol = Solution()
    
    # Test Case 1: Odd Length Array
    A1 = [1, 2, 3, 4, 5]
    N1 = len(A1)
    print("Test Case 1:")
    print("Input Array:", A1)
    print("Expected Median:", 3)
    print("Returned Median:", sol.median(A1, N1))
    print("Expected Mean:", 3)
    print("Returned Mean:", sol.mean(A1, N1))
    print()
    
    # Test Case 2: Even Length Array
    A2 = [1, 2, 3, 4]
    N2 = len(A2)
    print("Test Case 2:")
    print("Input Array:", A2)
    print("Expected Median:", 2.5)
    print("Returned Median:", sol.median(A2, N2))
    print("Expected Mean:", 2.5)
    print("Returned Mean:", sol.mean(A2, N2))
    print()
    
    # Test Case 3: All Elements Same
    A3 = [5, 5, 5, 5]
    N3 = len(A3)
    print("Test Case 3:")
    print("Input Array:", A3)
    print("Expected Median:", 5)
    print("Returned Median:", sol.median(A3, N3))
    print("Expected Mean:", 5)
    print("Returned Mean:", sol.mean(A3, N3))
    print()
    
    # Test Case 4: Empty Array
    A4 = []
    N4 = len(A4)
    print("Test Case 4:")
    print("Input Array:", A4)
    # Handling of empty array case could involve a None return or error handling
    # print("Expected Median:", None)
    # print("Returned Median:", sol.median(A4, N4))
    # print("Expected Mean:", None)
    # print("Returned Mean:", sol.mean(A4, N4))
    print()
    
    # Test Case 5: Negative Numbers
    A5 = [-1, -2, -3, -4, -5]
    N5 = len(A5)
    print("Test Case 5:")
    print("Input Array:", A5)
    print("Expected Median:", -3)
    print("Returned Median:", sol.median(A5, N5))
    print("Expected Mean:", -3)
    print("Returned Mean:", sol.mean(A5, N5))
    print()
