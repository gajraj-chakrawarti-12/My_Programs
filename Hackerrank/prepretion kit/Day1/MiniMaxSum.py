# question >>> https://www.hackerrank.com/challenges/one-week-preparation-kit-mini-max-sum/problem
# solution >>>!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    sl =[]
    s = sum(arr)
    for i in arr:
        sl.append(s - i)
    print(min(sl), max(sl))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)