#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr, n):
    # Write your code here
    plus = [x for x in arr if x > 0]
    minus = [x for x in arr if x < 0]
    zero = [x for x in arr if x == 0]
    return len(plus)/n, len(minus)/n, len(zero)/n

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    p, m, z = plusMinus(arr, n)

    print('%.6f' % p, file=sys.stdout)
    print('%.6f' % m, file=sys.stdout)
    print('%.6f' % z, file=sys.stdout)
