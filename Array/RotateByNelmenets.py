#!/bin/python3

import math
# import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def reverse(arr, start, end):
    
        while start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            start = start + 1
            end = end - 1
        
       

def rotateLeft(self, d, arr):
    # Write your code here
    
        N = len(arr)
    
        d = d % N
        if d == 0:
            return
        
        self.reverse(arr, 0, d-1)
        self.reverse(arr, d, N-1)
        self.reverse(arr, 0, N-1)

# Test Case 1
arr1 = [1, 2, 3, 4, 5, 6, 7]
d1 = 2
print("Original Array:", arr1)
print("Left Rotated Array by", d1, "positions:", rotateLeft(d1, arr1.copy()))

# Test Case 2
arr2 = [10, 20, 30, 40, 50]
d2 = 3
print("Original Array:", arr2)
print("Left Rotated Array by", d2, "positions:", rotateLeft(d2, arr2.copy()))

