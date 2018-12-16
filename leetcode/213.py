'''
Author:    ZHAO Zinan
Created: 12/16/2018

213. House Robber II
'''
class Solution:
    def _rob(self, nums):
        length = len(nums)
        result = [0]*length
        if not length:
            return 0
        
        if length == 1:
            return nums[0]
        
        result[0] = nums[0]
        result[1] = max(nums[0], nums[1])
        for i in range(2, length):
            result[i] = max(result[i-1], result[i-2]+nums[i])
            
        return result[length-1]

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        result1ton_1 = self._rob(nums[:len(nums)-1])
        result2ton = self._rob(nums[1:])

        return max(result1ton_1, result2ton)


# test
if __name__ == '__main__':
    print(Solution().rob([1, 2, 3, 1])) # 4
    print(Solution().rob([2, 3, 2])) # 3
    print(Solution().rob([1,1,3,6,7,10,7,1,8,5,9,1,4,4,3])) # 41
    print(Solution().rob([1,1])) # 1
    print(Solution().rob([2,2,4,3,2,5])) # 10