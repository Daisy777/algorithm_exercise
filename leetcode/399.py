'''Author:    ZHAO Zinan
Created: 01/13/2019

399. Evaluate Division
'''
class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # graph
        variable_grpah = {}
        for index, equation in enumerate(equations):
            node_start = equation[0]
            node_end = equation[1]

            if node_start not in variable_grpah:
                variable_grpah[node_start] = [[node_end, values[index]]]
            else:
                variable_grpah[node_start].append([node_end, values[index]])

            if node_end not in variable_grpah:
                variable_grpah[node_end] = [[node_start, 1/values[index]]]
            else:
                variable_grpah[node_end].append([node_start, 1/values[index]])

        def _calcQuery(graph, start, end):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            
            nodes = list(graph.keys())
            nodes.remove(start)
            previous = graph[start]
            while(len(nodes) and len(previous)):
                next = []
                for i, edge in enumerate(previous):
                    if edge[0] == end:
                        return edge[1]
                    next.extend([[node, value*edge[1]] for node, value in graph[edge[0]] if node in nodes])
                    nodes.remove(edge[0])

                previous = next
            return -1.0
                
        result = []
        for query in queries:
            node1 = query[0]
            node2 = query[1]
            result.append(_calcQuery(variable_grpah, node1, node2))
        return result

# test
if __name__ == '__main__':
    equations1 = [['a', 'b'], ['b', 'c']]
    values1 = [2.0, 3.0]
    queries1 = [['a', 'c'], ['b', 'a'], ['a', 'e'], ['a', 'a'], ['x', 'x']]
    print(Solution().calcEquation(equations1, values1, queries1))
    # [6.0, 0.5, -1.0, 1.0, -1.0]

    equations2 = [['a', 'b'], ['c', 'd']]
    values2 = [1.0, 1.0]
    queries2 = [['a', 'c'], ['b', 'd']]
    print(Solution().calcEquation(equations2, values2, queries2))
    

            
                
            