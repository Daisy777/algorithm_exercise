class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        elements = set(nums)
        for ele in elements:
            if len([i for i in nums if i == ele]) > length//2:
                return ele