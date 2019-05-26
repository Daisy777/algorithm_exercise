'''
Author:    ZHAO Zinan
Created: 26-May-2019

977. Squares of a Sorted Array
'''
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if not A:
            return A
        
        if A[0] >= 0:
            return [a**2 for a in A]
        if A[0] < 0 and A[-1] < 0:
            return [a**2 for a in A[::-1]]
        
        # instead of finding the center and expand, we can begin with the two ends
        result, ptr = [0]*len(A), len(A)-1
        
        left, right = 0, len(A) -1 
        while(left <= right):
            if abs(A[left]) < abs(A[right]):
                result[ptr] = A[right]**2
                right -= 1
            else:
                result[ptr] = A[left]**2 
                left += 1
            ptr -= 1
        return result
        