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

def plusMinus(arr):
    # Write your code here
    sm, sp, sz = 0, 0, 0
    n = len(arr)
    for i in arr:
        if i < 0:
            sm += 1
        elif i > 0:
            sp += 1
        else:
            sz += 1
    print(sp/n, "\n", sm/n, "\n", sz/n)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)