def sum_of_first_n(n):
    """
    Calculate the sum of the first n natural numbers.
    
    Parameters:
    n (int): The number up to which the sum is calculated.
    
    Returns:
    int: The sum of the first n natural numbers.
    """
    total = 0

    for i in range(1, n + 1):
        total += i
    return total


def test_sum_of_first_n():
    # Test case 1: Sum of first 0 natural numbers
    assert sum_of_first_n(0) == 0, "Test case 1 failed"

    # Test case 2: Sum of first 1 natural number
    assert sum_of_first_n(1) == 1, "Test case 2 failed"

    # Test case 3: Sum of first 5 natural numbers
    assert sum_of_first_n(5) == 15, "Test case 3 failed"  # 1 + 2 + 3 + 4 + 5 = 15

    # Test case 4: Sum of first 10 natural numbers
    assert sum_of_first_n(10) == 55, "Test case 4 failed"  # 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55

    # Test case 5: Sum of first 100 natural numbers
    assert sum_of_first_n(100) == 5050, "Test case 5 failed"  # Sum of first 100 numbers

    # Test case 6: Sum of first 1000 natural numbers
    assert sum_of_first_n(1000) == 500500, "Test case 6 failed"  # Sum of first 1000 numbers

    print("All test cases pass")

# Run the test cases
test_sum_of_first_n()
