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
        odd_negative = False
        
        

# test
if __name__ == '__main__':
    print(Solution().maxProduct([-2, 0, -1]))    # 0
    pritn(Solution().maxProduct([2, 1, -1, 3]))  # 3
    pritn(Solution().maxProduct([2, 2, -1, 3]))  # 4
    print(Solution().maxProduct([2, 1, -1, -3])) # 6