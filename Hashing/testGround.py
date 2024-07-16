def frequency_count(arr):
    n = len(arr)
    # Initialize a list of zeros with a length of the maximum element + 1
    hash_table = [0] * n 
    
    # Iterate through the array and count the frequency of each element
    for num in arr:
        index = num % n
        hash_table[index] += 1
    
    # Print the frequency of each element
    for i in range(len(hash_table)):
        if hash_table[i] > 0:
            print(f"{i}  {hash_table[i]}")

# Test cases
test_cases = [
    [1, 2, 2, 3, 3, 3],           # Normal case with duplicate elements
    [4, 5, 6, 7, 8, 9],           # Case with all distinct elements
    [0, 1, 2, 3, 4, 5,0, 1, 2, 3, 4, 5],           # Case where elements are 0 to n-1
    [0, 0, 0, 0, 0],              # Case with all elements the same
    [10, 20, 30, 40, 50],         # Case with elements larger than the length of the array
    [5, 3, 5, 3, 5],              # Case with multiple duplicates
    [],                           # Empty array
    [1],                          # Single element array
    [100, 200, 300, 400, 500]     # Large numbers
]

for i, test in enumerate(test_cases):
    print(f"Test case {i + 1}: {test}")
    frequency_count(test)
    print('-' * 40)
