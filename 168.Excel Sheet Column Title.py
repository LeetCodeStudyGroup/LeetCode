class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ''
        while n > 0:
            result = chr(ord('A') + (n - 1) % 26) + result
            n = (n - 1) / 26
        return result
