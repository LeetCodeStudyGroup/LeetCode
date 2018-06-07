class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_nav = False
        if x < 0:
            is_nav = True
            x = 0 - x
        result = 0
        m = 0
        while x != 0:
            result *= 10
            m = x % 10
            x = x / 10
            result += m
        if is_nav:
            result = 0 - result
        if result > 2147483647 or result < -2147483648:
            return 0
        
        return result
