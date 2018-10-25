'''
Author:    ZHAO Zinan
Created: 25-Oct-2018

best time to buy and sell stock with cooldown
'''
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if (len(prices)==1 or len(prices)==0):
            return 0;

        buy = [-prices[0], max(-prices[0], -prices[1])]
        sell = [0, max(0, prices[1]-prices[0])]

        for i in range(2, len(prices)):
            buy[0] = buy[1] 
            buy[1] = max(sell[0]-prices[i], buy[0])

            sell[0] = sell[1]
            sell[1] = max(buy[0]+prices[i], sell[0])

        return sell[1]

# test
if __name__ == '__main__':
    solution = Solution()
    # print(solution.maxProfit([1, 2, 3, 0, 2]))
    print(solution.maxProfit([1, 2]))

