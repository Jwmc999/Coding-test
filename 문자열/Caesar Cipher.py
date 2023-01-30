#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    decode = ''
    for ch in s:
        if 'a' <= ch <= 'z':
            if ord(ch) + k > ord('z'):
                decode += chr((ord(ch) - 97 + k)%26 + 97)
            else:
                decode += chr(ord(ch) + k)
        elif 'A' <= ch <= 'Z':
            if ord(ch) + k > ord('Z'):
                decode += chr((ord(ch) - 65 + k)%26 + 65)
            else:
                decode += chr(ord(ch) + k)
        else:
            decode += ch
    return decode

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
