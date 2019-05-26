'''
Author:    ZHAO Zinan
Created: 26-May-2019

1051. Height Checker
'''
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        right = sorted(heights)
        return sum([right[i] != heights[i] for i in range(len(right))])