'''
Author:    ZHAO Zinan
Created: 21-May-2019

528. Random Pick with Weight
'''
import random 
from typing import List 
import itertools
import bisect

class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = list(itertools.accumulate(w))

    def pickIndex(self) -> int:
        rand = random.randint(0, self.prefix_sum[-1] - 1)
        return bisect.bisect_right(self.prefix_sum, rand)
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
if __name__ == '__main__':
    print(Solution([2, 3]).pickIndex())