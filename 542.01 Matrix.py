from collections import deque

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        m, n = len(matrix), len(matrix[0])
        rst = [[m * n] * n for _ in range(m)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    q.append((i, j))
                    rst[i][j] = 0
        while len(q) > 0:
            for _ in range(len(q)):
                i, j = q.popleft()
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if x < 0 or y < 0 or x >= m or y >= n or rst[x][y] != m * n:
                        continue
                    rst[x][y] = min(rst[x][y], rst[i][j] + 1)
                    q.append((x, y))
        return rst
