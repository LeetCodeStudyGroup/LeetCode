class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = [0] * (N + 1)
        for i in range(N):
            dp[i + 1] = dp[i] + 1
            for j in range(i - 3, -1, -1):
                dp[i + 1] = max(dp[i + 1], dp[j] * (i - j))
        return dp[-1]
