# in directed acyclic graph
# begin with nodes whose in-degree is 0
# a special form of dfs?

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.edges = defaultdict(list)
        self.vertices = list(range(vertices))
    def addEdge(self, v, w):
        if v in self.vertices:
            self.edges[v].append(w)

    def _topologicalSort(self, v,visited, stack):
        visited[v] = True
        for neighbor in self.edges[v]:
            if not visited[neighbor]:
                self._topologicalSort(neighbor, visited, stack)
        stack.append(v)

    def topologicalSort(self):
        visited = [False]*len(self.vertices)
        stack = []
        
        for v in self.vertices:
            if not visited[v]:
                self._topologicalSort(v, visited, stack)
        return list(reversed(stack))

# test 
if __name__ == '__main__':
    g= Graph(6) 
    g.addEdge(5, 2); 
    g.addEdge(5, 0); 
    g.addEdge(4, 0); 
    g.addEdge(4, 1); 
    g.addEdge(2, 3); 
    g.addEdge(3, 1); 
    print(g.topologicalSort())