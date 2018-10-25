/*
Author:    ZHAO Zinan
Created: 24-Oct-2018
*/
class Solution {
    public int maxProfit(int[] prices, int fee) {
        int days = prices.length;
        if (days <= 1) {
            return 0;
        }

        int sell[] = new int[days];
        int buy[] = new int[days];

        sell[0] = 0;
        buy[0] = -prices[0]-fee;
        for (int i=1; i<days; i++) {
            sell[i] = Math.max(sell[i-1], buy[i-1]+prices[i]);
            buy[i] = Math.max(buy[i-1], sell[i-1]-prices[i]-fee);
        }

        return sell[days-1];
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.maxProfit(new int[]{1, 3, 2, 8, 4, 9}, 2));
    }
}

