/**
     * 309. Best Time to Buy and Sell Stock with Cooldown
     * Medium
     * 6.9K
     * 236
     * Companies
     * You are given an array prices where prices[i] is the price of a given stock on the ith day.
     *
     * Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
     *
     * After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
     * Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
     *
     *
     *
     * Example 1:
     *
     * Input: prices = [1,2,3,0,2]
     * Output: 3
     * Explanation: transactions = [buy, sell, cooldown, buy, sell]
     * Example 2:
     *
     * Input: prices = [1]
     * Output: 0
     *
     *
     * Constraints:
     *
     * 1 <= prices.length <= 5000
     * 0 <= prices[i] <= 1000
     */

    public int maxProfit(int[] prices) {
        if(prices == null || prices.length <= 1) return 0;

        int[] buy = new int[prices.length];
        int[] sell = new int[prices.length];
        buy[0] = -prices[0];
        buy[1] = -Math.min(prices[0], prices[1]);
        sell[1] = Math.max(0, buy[0] + prices[1]);

        for(int i = 2; i < prices.length; i++) {
            buy[i] = Math.max(buy[i - 1], sell[i - 2] - prices[i]);
            sell[i] = Math.max(sell[i - 1], buy[i - 1] + prices[i]);
        }

        return sell[prices.length - 1];
    }
