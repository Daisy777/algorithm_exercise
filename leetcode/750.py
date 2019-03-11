class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        # if not grid or not grid[0]:
        #     return 0
        
        # nrows = len(grid)
        # ncols = len(grid[0])

        # num = 0
        # for i in range(nrows):
        #     for j in range(i+1, nrows):
        #         col = 0
        #         for x in range(ncols):
        #             if grid[i][x] and grid[j][x]:
        #                 col += 1
        #         num += col*(col-1)//2
        # return num

        # performance improvemnet for sparse matrix
        # store locations of ones in ith line
        if not grid or not grid[0]:
            return 0

        nrows = len(grid)
        ncols = len(grid[0])

        num = 0
        for i in range(nrows):
            ones = set()
            for k in range(ncols):
                if grid[i][k]:
                    ones.add(k)

            for j in range(i+1, nrows):
                col = 0
                onescopy = ones.copy()
                while(onescopy):
                    loc = onescopy.pop()
                    if grid[j][loc]:
                       col += 1
                num += col*(col-1)/2
        return num 

# test
if __name__ == '__main__':
    testgrid = [
        [1, 0, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0],
        [1, 0, 1, 0, 1]
    ]

    print(Solution().countCornerRectangles(testgrid))