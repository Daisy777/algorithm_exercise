'''
Author:    ZHAO Zinan
Created: 26-Oct-2018

best time to buy and sell stock 2
'''
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if (len(prices) == 1 or len(prices) == 0):
            return 0

        buy = -prices[0] 
        sell = 0

        for i in range(1, len(prices)):
            previous_buy = buy
            buy = max(buy, sell-prices[i])
            sell = max(previous_buy+prices[i], sell)

        return sell

# test
if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([7, 1, 5, 3, 6, 4])) # 7
    print(solution.maxProfit([1, 2, 3, 4, 5]))    # 4
    print(solution.maxProfit([7, 6, 4, 3, 1]))    # 0