'''
Author: ZHAO Zinan
Created: 14. March 2019

361. Bomb Enemy
''' 
# dfs
class Solution:
    def maxKilledEnemies(self, grid) -> int:
        if not grid or not grid[0]:
            return 0

        numrow = len(grid)
        numcol = len(grid[0])
        # iterate by rows first
        for indexi, row in enumerate(grid):
            zeros = set()
            accu = 0
            for indexj, ele in enumerate(row):
                if ele == '0' or isinstance(ele, int):
                    zeros.add((indexi, indexj))
                    grid[indexi][indexj] = int(grid[indexi][indexj])
                elif ele == 'W':
                    while(zeros):
                        x, y = zeros.pop()
                        grid[x][y] += accu
                    accu = 0
                elif ele == 'E':
                    accu += 1
                    
            while(zeros):
                x, y = zeros.pop()
                grid[x][y] += accu

        # iterate by cols 
        for indexj, col in enumerate(list(map(list, zip(*grid)))):
            zeros = set()
            accu = 0
            for indexi, ele in enumerate(col):
                if ele=='0' or isinstance(ele, int):
                    zeros.add((indexi, indexj))
                    grid[indexi][indexj] = int(grid[indexi][indexj])
                elif ele == 'W':
                    while(zeros):
                        x, y = zeros.pop()
                        grid[x][y] += accu
                    accu = 0
                elif ele == 'E':
                    accu += 1

            while(zeros):
                x, y = zeros.pop()
                grid[x][y] += accu
        
        # print(grid)
        valid = [x for row in grid for x in row if isinstance(x, int)]
        if valid:
            return max(valid)
        return 0

# test
if __name__ == '__main__':
    # 3
    print(Solution().maxKilledEnemies([["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]))
    print(Solution().maxKilledEnemies([['E']]))