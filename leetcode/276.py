'''
Author: ZHAO Zinan
Created: 09. March 2019

276. Paint Fence
''' 
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0 or (n>2 and k == 1):
            return 0
        if n == 1:
            return k
        
        diff = k*(k-1)
        same = k
        
        for i in range(n-2):
            diff, same = (diff+same)*(k-1), diff
    
        return diff + same
    