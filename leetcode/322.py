'''
Author: ZHAO Zinan
Created: 06. May 2019

322. Coin Change

You are given coins of different denominations and a total amount of money
amount. Write a function to compute the fewest number of coins that you need to
make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Note:
You may assume that you have an infinite number of each kind of coins.
'''
from typing import List
# dp
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        if not coins:
            return -1

        dp = [-1 for i in range(amount+1)]
        dp[0] = 0
        for i in range(1, amount+1):
            if i in coins:
                dp[i] = 1
            else:
                choice = [dp[i-coin]+1 for coin in coins if i >= coin and dp[i-coin] != -1]
                dp[i] = min(choice) if choice else -1
        return dp[-1]

if __name__ == '__main__':
    print(Solution().coinChange([1, 2, 5], 11))
    print(Solution().coinChange([2], 3))