class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        matrix = obstacleGrid[:]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = 1
        for i in range(1, m):
            if matrix[i][0] != 0:
                matrix[i][0] = matrix[i - 1][0]
        for j in range(1, n):
            if matrix[0][j] != 0:
                matrix[0][j] = matrix[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != 0:
                    matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
        return matrix[m - 1][n - 1]
