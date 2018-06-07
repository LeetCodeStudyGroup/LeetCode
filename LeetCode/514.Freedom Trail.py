class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        n, m = len(key), len(ring)
        if n == 0 or m == 0:
            return 0

        rst = max_len = (m + 1) * n
        dp = [[max_len] * (m + 1) for x in range(n + 1)]
        table = collections.defaultdict(list)
        for i in range(m):
            dp[0][i] = self.min_step(m, i)
            table[ring[i]].append(i)

        for k in range(n):
            for i in table[key[k]]:
                if dp[k + 1][i] <= dp[k][i] + 1:
                    continue
                dp[k + 1][i] = dp[k][i] + 1
                for j in range(1, m):
                    inx = (i + j) % m
                    next_step = self.min_step(m, j) + dp[k + 1][i]
                    dp[k + 1][inx] = min(dp[k + 1][inx], next_step)

        for i in range(m):
            rst = min(rst, dp[-1][i])
        return rst

    def min_step(self, length, i):
        return min(i, length - i)
