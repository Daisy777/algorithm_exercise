class Solution:
    def maxUncrossedLines(self, A, B):
        if not A or not B:
            return 0 
        # check A one by one
        setb = set(B)
        ptrb = 0
        ptra = 0
        pairsa = 0
        while(ptra < len(A)):
            if A[ptra] in setb:
                while(B[ptrb]) != A[ptra]:
                    ptrb += 1
                print(ptra, ptrb)
                ptrb += 1
                pairsa += 1
                setb = set(B[ptrb:])
            ptra += 1 

        # check B one by one
        seta = set(A)
        ptrb = 0
        ptra = 0
        pairsb = 0
        while(ptrb < len(B)):
            if B[ptrb] in seta:
                while(A[ptra]) != B[ptrb]:
                    ptra += 1
                print(ptra, ptrb)
                ptra += 1
                pairsb += 1
                seta = set(A[ptra:])
            ptrb += 1 
        return max(pairsa, pairsb)
    
if __name__ == '__main__':
    print(Solution().maxUncrossedLines([1,1,3,5,3,3,5,5,1,1], [2,3,2,1,3,5,3,2,2,1]))
            