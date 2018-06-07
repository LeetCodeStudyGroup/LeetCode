class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        is_nav = False
        i = ret = 0

        while i < len(str) and ord(str[i]) != ord('-') and ord(str[i]) != ord('+') and (ord(str[i]) == ord(' ') or ord(str[i]) == ord('0')):
            i += 1
            
        if i < len(str):
            if ord(str[i]) == ord('-'):
                is_nav = not is_nav
                i += 1
            elif ord(str[i]) == ord('+'):
                i += 1

        while i < len(str) and ord(str[i]) == ord('0'):
            i += 1

        while i < len(str):
            if ord(str[i]) > ord('9') or ord(str[i]) < ord('0'):
                break
            ret *= 10
            ret += ord(str[i]) - ord('0')
            i += 1
        
        if is_nav:
            ret = 0 - ret
        if ret > 2147483647:
            return 2147483647
        if ret < -2147483648:
            return -2147483648
        return ret