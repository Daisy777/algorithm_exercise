'''
Author:          ZHAO Zinan
Written:         2018-08-28
Last Updated:    2018-08-28


On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes.
Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).
Now we view the projection of these cubes onto the xy, yz, and zx planes.
A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane. 
Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.
Return the total area of all three projections.

Example 1:
    Input: [[2]]
    Output: 5

Example 2:
    Input: [[1,2],[3,4]]
    Output: 17
'''

class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # top
        top = sum(i!=0 for j in grid for i in j)

        # two side
        # sum up the max in each column/row
        side1 = sum(max(grid[i][j] for j in range(len(grid))) for i in range(len(grid)))
        side2 = sum(max(grid[i][j] for i in range(len(grid))) for j in range(len(grid)))

        return top + side1 + side2