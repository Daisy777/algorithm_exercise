'''
Author:    ZHAO Zinan
Created: 12/05/2018

746. Min Cost Climbing Stairs
'''
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) == 0 or len(cost) == 1:
            return 0

        # init cost of first and second step
        # to save space, use two variables instead of an array
        first_cost = cost[0]
        second_cost = cost[1]

        i = 2
        while(i < len(cost)):
            min_cost = min(first_cost, second_cost)
            first_cost = second_cost
            second_cost = min_cost + cost[i]
            i+=1

        return min(first_cost, second_cost)
# test
if __name__ == '__main__':
    print(Solution().minCostClimbingStairs([10, 15, 20]))     # 15  
    print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])) # 6
    print(Solution().minCostClimbingStairs([0, 0, 0, 0])) # 0