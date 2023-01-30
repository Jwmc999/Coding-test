#!/bin/python3

import math
import os
import random
import re
import sys
from heapq import heappush, heappop, heapify
#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    # Write your code here
    cnt = 0
    heapify(A)
    while True:
        if all(x>=k for x in A):
            return cnt
            break
    
        elif len(A) <= 1:
            return -1
            break
            
        else:
            x1 = A[0]
            heappop(A)
            x2 = A[0]
            heappop(A)
            swt = 1 * x1 + 2 * x2
            heappush(A, swt)
            cnt += 1

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
