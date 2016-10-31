class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        additional = 5
        while additional <= n:
            count += n / additional
            additional *= 5
        return count
