class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # from collections import Counter
        # import heapq
        # cnt = Counter(nums)
        # top_k = heapq.nlargest(k, cnt.values())
        
        # result = []
        # for key in cnt.keys():
        #     if cnt[key] in top_k:
        #         result.append(key)
                
        # return result

        max_num = max(nums)
        min_num = min(nums)
        count = [0] * (max_num - min_num + 1)
        
        for n in nums:
            count[n - min_num] += 1
        
        m = {}
        for index, c in enumerate(count):
            if c in m:
                m[c].append(index + min_num)
            else:
                m[c] = [index + min_num]
        
        index = 0
        result = []
        for c in range(max(count), -1, -1):
            if index >= k:
                return result
            if c in m:
                result += m[c]
                index += len(m[c])
        
        