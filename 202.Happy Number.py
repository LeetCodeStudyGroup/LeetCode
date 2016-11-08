class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        record = []
        while n not in record:
            if n == 1:
                return True
            record.append(n)
            val = 0
            while n > 0:
                val += (n % 10) ** 2
                n /= 10
            n = val
        return False
