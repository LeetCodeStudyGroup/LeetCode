class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        i = 0
        while i < len(s):
            while i < len(s) and s[i] == ' ':
                i += 1
            if i == len(s):
                break
            start = i
            while i < len(s) and s[i] != ' ':
                i += 1
            result = s[start:i] if len(result) == 0 else s[start:i] + ' ' + result
        return result
