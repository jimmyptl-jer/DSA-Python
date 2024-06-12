def second_largest(arr):

    if len(arr) <=1:
        return None
    
    lar = arr[0]
    slar = None

    for x in arr[1:]:
        if x > lar:
            slar = lar
            lar = x
        elif  x != lar:
            if slar is None or slar < x:
                slar = x
    
    return slar

# Test case 1: Array with multiple elements
arr1 = [1, 3, 4, 5, 0, 2]
print(f"Second largest in {arr1} is {second_largest(arr1)}")  # Expected output: 4

# Test case 2: Array with all elements the same
arr2 = [7, 7, 7, 7]
print(f"Second largest in {arr2} is {second_largest(arr2)}")  # Expected output: None

# Test case 3: Array with two elements
arr3 = [10, 20]
print(f"Second largest in {arr3} is {second_largest(arr3)}")  # Expected output: 10

# Test case 4: Array with one element
arr4 = [5]
print(f"Second largest in {arr4} is {second_largest(arr4)}")  # Expected output: None

# Test case 5: Array with negative and positive numbers
arr5 = [-10, -20, 5, 3, 1]
print(f"Second largest in {arr5} is {second_largest(arr5)}")  # Expected output: 3

# Test case 6: Empty array
arr6 = []
print(f"Second largest in {arr6} is {second_largest(arr6)}")  # Expected output: None
