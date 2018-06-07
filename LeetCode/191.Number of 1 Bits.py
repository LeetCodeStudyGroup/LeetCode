class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n > 0:
            cnt += 1
            n &= (n - 1)
        return cnt

    def hammingWeight2(self, n):
        cnt = 0
        while n > 0:
            cnt += n & 1
            n >>= 1
        return cnt
