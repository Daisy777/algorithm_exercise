'''
Author:    ZHAO Zinan
Created: 12/21/2018

289. Game of Life
'''
class Solution:
    def gameOfLife(self, data):
        """
        :type data: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(data) == 0 or len(data[0]) == 0:
            return
        
        row = len(data)
        col = len(data[0])

        def update(data, x, y):
            for i in range(max(0, x-1), min(len(data), x+1+1)):
                for j in range(max(0, y-1), min(len(data[0]), y+1+1)):
                    data[i][j] += 1
                
            data[x][y] -= 1

        neighbors = [[0 for i in range(col)] for i in range(row)]
        for i in range(row):
            for j in range(col):
                if data[i][j]:
                    update(neighbors, i, j)

        # print(neighbors)
        for i in range(row):
            for j in range(col):
                if neighbors[i][j] == 3:
                    data[i][j] = 1
                elif neighbors[i][j] < 2 or neighbors[i][j] > 3:
                    data[i][j] = 0
                
        # return data

# test
if __name__ == '__main__':
    data1 = [
    [0,1,0],
    [0,0,1],
    [1,1,1],
    [0,0,0]
    ]
    print(Solution().validUtf8(data1))

        