'''
Author:    ZHAO Zinan
Created: 06-Nov-2018

75. Sort Colors
https://leetcode.com/problems/sort-colors/description/
'''
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero = 0
        two = 0
        for index, value in enumerate(nums):
            if not value:
                nums[zero] = 0
                zero += 1
            elif value == 2:
                two += 1
        
        for i in range(zero, len(nums)-two):
            nums[i] = 1
            
        while two:
            nums[len(nums)-two] = 2
            two -= 1
            
        
            
            