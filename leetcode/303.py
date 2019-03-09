'''
Author: ZHAO Zinan
Created: 09. March 2019

303. Range Sum Query - Immutable
''' 
class NumArray:

    def __init__(self, nums: List[int]):
        if len(nums) == 0:
            self.sums = []
            return
        self.sums = [0 for i in range(len(nums))]
        self.sums[0] = nums[0]
        for i in range(1, len(nums)):
            self.sums[i] = self.sums[i-1]+nums[i]

    def sumRange(self, i: int, j: int) -> int:
        if not self.sums:
            return 0
        if i == 0:
            return self.sums[j]
        else:
            return self.sums[j] - self.sums[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)