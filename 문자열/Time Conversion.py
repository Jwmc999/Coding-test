#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    tmp = [t for t in s[:-2].split(':')]
    if s[-2:] == "PM":
        if tmp[0] != '12':
            tmp[0] = int(tmp[0]) + 12
            tmp[0] = str(tmp[0])
    else:
        if tmp[0] == '12':
            tmp[0] = '00'
    
    result = ':'.join(tmp)
    return result

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
