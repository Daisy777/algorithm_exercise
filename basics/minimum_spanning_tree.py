
def prim(graph):
    # adjacency list representation for graph as we need to iterate all the
    # neigh nodes
    import heapq
    import random
    mst = []

    heap = []
    heapq.heapify(heap)
    notvisited = set(graph.keys())
    start = random.sample(graph.keys(), 1)[0]

    notvisited.remove(start)
    for neighborstart in graph[start]:
        heapq.heappush(heap, (graph[start][neighborstart], (start, neighborstart)))

    while notvisited:
        min_weight, (node1, node2) = heapq.heappop(heap)
        if node2 not in notvisited:
            continue
        mst.append((node1, node2))
        notvisited.remove(node2)
        for node in graph[node2]:
            if node in notvisited:
                heapq.heappush(heap, (graph[node2][node], (node2, node)))
    return mst


def kruskal(graph):
    import heapq
    # always get the edge with minimum weight
    mst = []
    class UnionFind:
        def __init__(self, length):
            self.arr = [i for i in range(length)]
        def find(self, node):
            if self.arr[node] != node:
                return self.find(self.arr[node])
            return node
        def connected(self, i, j):
            return self.find(i) == self.find(j)
        def union(self, i, j):
            if self.connected(i, j):
                return
            rooti = self.find(i)
            rootj = self.find(j)
            self.arr[rooti] = rootj

    heap_edge = []
    heapq.heapify(heap_edge)
    for node in graph:
        for neighbor in graph[node]:
            heapq.heappush(heap_edge, (graph[node][neighbor], (node, neighbor)))
    
    nodes = set([node for node in graph])
    unionfind = UnionFind(len(nodes))
    while(nodes):
        weight, (node1, node2) = heapq.heappop(heap_edge)
        if not unionfind.connected(node1, node2):
            mst.append((node1, node2))
            unionfind.union(node1, node2)
            if node1 in nodes:
                nodes.remove(node1)
            if node2 in nodes:
                nodes.remove(node2)

    return mst

# test
if __name__ == '__main__':
    graph = {
        0: {1: 2, 2:3}, 
        1: {0:2, 2:5, 3: 3, 4:4},
        2: {0: 3, 1:5, 3: 2},
        3: {1: 3, 2: 2, 4:2, 5: 3},
        4: {1: 4, 3: 2, 5: 5},
        5: {4: 5, 3:3, 4:5}
    }
    print(prim(graph))
    print(kruskal(graph))
        
