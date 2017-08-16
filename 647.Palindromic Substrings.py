class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        rst = 0
        for i in range(len(s)):
            rst += self.palindromic(s, i, i)
            if i + 1 < len(s) and s[i] == s[i + 1]:
                rst += self.palindromic(s, i, i + 1)
        return rst

    def palindromic(self, s, i, j):
        cnt = 1
        i, j = i - 1, j + 1
        while i >= 0 and j < len(s):
            if s[i] != s[j]:
                break
            cnt += 1
            i, j = i - 1, j + 1
        return cnt

    def countSubstrings2(self, s):
        rst = 0
        dp = [[False for x in range(len(s))] for y in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                dp[i][j] = (s[i] == s[j]) and (j - i <= 2 or dp[i + 1][j - 1])
                if dp[i][j]:
                    rst += 1
        return rst
