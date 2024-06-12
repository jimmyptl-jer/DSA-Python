def solution(x):
    """
    Count the number of digits in a given non-negative integer x.

    Parameters:
    x (int): The number whose digits are to be counted. Should be non-negative.

    Returns:
    int: The count of digits in the number x.
    """
    if x < 0:
        return "Input should be a non-negative integer"
    
    if x == 0:
        return 1

    res = 0

    while x > 0:
        x = x // 10
        res += 1
    
    print("Count of digits is " + str(res))
    return res

def test_solution():
   

    # Test case 2: Count digits of a single-digit number
    assert solution(5) == 1, "Test case 2 failed"  # 5 has 1 digit

    # Test case 3: Count digits of a two-digit number
    assert solution(25) == 2, "Test case 3 failed"  # 25 has 2 digits

    # Test case 4: Count digits of a larger number
    assert solution(12345) == 5, "Test case 4 failed"  # 12345 has 5 digits

    # Test case 5: Count digits of a very large number
    assert solution(9876543210) == 10, "Test case 5 failed"  # 9876543210 has 10 digits

    # Test case 6: Negative input
    assert solution(-1) == "Input should be a non-negative integer", "Test case 6 failed"

    print("All test cases pass")

# Run the test cases
test_solution()
