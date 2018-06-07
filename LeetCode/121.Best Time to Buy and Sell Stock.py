class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max = 0
        cur = 0
        i = 1
        while i < len(prices):
            cur += prices[i] - prices[i - 1]
            if cur > max:
                max = cur
            elif cur < 0:
                cur = 0
            i += 1
        return max
