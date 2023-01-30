#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr, n):
    # Write your code here
    result = [0] * 100
    cnt = Counter(arr)
    for k, v in cnt.items():
        result[k] = v 
            
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr, n)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
