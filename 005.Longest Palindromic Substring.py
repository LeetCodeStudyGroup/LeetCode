class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rst = ''
        for i in range(len(s)):
            sub = self.palindromic(s, i, i)
            if len(sub) > len(rst):
                rst = sub
            if i + 1 < len(s) and s[i] == s[i + 1]:
                sub = self.palindromic(s, i, i + 1)
                if len(sub) > len(rst):
                    rst = sub
        return rst

    def palindromic(self, s, i, j):
        while i >= 0 and j < len(s):
            if s[i] != s[j]:
                break
            i, j = i - 1, j + 1
        return s[i + 1:j]

    def longestPalindrome2(self, s):
        rst, dp = '', [[False for x in range(len(s))] for y in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                dp[i][j] = (s[i] == s[j]) and ((j - i < 3) or dp[i + 1][j - 1])
                if dp[i][j] and j - i + 1 > len(rst):
                    rst = s[i:j + 1]
        return rst
