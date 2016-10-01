class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        root = (x + 1) / 2
        while root * root > x:
            root /= 2
        root *= 2
        while root * root > x:
            root -= 1
        return root
