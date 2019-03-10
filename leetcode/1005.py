'''
Author: ZHAO Zinan
Created: 10. March 2019

1005. Maximize Sum Of Array After K Negations
''' 
class Solution:

    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        for index, a in enumerate(A):
            if a <= 0:
                if K > 0:
                    A[index] = -a
                    K -= 1
                if K == 0 or a == 0:
                    return sum(A)
            else:
                break
            
        A.sort(reverse = True)
        K = K%2
        while(K):
            A[-K] = -A[-K]
            K -= 1
        return sum(A)
        
        