'''
Author:    ZHAO Zinan
Created: 08-Nov-2018

494. Target Sum
https://leetcode.com/problems/target-sum/description/
'''
# brute force 2^n
class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        return self._findTargetSumWays(nums, len(nums), S)
    
    def _findTargetSumWays(self, nums, length, S):
        if length == 1:
            return int(nums[0] == S) + int(nums[0] == -S)

        last = nums[length-1]
        first = self._findTargetSumWays(nums, length-1, S-last)
        second = self._findTargetSumWays(nums, length-1, S+last)
        return first + second
        

# test
if __name__ == '__main__':
    print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3)) # 5
    print(Solution().findTargetSumWays([0, 0, 0, 0, 0, 0, 0, 0, 1], 1)) # 256
    print(Solution().findTargetSumWays([0], 0))
    print(Solution().findTargetSumWays([1, 2, 3, 4], 6))