'''
Author: ZHAO Zinan
Created: 24. February 2019

807. Max Increase to Keep City Skyline
''' 
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        num_row = len(grid)
        num_col = len(grid[0])
        
        col_max = [0]*num_col
        row_max = [0]*num_row
        for i in range(num_row):
            row_max[i] = max(grid[i])
        
        col_grid = list(zip(*grid))
        for i in range(num_col):
            col_max[i] = max(col_grid[i])
        
        sum = 0
        for i in range(num_row):
            for j in range(num_col):
               sum += min(row_max[i], col_max[j]) - grid[i][j]
        return sum

'''
a more pythonic solution
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: 'List[List[int]]') -> 'int':
        l2r_skyline = list(map(max, grid))  
        u2d_skyline = list(map(max, *grid))
        return sum(min(i, j) for i in l2r_skyline for j in u2d_skyline) - sum(map(sum, grid))
'''