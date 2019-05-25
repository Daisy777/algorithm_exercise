'''
Author:    ZHAO Zinan
Created: 25-May-2019

219. Contains Duplicate II
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        loc = collections.defaultdict(list)
        for index, ele in enumerate(nums):
            loc[ele].append(index) 
            if len(loc[ele]) > 1 and loc[ele][-1] - loc[ele][-2] <=k:
                return True 
        return False