from collections import deque

class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rst = []
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return rst

        m, n = len(matrix), len(matrix[0])
        maps = [[0] * n for _ in range(m)]
        q = deque()
        for i in range(n):
            maps[0][i] = 1
            q.append((0, i))
        for i in range(1, m):
            maps[i][0] = 1
            q.append((i, 0))
        self.bfs(matrix, m, n, maps, 1, q)
        for i in range(n):
            maps[m - 1][i] += 2
            q.append((m - 1, i))
        for i in range(m - 1):
            maps[i][n - 1] += 2
            q.append((i, n - 1))
        self.bfs(matrix, m, n, maps, 2, q)

        for i in range(m):
            for j in range(n):
                if maps[i][j] == 3:
                    rst.append([i, j])
        return rst

    def bfs(self, matrix, m, n, maps, val, q):
        while len(q) > 0:
            for _ in range(len(q)):
                i, j = q.popleft()
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if x < 0 or y < 0 or x >= m or y >= n:
                        continue
                    if maps[x][y] & val == 0 and matrix[i][j] <= matrix[x][y]:
                        maps[x][y] += val
                        q.append((x, y))
