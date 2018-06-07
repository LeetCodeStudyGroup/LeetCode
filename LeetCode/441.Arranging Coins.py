class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 0, n
        while start != end:
            mid = (start + end) / 2
            val = (1 + mid) * mid / 2
            if val < n and (val + mid + 1) > n:
                return mid
            elif val < n:
                start = mid + 1
            else:
                end = mid
        return start
        #return self.find(n, 0, n)

    def find(self, n, start, end):
        if start == end:
            return start
        mid = (start + end) / 2
        val = (1 + mid) * mid / 2
        if val < n and (val + mid + 1) > n:
            return mid
        elif val < n:
            return self.find(n, mid + 1, end)
        else:
            return self.find(n, start, mid)
