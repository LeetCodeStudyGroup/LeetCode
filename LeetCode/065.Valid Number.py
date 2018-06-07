class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = 0
        while start < len(s):
            if s[start] != ' ':
                break
            start += 1
        end = len(s) -1
        while end >= 0:
            if s[end] != ' ':
                break
            end -= 1
        
        has_sign = False
        has_number = False
        has_point = False
        has_e = False
        while start <= end:            
            if self.is_zero_nine(s[start]):
                has_number = True
            elif (s[start] == '-' or s[start] == '+') and not has_number and not has_sign and not has_point:
                has_sign = True
            elif s[start] == '.' and not has_point and not has_e:
                has_point = True
            elif s[start] == 'e' and not has_e and has_number:
                has_e = True
                has_sign = False
                has_point = False
                has_number = False
            else:
                return False
            start += 1
        return has_number
        
    def is_zero_nine(self, c):
        return ord(c) >= ord('0') and ord(c) <= ord('9')
