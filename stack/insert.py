class Solution:
    def InsertInStack(self,n,arr):
        #code here
        res = []
        while arr:
            res.append(arr.pop())
    
        return res

if __name__ == "__main__":
    n = 5
    arr = [1, 2, 3, 4, 5]
    
    solution = Solution()
    result = solution.InsertInStack(n, arr)
    
    print(f"Input: n = {n}, arr = {arr}")
    print(f"Output: {result}")
