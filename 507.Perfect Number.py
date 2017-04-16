class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1: return False
        val, cnt = 1, 0
        while val < num:
            cnt += 1
            val *= 2
        cnt -= 1
        result = pow(2, cnt / 2) * (pow(2, cnt / 2 + 1) - 1)
        return result == num
