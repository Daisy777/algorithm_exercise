'''
Author: ZHAO Zinan
Created: 23. February 2019

760. Find Anagram Mappings
''' 
class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        import collections
        mapBloc = collections.defaultdict(int)
        
        for index, ele in enumerate(B):
            mapBloc[ele] = index
        
        result = [0]*len(A)
        for index, ele in enumerate(A):
            result[index] = mapBloc[ele]
        return result
        