'''
Author:    ZHAO Zinan
Created: 19-Nov-2018

46. Permutations
https://leetcode.com/problems/permutations/description/
'''
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self._permute(nums, 0, len(nums)-1)
        
    def _permute(self, nums, begin, end):
        if begin == end:
            # should use copy of the list
            return [nums[:]]
        
        result = []
        for i in range(begin, end+1):
            # swap
            temp = nums[begin]
            nums[begin] = nums[i]
            nums[i] = temp
            
            result.extend(self._permute(nums, begin+1, end))

            temp = nums[begin]
            nums[begin] = nums[i]
            nums[i] = temp
            
        return result

# test
if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))
        