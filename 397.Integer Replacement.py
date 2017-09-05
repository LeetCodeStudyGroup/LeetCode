class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n > 1:
            cnt += 1
            if n & 1 == 0:
                n = n >> 1
            #elif n == 3 or bin(n + 1).count('1') > bin(n - 1).count('1'):
            elif n == 3 or (n >> 1) & 1 == 0:
                n -= 1
            else:
                n += 1
        return cnt
