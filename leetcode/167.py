'''
Author:    ZHAO Zinan
Created: 12/01/2018

167. Two Sum II - Input array is sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
'''
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers)-1

        while i < j:
            sumtwo = numbers[i] + numbers[j]
            if sumtwo == target:
                return [i+1, j+1]
            elif sumtwo < target:
                i += 1
            else:
                j -= 1
            
        