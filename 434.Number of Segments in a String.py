class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        while start < len(s) and s[start] == ' ':
            start += 1
        if start == len(s): return 0
        cnt = 1
        for i in range(start + 1, len(s)):
            if s[i - 1] == ' ' and s[i] != ' ':
                cnt += 1
        return cnt
