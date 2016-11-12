class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = [0] * 26
        for c in s:
            table[ord(c) - ord('a')] += 1
        for i in range(len(s)):
            if table[ord(s[i]) - ord('a')] == 1:
                return i
        return -1
