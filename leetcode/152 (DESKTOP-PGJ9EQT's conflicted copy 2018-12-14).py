'''
Author:    ZHAO Zinan
Created: 05-Nov-2018

152. Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray/description/
'''
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        smallest_negative = [0] * len(nums)
        largest_positive = [0] * len(nums)

        if nums[0] > 0:
            largest_positive[0] = nums[0]
        elif nums[0] < 0:
            smallest_negative[0] = nums[0]


        for i, num in enumerate(nums[1:]):
            index = i+1
            if num > 0:
                largest_positive[index] = max(num, largest_positive[index-1]*num)
                smallest_negative[index] = smallest_negative[index-1]*num
            elif num < 0:
                largest_positive[index] = smallest_negative[index-1]*num
                smallest_negative[index] = min(num, largest_positive[index-1]*num)
                
        return max(largest_positive)

# test
if __name__ == '__main__':
    print(Solution().maxProduct([-2, 0, -1]))    # 0
    print(Solution().maxProduct([2, 1, -1, 3]))  # 3
    print(Solution().maxProduct([2, 2, -1, 3]))  # 4
    print(Solution().maxProduct([2, 1, -1, -3])) # 6