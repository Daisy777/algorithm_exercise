'''
Author:    ZHAO Zinan
Created: 01/18/2019

https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    numvally = 0
    invally = False
    height = 0

    for char in s:
        if char == 'D':
            height -= 1
        else:
            height += 1

        if height < 0 and not invally:
            invally = True
        elif height >= 0 and invally:
            invally = False
            numvally += 1
    return numvally

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
