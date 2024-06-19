class Solution:
    
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

# Example usage:
solution = Solution()
arr = [1, 1, 1, 1, 0, 0, 0]
N = len(arr)
X = 1

first_index = solution.firstOccurrence(arr, 0, N - 1, X)
last_index = solution.lastOccurrence(arr, 0, N - 1, X)

numberOfOccurrence = last_index - first_index + 1
print (numberOfOccurrence)

print("First occurrence of", X, "is at index:", first_index)  # Output should be 3
print("Last occurrence of", X, "is at index:", last_index)    # Output should be 4