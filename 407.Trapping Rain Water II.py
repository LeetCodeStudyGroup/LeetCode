from collections import deque
from heapq import *

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        rst = 0
        if len(heightMap) == 0 or len(heightMap[0]) == 0:
            return rst

        m, n = len(heightMap), len(heightMap[0])
        visited, h = [[False] * n for _ in range(m)], []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heappush(h, (heightMap[i][j], i, j))
                    visited[i][j] = True
        level = 0
        while len(h) > 0:
            height, i, j = heappop(h)
            level = max(level, height)
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if x < 0 or y < 0 or x >= m or y >= n or visited[x][y]:
                    continue
                visited[x][y] = True
                if heightMap[x][y] < level:
                    rst += level - heightMap[x][y]
                heappush(h, (heightMap[x][y], x, y))
        return rst
