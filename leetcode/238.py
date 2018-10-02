class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        length = len(nums)
        p = 1

        # -> 
        for i in range(length):
            res.append(p)
            p *= nums[i]

        # <-
        p = 1
        for i in range(length-1, -1, -1):
            res[i] *= p
            p *= nums[i]

        return res

# for testing
if __name__ == '__main__':
    print(Solution().productExceptSelf([1,2,3,4]))