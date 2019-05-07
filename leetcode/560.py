'''
Author:    ZHAO Zinan
Created: 07-May-2019

560. Subarray Sum Equals K

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
'''
import collections 
from typing import List 

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = collections.defaultdict(int)
        count[0] = 1
        accu, result = 0, 0

        for num in nums:
            accu += num 
            result += count[accu-k] 
            count[accu] += 1 
        return result 
if __name__ == '__main__':
    print(Solution().subarraySum([1, 1, 1], 2))
            
