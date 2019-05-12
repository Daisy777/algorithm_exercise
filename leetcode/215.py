'''
Author:    ZHAO Zinan
Created: 12-May-2019

215. Kth Largest Element in an Array
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]