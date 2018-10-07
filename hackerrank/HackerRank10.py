#!/bin/python3

import math
import os
import random
import re
import sys

def consecutive1(n):
    # get binary form
    binNum = bin(n)[2:]

    # get consecutive 1s number
    cnt = 0
    maxcnt = 0 

    for x in binNum:
        if x == '0':
            maxcnt = max(maxcnt, cnt)
            cnt = 0
        else:
            cnt += 1
    # compare it last time
    maxcnt = max(maxcnt, cnt)

    return maxcnt

if __name__ == '__main__':
    n = int(input())
    print(consecutive1(n))

# 13 -> 2
# 439 -> 3
# 5 -> 1