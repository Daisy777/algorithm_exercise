n'''
Author:    ZHAO Zinan
Created: 12/16/2018

198. House Robber
'''
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        result = [0]*length
        if not length:
            return 0
        
        if length == 1:
            return nums[0]
        
        result[0] = nums[0]
        result[1] = max(nums[0], nums[1])
        for i in range(2, length):
            result[i] = max(result[i-1], result[i-2]+nums[i])
            
        return result[length-1]
        