'''
Author: ZHAO Zinan
Created: 21. March 2019

955. delete colomns to make sorted 2
''' 
class Solution:
    def minDeletionSize(self, A) -> int:
        if not A or not A[0]:
            return 0
        numstring = len(A)
        numchar = len(A[0])
        result = 0
        finish = False
        i=0
        while (i < numchar):
            finish = True
            j=0
            while (j< numstring-1):
                if A[j][i] > A[j+1][i]:
                    result += 1
                    finish = False
                    break
                if A[j][i] == A[j+1][i]:
                    finish = False
                j += 1
            i+= 1
            if finish:
                break

        return result

# test 
if __name__ == '__main__':
    print(Solution().minDeletionSize(["ca","bb","ac"])) # 1
    print(Solution().minDeletionSize(["xc","yb","za"])) # 0
    print(Solution().minDeletionSize(["zyx","wvu","tsr"])) # 3
    print(Solution().minDeletionSize(["xga","xfb","yfa"]))  # 1
        
