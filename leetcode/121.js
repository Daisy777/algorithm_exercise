/*
Author:    ZHAO Zinan
Created: 24-Oct-2018

Best Time to Buy and Sell Stock
at most one transaction
*/
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    if (prices.length == 1) {
        return 0;
    }
    
    var min = prices[0]; // the min element before 
    var max = 0;         // max profit can get
    
    for (var i=1; i<prices.length; i++) {
        max = Math.max(max, prices[i]-min);
        min = Math.min(min, prices[i]);
    }
    
    return max;
};