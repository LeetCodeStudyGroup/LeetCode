class Solution(object):
    def maxKilledEnemies(self, grid):
        if grid == None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        max_cnt = 0
        rowhits, colhits = 0, [0] * n
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if j == 0 or row[j - 1] == 'W':
                    rowhits = 0
                    k = j
                    while k < n and row[k] != 'W':
                        if row[k] == 'E':
                            rowhits += 1
                        k += 1
                if i == 0 or grid[i - 1][j] == 'W':
                    colhits[j] = 0
                    k = i
                    while k < m and grid[k][j] != 'W':
                        if grid[k][j] == 'E':
                            colhits[j] += 1
                        k += 1
                if cell == '0':
                    max_cnt = max(max_cnt, rowhits + colhits[j])
        return max_cnt

    def maxKilledEnemies2(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        n, m = len(grid), len(grid[0])
        left, right = [[0] * m for _ in range(n)], [[0] * m for _ in range(n)]
        up, down = [[0] * m for _ in range(n)], [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                cnt = left[i][j - 1] if j > 0 else 0
                left[i][j] = self.update(grid[i][j], cnt)
            for j in range(m - 1, -1, -1):
                cnt = right[i][j + 1] if j + 1 < m else 0
                right[i][j] = self.update(grid[i][j], cnt)
        for i in range(m):
            for j in range(n):
                cnt = up[j - 1][i] if j > 0 else 0
                up[j][i] = self.update(grid[j][i], cnt)
            for j in range(n - 1, -1, -1):
                cnt = down[j + 1][i] if j + 1 < n else 0
                down[j][i] = self.update(grid[j][i], cnt)
        max_cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '0':
                    max_cnt = max(max_cnt, left[i][j] + right[i][j] + up[i][j] + down[i][j])
        return max_cnt

    def update(self, point, cnt):
        if point == 'W':
            cnt = 0
        elif point == 'E':
            cnt += 1
        return cnt
