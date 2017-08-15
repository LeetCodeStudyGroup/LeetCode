class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 0
        for d in range(2, n + 1):
            while n % d == 0:
                s += d
                n /= d
        return s

    def minSteps2(self, n):
        if n == 0:
            return 0
        dp = [x for x in range(n + 1)]
        dp[1] = 0
        for i in range(2, n + 1):
            cnt = dp[i] + 1
            for j in range(i, n + 1, i):
                dp[j] = min(dp[j], cnt)
                cnt += 1
        return dp[n]

