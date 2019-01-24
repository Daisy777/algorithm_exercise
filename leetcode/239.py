'''
Author:    ZHAO Zinan
Created: 01/24/2019

239. Sliding Window Maximum
'''
class MonotoneQueue:
        def __init__(self):
            import queue
            self.queue = queue.Queue()
            self.helper = []

        def push(self, ele):
            while self.helper and ele > self.helper[-1]:
                self.helper.pop()
            self.helper.append(ele)
            self.queue.put(ele)

        def pop(self):
            if self.helper[0] == self.queue.get():
                self.helper.pop(0)

        def max(self):
            return self.helper[0]

class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0 or len(nums) == 0:
            return []
        start, end = 1, k
        slidingwindow = MonotoneQueue()
        result = []
        for i in range(k):
            slidingwindow.push(nums[i])
        result.append(slidingwindow.max())

        while(end<len(nums)):
            slidingwindow.push(nums[end])
            slidingwindow.pop()
            result.append(slidingwindow.max())
            end += 1
            start += 1
        return result    
# test
if __name__ == '__main__':
    print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
    # [3,3,5,5,6,7]

    print(Solution().maxSlidingWindow([], 0))
    # 0