class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        matrix = [[0 for x in range(n)] for y in range(m)]
        matrix[0][0] = grid[0][0]
        for i in range(1, m):
            matrix[i][0] = matrix[i - 1][0] + grid[i][0]
        for j in range(1, n):
            matrix[0][j] = matrix[0][j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j - 1] > matrix[i - 1][j]:
                    matrix[i][j] = matrix[i - 1][j]  + grid[i][j]
                else:
                    matrix[i][j] = matrix[i][j - 1]  + grid[i][j]
        return matrix[m - 1][n - 1]
