'''
Author: ZHAO Zinan
Created: 09. March 2019

256. Paint House
''' 
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs or not costs[0]:
            return 0
        
        numhouse = len(costs)
        
        mincost = costs[0]
        for i in range(numhouse-1):
            mincost[0], mincost[1], mincost[2] = costs[i+1][0]+min(mincost[1], mincost[2]), costs[i+1][1]+min(mincost[0], mincost[2]), costs[i+1][2]+min(mincost[0], mincost[1])
            
        return min(mincost)