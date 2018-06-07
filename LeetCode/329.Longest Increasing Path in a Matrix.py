class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        rst = 0
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return rst

        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                rst = max(rst, self.dfs(dp, matrix, i, j))
        return rst

    def dfs(self, dp, matrix, i, j):
        if dp[i][j] > 0:
            return dp[i][j]
        val = 0
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]):
                continue
            if matrix[i][j] < matrix[x][y]:
                val = max(val, self.dfs(dp, matrix, x, y))
        dp[i][j] = val + 1
        return dp[i][j]
