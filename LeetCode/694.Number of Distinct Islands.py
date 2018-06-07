class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        islands = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    points = []
                    self.helper(grid, m, n, visited, i, j, i, j, points)
                    islands.add(''.join(points))
        return len(islands)

    def helper(self, grid, m, n, visited, start, end, i, j, points):
        points.append(str(i - start) + str(j - end))
        visited[i][j] = True
        for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
            if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] == 0 or visited[x][y]:
                continue
            self.helper(grid, m, n, visited, start, end, x, y, points)
