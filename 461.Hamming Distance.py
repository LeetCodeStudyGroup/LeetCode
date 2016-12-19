class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        cnt = 0
        while x != 0 or y != 0:
            if x & 1 != y & 1:
                cnt += 1
            x, y = x >> 1, y >> 1
        return cnt
