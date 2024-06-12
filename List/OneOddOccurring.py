def solution(arr):
    for x in arr:
        count = 0
        for y in arr:
            if x == y:
                count += 1
        
        if count % 2 != 0:
            return x

def run_tests():
    assert solution([7]) == 7
    assert solution([1, 1, 2, 2, 3]) == 3
    assert solution([4, 5, 5, 4, 4]) == 4
    assert solution([10, 10, 20, 20, 30, 30, 30]) == 30
    assert solution([10, 10, 20, 20, 30, 30, 40, 40, 50, 50, 40]) == 40
    assert solution([5, 5, 6, 6, 7, 7, 8, 8, 8]) == 8
    assert solution([1, 2, 3, 2, 3, 1, 3]) == 3
    assert solution([1, 2, 1, 2, 3, 3, 4, 4, 5]) == 5
    assert solution([2, 2, 3, 3, 4, 4, 5, 5, 1]) == 1
    assert solution([6, 7, 7, 8, 8, 9, 9, 6, 10]) == 10
    assert solution([5, 5, 5, 5, 6]) == 6
    assert solution([7, 7, 7, 8, 8]) == 7

    print("All test cases passed!")

run_tests()
