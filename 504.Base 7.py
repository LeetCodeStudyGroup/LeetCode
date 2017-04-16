class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return "0"
        result = ""
        is_nav = num < 0
        num = abs(num)
        while num > 0:
            result = str(num % 7) + result
            num /= 7
        return "-" + result if is_nav else result
