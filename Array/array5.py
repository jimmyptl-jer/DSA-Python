def plusOne(arr):
    # Start from the least significant digit
    carry = 1  # Initialize carry as 1 to increment by one
    
    # Traverse the array in reverse order
    for i in range(len(arr) - 1, -1, -1):
        total = arr[i] + carry  # Add the current digit with the carry
        arr[i] = total % 10  # Update the current digit to the remainder when divided by 10
        carry = total // 10  # Update the carry to the quotient when divided by 10
        
        # If carry becomes 0, no need to continue
        if carry == 0:
            break
    
    # If carry is still 1 after traversing all digits, add a new digit '1' at the beginning
    if carry == 1:
        arr.insert(0, 1)
    
    return arr

# Test cases
digits1 = [1, 2, 9]
print(plusOne(digits1))  # Expected output: [1, 2, 4]

digits2 = [4, 3, 2, 1]
print(plusOne(digits2))  # Expected output: [4, 3, 2, 2]

digits3 = [9]
print(plusOne(digits3))  # Expected output: [1, 0]
