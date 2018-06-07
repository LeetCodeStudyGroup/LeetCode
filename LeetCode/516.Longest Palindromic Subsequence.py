class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        dp1, dp2 = [0] * len(s), [0] * len(s)
        for i in range(len(s) - 1, -1, -1):
            dp2[i] = 1
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp2[j] = dp1[j - 1] + 2
                else:
                    dp2[j] = max(dp1[j], dp2[j - 1])
            dp1, dp2 = dp2, dp1
        return dp1[-1]
