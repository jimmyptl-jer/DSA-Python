def solution(arr):
    res = []

    for x in arr:
        if x not in res:
            res.append(x)
    
    return res

def test_case_1():
    assert solution([]) == [], "Test case 1 failed"
    print("Test case 1 passed")

def test_case_2():
    assert solution([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Test case 2 failed"
    print("Test case 2 passed")

def test_case_3():
    assert solution([1, 1, 1, 1]) == [1], "Test case 3 failed"
    print("Test case 3 passed")

def test_case_4():
    assert solution([1, 2, 2, 3, 3, 4, 4, 5]) == [1, 2, 3, 4, 5], "Test case 4 failed"
    print("Test case 4 passed")

def test_case_5():
    assert solution([1, 2, 1, 3, 2, 4, 3, 5]) == [1, 2, 3, 4, 5], "Test case 5 failed"
    print("Test case 5 passed")

def test_case_6():
    assert solution([-1, -2, -2, -3, -1, 0]) == [-1, -2, -3, 0], "Test case 6 failed"
    print("Test case 6 passed")

def test_case_7():
    assert solution([1, "1", 2, "2", 1, "1"]) == [1, "1", 2, "2"], "Test case 7 failed"
    print("Test case 7 passed")

def test_case_8():
    large_array = list(range(1000)) + list(range(500))
    expected_result = list(range(1000))
    assert solution(large_array) == expected_result, "Test case 8 failed"
    print("Test case 8 passed")


def run_all_tests():
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
    test_case_6()
    test_case_7()
    test_case_8()
    print("All test cases passed")

# Run all test cases
run_all_tests()
