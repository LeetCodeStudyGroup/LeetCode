class Solution(object):
    def encode(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = [[s] * len(s) for _ in range(len(s))]
        for length in range(len(s)):
            for i in range(len(s) - length):
                j = i + length
                substr = s[i:j + 1]
                dp[i][j] = substr
                if length > 3:
                    for k in range(j):
                        if len(dp[i][k]) + len(dp[k + 1][j]) < len(dp[i][j]):
                            dp[i][j] = dp[i][k] + dp[k + 1][j]
                    for k in range(len(substr)):
                        repeat = substr[:k + 1]
                        is_repeat = len(repeat) > 0 and len(substr) % len(repeat) == 0
                        if is_repeat and substr.replace(repeat, '') == '':
                            newstr = str(len(substr) / len(repeat)) + '[' + dp[i][i + k] + ']'
                            if len(newstr) < len(dp[i][j]):
                                dp[i][j] = newstr
        return dp[0][-1]
