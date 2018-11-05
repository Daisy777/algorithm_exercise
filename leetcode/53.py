# class Solution:
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         maxSumi = nums[0] 
#         maxSum = maxSumi
#         for i in range(1, len(nums)):
#             maxSumi = max(nums[i], nums[i]+maxSumi)
#             maxSum = max(maxSum, maxSumi)
            
#         return maxSum

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        running_sum = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            if running_sum < 0:
                running_sum = 0
            running_sum += nums[i]
            if running_sum > res:
                res = running_sum
       
        return res
        

# test
if __name__ == '__main__':
    print(Solution().maxSubArray([-1, -2, -3]))