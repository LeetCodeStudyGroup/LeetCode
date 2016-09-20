class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_result, start, end = self.sub_max_profit(prices, 0, len(prices))
        min_result = self.sub_min_profit(prices, start, end + 1)
        
        max1, start1, end1 = self.sub_max_profit(prices, 0, start)
        max2, start2, end2 = self.sub_max_profit(prices, end + 1, len(prices))
        
        min_result = self.sub_min_profit(prices, start, end + 1)

        return max(max_result - min_result, max_result + max(max1, max2))

    def sub_min_profit(self, prices, start, end):
        min = 0
        cur = 0
        i = start + 1
        while i < end:
            cur += prices[i] - prices[i - 1]
            if cur < min:
                min = cur
            elif cur > 0:
                cur = 0
            i += 1
        return min
        
    def sub_max_profit(self, prices, start, end):
        max_result = 0
        max_start = 0
        max_end = 0
        cur = 0
        cur_start = 0
        i = start + 1
        while i < end:
            cur += prices[i] - prices[i - 1]
            if cur > max_result:
                max_result = cur
                max_start = cur_start
                max_end = i
            elif cur < 0:
                cur_start = i
                cur = 0
            i += 1
        return max_result, max_start, max_end
