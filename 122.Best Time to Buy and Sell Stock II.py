class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        i = 1
        while i < len(prices):
            diff = prices[i] - prices[i - 1]
            if diff > 0:
                profit += diff
            i += 1
        return profit
