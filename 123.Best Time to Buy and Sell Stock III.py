class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_result, start, end = self.sub_max_profit(prices)
        
        max1, start1, end1 = self.sub_max_profit(prices[:start])
        max2, start2, end2 = self.sub_max_profit(prices[end + 1:])
        
        min_result = self.sub_min_profit(prices[start:end + 1])

        return max(max_result - min_result, max_result + max(max1, max2))

    def sub_min_profit(self, prices):
        min = 0
        cur = 0
        i = 1
        while i < len(prices):
            cur += prices[i] - prices[i - 1]
            if cur < min:
                min = cur
            elif cur > 0:
                cur = 0
            i += 1
        return min
        
    def sub_max_profit(self, prices):
        max = 0
        start = 0
        max_start = -1
        max_end = -1
        cur = 0
        i = 1
        while i < len(prices):
            cur += prices[i] - prices[i - 1]
            if cur > max:
                max = cur
                max_start = start
                max_end = i
            elif cur < 0:
                start = i
                cur = 0
            i += 1
        return max, max_start, max_end
