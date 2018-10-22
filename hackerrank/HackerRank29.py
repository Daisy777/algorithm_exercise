'''
Author:    ZHAO Zinan
Created: 22-Oct-2018

bitwise and
'''
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    # brute-force
    # t = int(input().strip())

    # for t_itr in range(t):
    #     n, k = map(int, input().strip().split())

    #     max_k = 0
    #     for i in range(1, n+1):
    #         for j in range(i+1, n+1):
    #             if i&j < k and i&j > max_k:
    #                 max_k = i&j

    #     print(max_k)

    t = int(input().strip())

    for t_itr in range(t):
        # k|(k-1) turns the most left 0 in (k-1) to 1
        n, k = map(int, input().strip().split())

        print(k-1 if k|(k-1) <= n else k-2)
