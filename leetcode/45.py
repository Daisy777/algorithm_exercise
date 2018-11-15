class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1. 
        # if len(nums) == 1:
        #     return 0
        
        # times = [float('inf')] * len(nums)

        # times[0] = 0
        # i = 0
        # while (times[len(nums)-1] == float('inf')):
        #     for j in range(i+1, min(nums[i]+i+1, len(nums))):
        #         times[j] = min(times[j], times[i]+1)
            
        #     i += 1
        
        # return times[len(nums)-1]

        # 2. 
        if len(nums) == 1:
            return 0

        lastBegin = 0
        lastEnd = 0
        farthest = 0
        times = 0

        while (farthest < len(nums)-1):
            for i in range(lastBegin, lastEnd+1):
                farthest = max(farthest, nums[i] + i)
            times += 1
            lastBegin = lastEnd
            lastEnd = farthest
        
        return times



# test
if __name__ == '__main__':
    print(Solution().jump([2, 3, 1, 1, 4])) # 2
    print(Solution().jump([1, 2, 3])) # 2