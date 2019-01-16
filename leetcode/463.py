'''Author:    ZHAO Zinan
Created: 01/16/2019

463. Island Perimeter
'''
class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0

        for x, row in enumerate(grid):
            for y, ele in enumerate(row):
                if ele:
                    add = 4
                    add -= (int(x!=0 and grid[x-1][y]) + (x!=len(grid)-1 and grid[x+1][y]) + (y!=0 and row[y-1]) + (y!=len(row)-1 and row[y+1]))
                    perimeter += add
        return perimeter

# test
if __name__ == '__main__':
    test0 = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

    print(Solution().islandPerimeter(test0)) # 16
