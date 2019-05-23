'''
Author:    ZHAO Zinan
Created: 23-May-2019

⭐974. Subarray Sums Divisible by K
'''
import collections 
from typing import List 

# use a table to record the remainder of each subarray
# subarray
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        if not A:
            return 0 

        mod_list = [1] + [0]*K 
        result, subsum = 0, 0
        for i in range(len(A)):
            subsum += A[i] 
            result += mod_list[subsum%K] 
            mod_list[subsum%K] += 1 
        return result
                
