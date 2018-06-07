class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if self.is_square(n):
            return 1
        while n & 3 == 0:
            n = n >> 2
        if n & 7 == 7:
            return 4
        for i in range(int(n ** 0.5) + 1):
            if self.is_square(n - i * i):
                return 2
        return 3

    def is_square(self, n):
        s = int(n ** 0.5)
        return n == s * s

    def numSquares_DP(self, n):
        dp, square = [0] * (n + 1), [1]
        for i in range(1, n + 1):
            dp[i] = i
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]
