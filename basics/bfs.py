# Different representation of graph determines different methods to check the
# program
# For instance:
# graph = {1:[2, 3], 2:[4], 3:[4]} (directional)
# have to make sure that graph[node], node is in graph

# or graph is represented in bst form
# have to make sure the node in graph[nextnode] is not none

def bfs(graph, begin):
    if not graph:
        return

    visited = set([begin])
    queue = [begin]
    path = []

    while(queue):
        nextnode = queue.pop(0)
        if nextnode in graph:
            for node in graph[nextnode]:
                if node not in visited:
                    visited.add(node)
                    queue.append(node)
                    path.append((nextnode, node))
    return path

# test 
if __name__ == '__main__':
    '''
        1
      /   \
    2       3
      \   /
        4
    '''
    graph = {1:[2, 3], 2:[4], 3:[4]}
    print(bfs(graph, 1))
