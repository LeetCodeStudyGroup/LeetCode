class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        pre_buy, buy, pre_sell, sell = 0, -prices[0], 0, 0
        for price in prices:
            pre_buy = buy
            buy = max(pre_sell - price, pre_buy)
            pre_sell = sell
            sell = max(pre_buy + price, pre_sell)

        return sell

    def maxProfit2(self, prices):
        if len(prices) < 2:
            return 0

        profits, dpv, dpx = [], [0, 0, 0], [0, 0, 0]
        for i in range(1, len(prices)):
            profits.append(prices[i] - prices[i - 1])

        for i in range(len(profits)):
            dpv.append(max(dpv[i + 2] + profits[i], dpv[i] + profits[i], dpx[i + 1] + profits[i]))
            dpx.append(max(dpv[i + 2], dpx[i + 2]))

        return max(dpv[-1], dpx[-1])

