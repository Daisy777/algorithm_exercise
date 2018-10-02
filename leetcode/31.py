class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return

        if nums == list(reversed(sorted(nums))):
            nums.sort()
        else:
            self._nextPermutation(nums, 0)

    def _nextPermutation(self, nums, pos):
        if pos == len(nums)-1:
            return

        if nums[pos + 1:] != list(reversed(sorted(nums[pos + 1:]))):
            self._nextPermutation(nums, pos+1)

        # all the elements are the same
        elif len(set(nums[pos:])) <= 1 and len(nums[pos:]) > 1:
            return 

        else:
            # pos of smallest num greater than nums[loc]
            def nextLarger(nums, loc):
                nextLoc = nums[loc+1:].index(min([x for x in nums[loc+1:] if x > nums[loc]])) + loc + 1
                return nextLoc

            nextLoc = nextLarger(nums, pos)
            # swap the pos and smallest greater
            nums[pos], nums[nextLoc] = nums[nextLoc], nums[pos]

            # sort the next session and extend 
            nums[pos+1:] = sorted(nums[pos+1:])


if __name__ == '__main__':
    # nums = [1,3,2]
    # Solution().nextPermutation(nums)
    # print(nums)

    # nums = [2,1,3]
    # Solution().nextPermutation(nums)
    # print(nums)

    nums = [5,4,7,5,3,2]
    Solution().nextPermutation(nums)
    print(nums)