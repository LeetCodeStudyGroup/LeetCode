from collections import deque

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == None or len(grid) == 0 or len(grid[0]) == 0:
            return -1

        m, n = len(grid), len(grid[0])
        building = 0
        for row in grid:
            building += row.count(1)
        if building == 0:
            return -1

        rst = -1
        maps = [[(0, 0)] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dis = self.bfs(grid, m, n, i, j, building, maps)
        for i in range(m):
            for j in range(n):
                if maps[i][j][1] == building:
                    if rst == -1 or rst > maps[i][j][0]:
                        rst = maps[i][j][0]
        return rst

    def bfs(self, grid, m, n, si, sj, count, maps):
        mark = [[0] * n for _ in range(m)]
        mark[si][sj] = 1
        q = deque([(si, sj)])
        rst, layer = 0, 0
        while len(q) > 0:
            layer += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if x < 0 or y < 0 or x >= m or y >= n or mark[x][y] == 1:
                        continue
                    mark[x][y] = 1
                    if grid[x][y] == 0:
                        maps[x][y] = (maps[x][y][0] + layer, maps[x][y][1] + 1)
                        q.append((x, y))
        return -1
