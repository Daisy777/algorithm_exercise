'''
Author:    ZHAO Zinan
Created: 22-Nov-2018

207. Course Schedule
https://leetcode.com/problems/course-schedule/description/
'''
class Graph:
    def __init__(self, int):
        from collections import defaultdict
        self.edges = defaultdict(list)
        # number of vertices (0 ~ n-1)
        self.vertices = int

    def addEdge(self, link):
        self.edges[link[0]].append(link[1])

    def Cyclic(self):
        visited = [0]*self.vertices
        inStack = [0]*self.vertices

        for i in range(self.vertices):
            if not visited[i]:
                if self._Cyclic(visited, inStack, i):
                    return True
        
        return False

    def _Cyclic(self, visited, inStack, v):
        if visited[v] and not inStack[v]:
            return False

        visited[v] = 1
        inStack[v] = 1

        # use depth first search to check whether this part is cyclic
        children = self.edges[v]
        result = False

        for child in children:
            if not inStack[child]:
                result = result or self._Cyclic(visited, inStack, child) 
            else:
                inStack[v] = 0
                return True
            if result:
                break

        inStack[v] = 0
        return result

class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        courseGraph = Graph(numCourses)
        for prerequesite in prerequisites:
            courseGraph.addEdge(prerequesite)

        return not courseGraph.Cyclic()

# test 
if __name__ == '__main__':
    print(Solution().canFinish(2, [[0, 1], [1, 0]])) # false
    print(Solution().canFinish(2, [[0, 1]])) # true
    print(Solution().canFinish(2, [[1, 0]])) # true
        