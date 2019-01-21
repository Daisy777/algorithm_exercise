'''
Author:    ZHAO Zinan
Created: 01/21/2019

228. Summary Ranges
'''

class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        
        p1 = 0
        p2 = 0
        result = []
        while(p2<len(nums)):
            while(p1<len(nums)-1 and nums[p1+1] == nums[p1]+1):
                p1+=1
            if p1 == p2:
                result.append(str(nums[p1]))
            else:
                result.append(''.join([str(nums[p2]), '->', str(nums[p1])]))
            p1 += 1
            p2 = p1

        return result

# test
if __name__ == '__main__':
    print(Solution().summaryRanges([0]))
    # ['0']
    print(Solution().summaryRanges([1, 2, 5]))
    # ['1->2', '5']

            