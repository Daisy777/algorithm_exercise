class Solution:
    def isEscapePossible(self, blocked, source,  target):
        if not blocked:
            return True 
        
        def findconnected(x, y, blocked, visited=[]):
            row = len(grid)
            col = len(grid[0])

            if visited == []:
                visited = [[False for i in range(col)] for j in range(row)]
            visited[x][y] = True

            if x > 0 and not visited[x-1][y] and (x-1, y) not in blocked:
                findconnected(x-1, y, blocked, visited)
            if x < row-1 and not visited[x+1][y] and (x+1, y) not in blocked:
                findconnected(x+1, y, blocked, visited)

            if y>0 and not visited[x][y-1] and (x, y-1) not in blocked:
                findconnected(x, y-1, blocked, visited)
            if y <col-1 and not visited[x][y+1] and (x, y+1) not in blocked:
                findconnected(x, y+1, blocked, visited)
            
        setblocked = set()
        for x, y in blocked:
            setblocked.add((x, y))
        squaresize = target[0]-source[0]+1
        visited = [[False for i in range(squaresize)] for j in range(squaresize)]
        findconnected(source[0], source[1], blocked, visited)
        if visited[target[0]][target[1]]:
            return True 
        return False