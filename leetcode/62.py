'''
Author:    ZHAO Zinan
Created: 12/13/2018

62. Unique Paths
'''
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if not m or not n:
            return 0
        if n == 1:
            return 1
        if m == 1:
            return 1
        
        arr = [[1]*n]*m
        
        for i in range(1, m):
            for j in range(1, n):
                arr[i][j] = arr[i-1][j] + arr[i][j-1]
                
        return arr[m-1][n-1]

# test
if __name__ == '__main__':
    print(Solution().uniquePaths(3, 2)) # 3
    print(Solution().uniquePaths(7, 3)) # 28
        