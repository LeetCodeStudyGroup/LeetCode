class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        base = 0
        while n > 9 * (10 ** base) * (base + 1):
            n -= 9 * (10 ** base) * (base + 1)
            base += 1
        n -= 1
        r = n % (base + 1)
        n = 10 ** base + n / (base + 1)
        for i in range(r, base):
            n /= 10
        return n % 10
