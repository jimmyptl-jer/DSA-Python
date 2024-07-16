def preprocess_lowercase(s):
    """
    Preprocess the input string to compute the frequency of each lowercase letter.
    
    Parameters:
    s (str): The input string containing only lowercase letters.
    
    Returns:
    list: A list of size 26 where each index corresponds to the frequency of a lowercase letter.
          The index 0 corresponds to 'a', index 1 to 'b', ..., index 25 to 'z'.
    """
    # Create a hash array of size 26 for lowercase letters ('a' to 'z')
    hash_array = [0] * 26
    
    # Iterate over each character in the string
    for char in s:
        # Compute the index for the character by subtracting the ASCII value of 'a'
        index = ord(char) - ord('a')
        # Increment the frequency count for the character at the computed index
        hash_array[index] += 1
    
    return hash_array

def query_lowercase(hash_array, char):
    """
    Query the frequency of a specific lowercase letter using the precomputed hash array.
    
    Parameters:
    hash_array (list): The precomputed hash array containing frequencies of lowercase letters.
    char (str): The lowercase letter to query the frequency of.
    
    Returns:
    int: The frequency of the specified lowercase letter.
    """
    # Compute the index for the character by subtracting the ASCII value of 'a'
    index = ord(char) - ord('a')
    # Return the frequency count for the character at the computed index
    return hash_array[index]

# Example usage
s = "abcdabehf"
hash_array = preprocess_lowercase(s)

# Queries to test the frequency of specific characters
queries = ['a', 'g', 'h', 'b', 'c']
for q in queries:
    print(f"Frequency of '{q}': {query_lowercase(hash_array, q)}")

# Additional Test Cases
print("\nAdditional Test Cases:")

# Test case 1: All letters present
s1 = "abcdefghijklmnopqrstuvwxyz"
hash_array1 = preprocess_lowercase(s1)
queries1 = ['a', 'z', 'm', 'c', 'k']
for q in queries1:
    print(f"Frequency of '{q}' in '{s1}': {query_lowercase(hash_array1, q)}")

# Test case 2: Multiple occurrences of letters
s2 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz"
hash_array2 = preprocess_lowercase(s2)
queries2 = ['a', 'b', 'z', 'm', 'n']
for q in queries2:
    print(f"Frequency of '{q}' in '{s2}': {query_lowercase(hash_array2, q)}")

# Test case 3: Single character string
s3 = "a"
hash_array3 = preprocess_lowercase(s3)
queries3 = ['a', 'b', 'c']
for q in queries3:
    print(f"Frequency of '{q}' in '{s3}': {query_lowercase(hash_array3, q)}")

# Test case 4: Repeated characters
s4 = "aaaaaaa"
hash_array4 = preprocess_lowercase(s4)
queries4 = ['a', 'b', 'c']
for q in queries4:
    print(f"Frequency of '{q}' in '{s4}': {query_lowercase(hash_array4, q)}")
