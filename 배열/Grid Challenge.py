#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#


def gridChallenge(grid):
    # Write your code here
    sortGrid = [sorted(s) for s in grid]
    
    cols = []
    for i in range(len(sortGrid[0])):
        cols.append([s[i] for s in sortGrid])

    ans = []
    for i in range(len(sortGrid[0])):
        if cols[i]==sorted(cols[i]):
            ans.append(True)
        else:
            ans.append(False)
            
    if all(ans):
        return "YES"
    else:
        return "NO"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
