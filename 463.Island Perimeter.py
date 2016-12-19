class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0: return 0
        cnt, m, n = 0, len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt += self.counting(grid, m, n, i, j)
        return cnt

    def counting(self, grid, m, n, i, j):
        cnt = 0
        for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if i + x == m or i + x < 0 or j + y == n or j + y < 0 or grid[i + x][j + y] == 0:
                cnt += 1
        return cnt
