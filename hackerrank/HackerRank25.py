'''
Author:    ZHAO Zinan
Created: 18-Oct-2018

prime number
O(n^(1/2))
'''
import math

def prime(a):
    # special case
    if a==2:
        return True
    if a==1:
        return False
        
    for i in range(2, int(math.sqrt(a))+1):
        if not a%i:
            return False

    return True

if __name__=='__main__':
    # read input 
    n = int(input().rstrip())
    for i in range(n):
        primeDecision = int(input().rstrip())
        if prime(primeDecision):
            print("Prime")
        else:
            print("Not prime")
