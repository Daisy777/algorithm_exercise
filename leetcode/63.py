'''Author:    ZHAO Zinan
Created: 12/13/2018

63. Unique Paths II
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        if not m:
            return 0
        n = len(obstacleGrid[0])
        
        arr = [[None for i in range(n)] for j in range(m)] # ! don't use * 
        arr[0][0] = 1 if not obstacleGrid[0][0] else 0

        # fill in the first col and row
        for i in range(1, m):
            if not obstacleGrid[i][0]:
                arr[i][0] = arr[i-1][0]
            else:
                arr[i][0] = 0
            
        for j in range(1, n):
            arr[0][j] = arr[0][j-1] if not obstacleGrid[0][j] else 0

            
        for i in range(1, m):
            for j in range(1, n):
                arr[i][j] = arr[i-1][j] + arr[i][j-1] if not obstacleGrid[i][j] else 0
            
        return arr[m-1][n-1]
        
# test
if __name__ == '__main__':
    obstacle1 = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
    ]
    print(Solution().uniquePathsWithObstacles(obstacle1)) # 2

    obstacle2 = [[1]]
    print(Solution().uniquePathsWithObstacles(obstacle2)) # 0

    obstacle3 = [
        [0, 0], 
        [1, 0]
    ]
    print(Solution().uniquePathsWithObstacles(obstacle3)) # 1
