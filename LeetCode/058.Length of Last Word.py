class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = len(s) - 1
        while start >= 0:
            if s[start] != ' ':
                break
            start -= 1

        i = start
        while i >= 0:
            if s[i] == ' ':
                break
            i -= 1
        return start - i
