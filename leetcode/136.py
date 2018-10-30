'''
Author:    ZHAO Zinan
Created: 30-Oct-2018

136. Single Number
https://leetcode.com/problems/single-number/description/
'''

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums):
            result = nums[0] 
            for i in range(1, len(nums)):
                result = result ^ nums[i]

        return result

# test
if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNumber([2, 1, 2]))
    print(solution.singleNumber([1, 2, 1, 2, 3]))
    