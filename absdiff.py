#!/bin/python3

import math
import os
import random
import re
import sys


def minimumAbsoluteDifference(arr):
    arr.sort()
    min_diff = float('inf')
    for i in range(len(arr) - 1):
        diff = abs(arr[i] - arr[i + 1])
        if diff < min_diff:
            min_diff = diff
    return min_diff
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
