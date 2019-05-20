'''
Author:    ZHAO Zinan
Created: 20-May-2019

332. Reconstruct Itinerary
'''
import collections 
from typing import List 
# graph 
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list) 
        for a, b in sorted(tickets)[::-1]:
            graph[a].append(b)
        print(graph)
        route = []
        def visit(place):
            while graph[place]:
                nextplace = graph[place].pop()
                visit(nextplace)
                route.append(nextplace) 
        visit('JFK')
        route.append('JFK')
        return route[::-1]
        # targets = collections.defaultdict(list)
        # for a, b in sorted(tickets)[::-1]:
        #     targets[a] += b,
        # route = []
        # def visit(airport):
        #     while targets[airport]:
        #         visit(targets[airport].pop())
        #     route.append(airport)
        # visit('JFK')
        # return route[::-1]

if __name__ == '__main__':
    # print(Solution().findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
    # print(Solution().findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
    print(Solution().findItinerary([["JFK","NRT"],["JFK","KUL"],["KUL","JFK"]])) 