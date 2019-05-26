'''
Author:    ZHAO Zinan
Created: 26-May-2019

922. Sort Array By Parity II
'''
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        if len(A) == 0 or len(A) == 1:
            return A 
        
        even, odd = 0, 1
        while(True):
            while(even < len(A) and A[even]%2 == 0):
                even += 2
            while(odd < len(A) and A[odd]%2 == 1):
                odd += 2
            if even < len(A) and odd < len(A):
                A[even], A[odd] = A[odd], A[even] 
            else:
                break
        return A