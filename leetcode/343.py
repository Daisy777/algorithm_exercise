'''
Author:    ZHAO Zinan
Created: 12/06/2018

343. Integer Break
https://leetcode.com/problems/integer-break/description/
'''
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1

        arr = [0] * n
        arr[2] = 1
        for i in range(3,n+1):
            