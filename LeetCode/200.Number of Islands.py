class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        mark = map(lambda x: map(lambda y: True if y == '1' else False, x) , grid)
        count = 0
        for i in range(m):
            for j in range(n):
                if mark[i][j]:
                    count += 1
                    mark[i][j] = False
                    record = [(i, j)]
                    while len(record) > 0:
                        x, y = record.pop()
                        if x + 1 < m and mark[x + 1][y]:
                            mark[x + 1][y] = False
                            record.append((x + 1, y))
                        if x - 1 >= 0 and mark[x - 1][y]:
                            mark[x - 1][y] = False
                            record.append((x - 1, y))
                        if y + 1 < n and mark[x][y + 1]:
                            mark[x][y + 1] = False
                            record.append((x, y + 1))
                        if y - 1 >= 0 and mark[x][y - 1]:
                            mark[x][y - 1] = False
                            record.append((x, y - 1))
        return count
