class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        rst = 1
        for i in range(n):
            val = 9
            for j in range(min(9, i)):
                val *= (9 - j)
            rst += val
        return rst
