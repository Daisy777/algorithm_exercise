'''
Author:    ZHAO Zinan
Created: 01/09/2019

416. Partition Equal Subset Sum
https://leetcode.com/problems/partition-equal-subset-sum/description/
'''
class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # convert to a problem of 0-1 knapsack problem
        sumweight = sum(nums)
        if sumweight & 1:
            return False

        dp = [[0 for i in range(sumweight//2+1)] for j in range(len(nums)+1)]
        for indexi, row in enumerate(dp):
            for indexj, item in enumerate(row):
                if indexi == 0 or indexj == 0:
                    continue
                if nums[indexi-1] <= indexj:
                    dp[indexi][indexj] = max(dp[indexi-1][indexj], dp[indexi-1][indexj-nums[indexi-1]]+nums[indexi-1])
                else:
                    dp[indexi][indexj] = dp[indexi-1][indexj]
                
        if dp[len(nums)][sumweight//2] == sumweight/2:
            return True
        return False
# test
if __name__ == '__main__':
    print(Solution().canPartition([1, 5, 11, 5])) # ture
    print(Solution().canPartition([1, 2, 3, 5])) # false