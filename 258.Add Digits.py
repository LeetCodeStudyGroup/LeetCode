class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0: return 0
        ret = num % 9
        if ret == 0:
            ret = 9
        return ret
