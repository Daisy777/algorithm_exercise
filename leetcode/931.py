'''
Author: ZHAO Zinan
Created: 18. March 2019

931. Minimum Falling Path Sum
''' 
class Solution:
    def minFallingPathSum(self, A) -> int:
        if not A or not A[0]:
            return 0
        numrow = len(A)
        numcol = len(A[0])
        
        minimum = A[0].copy()
        for i in range(1, numrow):
            minimum = [min(minimum[index], minimum[max(0, index-1)], minimum[min(numcol-1, index+1)])+A[i][index] for index, ele in enumerate(minimum)]
        return min(minimum)

# test
if __name__ == '__main__':
    print(Solution().minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]])) # 12
    print(Solution().minFallingPathSum([[-19,57],[-40,-5]])) # -59