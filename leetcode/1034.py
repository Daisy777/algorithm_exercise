
class Solution:
    def colorBorder(self, grid, r0, c0, color):
        def border(x, y, grid):
            row = len(grid)
            col = len(grid[0])
            if x == 0 or x == row-1or y == 0 or y == col-1:
                return True
            
            if grid[x][y] == grid[x][y-1] and grid[x][y] == grid[x][y+1] and grid[x][y] == grid[x-1][y] and grid[x][y] == grid[x+1][y]:
                return False 

            return True

        def findconnected(x, y, grid,  connected, visited=[]):
            row = len(grid)
            col = len(grid[0])

            if visited == []:
                visited = [[False for i in range(col)] for j in range(row)]
            visited[x][y] = True

            connected.add((x, y))
            if x > 0 and not visited[x-1][y] and grid[x-1][y] == grid[x][y]:
                findconnected(x-1, y, grid, connected, visited)
            if x < row-1 and not visited[x+1][y] and grid[x+1][y] == grid[x][y]:
                findconnected(x+1, y, grid, connected, visited)

            if y>0 and not visited[x][y-1] and grid[x][y-1] == grid[x][y]:
                findconnected(x, y-1, grid, connected, visited)
            if y <col-1 and not visited[x][y+1] and grid[x][y+1] == grid[x][y]:
                findconnected(x, y+1, grid, connected, visited)

            
        if not grid or not grid[0]:
            return grid 
        connected = set()
        findconnected(r0, c0, grid, connected, [])
        borderconnected = [ele for ele in connected if border(ele[0], ele[1], grid)]
        
        for x, y in borderconnected:
            grid[x][y] = color 
        return grid



if __name__ == '__main__':
    grid = [[2,1,2,2],[2,2,1,2],[1,1,2,1]]

    print(Solution().colorBorder(grid, 2, 2, 2))


