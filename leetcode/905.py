class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        p1 = 0
        p2 = len(A)-1
        
        while(p1<p2):
            if A[p1]&1:
                A[p1], A[p2] = A[p2], A[p1]
                p2 -= 1
            else:
                p1 += 1
        return A
                