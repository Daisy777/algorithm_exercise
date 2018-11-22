'''
Author:    ZHAO Zinan
Created: 21-Oct-2018

regular expressions
input: first line - number of input lines
       <first name> <email>
output: first name per line whose email is gmail
'''

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    result_name = []
    N = int(input())

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        result = re.match("^(.*)@gmail.com$", emailID)
        if result:
            result_name.append(firstName)


    for name in sorted(result_name):
        print(name)



