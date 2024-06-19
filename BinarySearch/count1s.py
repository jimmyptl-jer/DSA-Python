# User function Template for python3

class Solution:
    ##Complete this code
    
    def firstOccurrence(self, arr, low, high, X):
        while low <= high:
            mid = (low + high) // 2
            if X < arr[mid]:
                return self.firstOccurrence(arr, low, mid - 1, X)
            elif X > arr[mid]:
                return self.firstOccurrence(arr, mid + 1, high, X)
            else:
                if mid == 0 or arr[mid] != arr[mid - 1]:
                    return mid
                else:
                    return self.firstOccurrence(arr, low, mid - 1, X)
        return -1
    
    def lastOccurrence(self, arr, low, high, X):
        while low <= high:
            mid = (low + high) // 2
            if X < arr[mid]:
                return self.lastOccurrence(arr, low, mid - 1, X)
            elif X > arr[mid]:
                return self.lastOccurrence(arr, mid + 1, high, X)
            else:
                if mid == len(arr) - 1 or arr[mid] != arr[mid + 1]:
                    return mid
                else:
                    return self.lastOccurrence(arr, mid + 1, high, X)
        return -1
    
    def countOnes(self, arr, N):
        low = 0
        high = len(arr) - 1
        X = 1
        
        first = self.firstOccurrence(arr, low, high, X)
        last = self.lastOccurrence(arr, low, high, X)
        
        if first >= 0 and last >= 0:
            return last - first + 1
        else:
            return 0

# Example usage:
solution = Solution()
arr = [1, 1, 1, 1, 1,0, 0]
N = len(arr)

count = solution.countOnes(arr, N)
print(count)  # Output should be 5
