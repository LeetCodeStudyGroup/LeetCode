class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = []
        for i in range(m + 1):
            dp.append([0] * (n + 1))
        for string in strs:
            x, y = self.transfer(string)
            for i in range(m, x - 1, -1):
                for j in range(n, y - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - x][j - y] + 1)
        return dp[m][n]

    def transfer(self, string):
        m, n = 0, 0
        for c in string:
            if c == '0':
                m += 1
            else:
                n += 1
        return (m, n)
