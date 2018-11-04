'''
Author:    ZHAO Zinan
Created: 04-Nov-2018

268. Missing Number
https://leetcode.com/problems/missing-number/description/
'''

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        nums.sort()
        previous = nums[0]
        if previous != 0:
            return 0

        for i in range(1, len(nums)):
            if nums[i] - previous != 1:
                return previous + 1
            previous = nums[i]

        return previous+1

# test
if __name__ == '__main__':
    print(Solution().missingNumber([3, 0, 1])) # 2
    print(Solution().missingNumber([0]))  # 1
    print(Solution().missingNumber([1]))  # 0