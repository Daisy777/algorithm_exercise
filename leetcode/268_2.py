'''
Author:    ZHAO Zinan
Created: 04-Nov-2018

268. Missing Number
'''
class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n*(n+1)//2 - sum(nums)