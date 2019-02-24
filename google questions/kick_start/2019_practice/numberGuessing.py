def numberGuessing(lower, upper):
    if upper-lower == 1:
        return upper
    return (lower+upper)//2

import sys
numTestCase = int(input().strip())
for i in range(numTestCase):
    a, b = map(int, input().strip().split())
    print(numberGuessing(a+1, b))
    sys.stdout.flush()
    while(True):
        result = input()
        if result == 'WRONG_ANSWER' or result == 'CORRECT':
            break
        elif result == 'TOO_SMALL':
            a = (a+1+b)//2
            print(numberGuessing(a, b))
            sys.stdout.flush()
        elif result == 'TOO_BIG':
            b = (a+b)//2
            print(numberGuessing(a+1, b))
            sys.stdout.flush()
    