# Question >>> https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/problem
#Solution >>> !/bin/python3

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
    if "AM" in s:
        s = s.removesuffix("AM")
        hh, mm, ss = s.split(":")
        if hh == "12":
            hh = "00"
        l1 = [hh, mm, ss]
        s = ":".join(l1)
    elif "PM" in s:
        s = s.removesuffix("PM")
        hh, mm, ss = s.split(":")
        hh = int(hh)
        if not hh == 12:
            hh += 12
        l1 = [str(hh), mm, ss]
        s = ":".join(l1)
    return s
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()