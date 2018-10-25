'''
Author:    ZHAO Zinan
Created: 24-Oct-2018

Best Time to Buy and Sell Stock with Transaction Fee
Dynamic Programming O(n^2)
! runtime limit exceeds 
'''
class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if len(prices) == 1:
            return 0
        if len(prices) == 2:
            return 0 if prices[1] - prices[0] <= fee else prices[1] - prices[0] - fee

        max_profits = [0]*len(prices)

        for i in range(1, len(prices)):
            # if add ith prices to the transaction
            max_include_profits = 0
            for j in range(i):
                profits = prices[i] - prices[j] - fee
                if j > 0:
                    profits += max_profits[j-1]
                max_include_profits = max(max_include_profits, profits)

            max_profits[i] = max(max_profits[i-1], max_include_profits)

        return max_profits[len(prices)-1]




# test
if __name__=='__main__':
    solution = Solution()
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    print(solution.maxProfit(prices, fee))


