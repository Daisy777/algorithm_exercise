'''
Author: ZHAO Zinan
Created: 10. March 2019

1007. Minimum Domino Rotations For Equal Row
''' 
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        from collections import defaultdict
        result1 = defaultdict(int)
        Arot = defaultdict(int)
        Brot = defaultdict(int)
        
        for i in range(len(A)):
            if A[i] != B[i]:
                result1[A[i]] += 1
                result1[B[i]] += 1
                Arot[A[i]] += 1
                Brot[B[i]] += 1
                
            else:
                result1[A[i]] += 1
                
        keynum = []
        for key in result1:
            if result1[key] == len(A):
                keynum.append(key)
        if not keynum:
            return -1
        
        minrotation = float('inf')
        for num in keynum:
            minrotation = min(minrotation, Brot[num], Arot[num])
        return minrotation
                
            
                       