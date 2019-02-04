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
        s = sum(nums)
        # find partition that sum(partition) == (target+sum)//2

        def partitionSum(self, nums, sum):
            # how to use dp to count times???
            dp = [0 for i in range(sum+1)]
            dp[0] = 1 # why ?????
            for n in nums:
                for i in 


# test
if __name__ == '__main__':
    print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3)) # 5
    print(Solution().findTargetSumWays([0, 0, 0, 0, 0, 0, 0, 0, 1], 1)) # 256
    print(Solution().findTargetSumWays([0], 0))
    print(Solution().findTargetSumWays([1, 2, 3, 4], 6))
    print(Solution().findTargetSumWays([29,6,7,36,30,28,35,48,20,44,40,2,31,25,6,41,33,4,35,38], 35))