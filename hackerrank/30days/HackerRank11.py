#!/bin/python3

import math
import os
import random
import re
import sys

def getPattern(arr, begin):
    x, y = begin
    sumPattern = 0

    for i in range(y, y+3):
        sumPattern += arr[x][i]
        sumPattern += arr[x+2][i]

    sumPattern += arr[x+1][y+1]
    return sumPattern

if __name__ == '__main__':
    arr = []
    SIZE = 6

    # get the input
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # can be negative
    maxSum = -float('inf')
    for i in range(SIZE-2):
        for j in range(SIZE-2):
            maxSum = max(maxSum, getPattern(arr, (i, j)))
        
    print(maxSum)


    
'''
-1 -1 0 -9 -2 -2
-2 -1 -6 -8 -2 -5
-1 -1 -1 -2 -3 -4
-1 -9 -2 -4 -4 -5
-7 -3 -3 -2 -9 -9
-1 -3 -1 -2 -4 -5
'''