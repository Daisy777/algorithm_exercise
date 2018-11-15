'''
Author:    ZHAO Zinan
Created: 13-Nov-2018

39. Combination Sum
'''
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self._combinationSum(candidates, 0, len(candidates)-1, target)
        
    def _combinationSum(self, candidates, begin, end, target):
        if not target:
            return [[]]
        if end < begin:
            return False
        
        result = []
        for i in range(target//candidates[end]+1):
            subresult = self._combinationSum(candidates, begin, end-1, target-candidates[end]*i)
            if subresult != False:
                result.extend([sub + [candidates[end]]*i for sub in subresult]) 
                    
        return result

# test
if __name__ == '__main__':
    print(Solution().combinationSum([2, 3, 6, 7], 7))
    # print(Solution().combinationSum([2, 3], 7))
