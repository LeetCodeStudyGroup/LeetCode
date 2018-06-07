class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        mask = 0
        val = n - m
        while val > 0:
            mask <<= 1
            mask += 1
            val >>= 1
        return m & n & (~mask)
