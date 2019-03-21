'''
Author: ZHAO Zinan
Created: 21. March 2019

982. Triples with Bitwise AND Equal To Zero
''' 
class Solution:
    def countTriplets(self, A: List[int]) -> int:
        counter = collections.Counter([x&y for x in A for y in A])
        return sum([counter[k] for i in A for k in counter if i&k ==0])