class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 0:
            return ''
        result = ''
        array = range(n)
        d = 1
        for x in range(1, n):
            d *= x
        val = k - 1
        i = n - 1
        while i > 0:
            result += str(array.pop(val / d) + 1)
            val %= d
            d /= i
            i -= 1
        result += str(array.pop(0) + 1)
        return result
