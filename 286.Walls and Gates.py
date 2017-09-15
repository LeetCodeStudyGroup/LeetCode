class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if rooms == None or len(rooms) == 0 or len(rooms[0]) == 0:
            return

        from collections import deque
        q = deque()
        mark = [[False] * len(rooms[0]) for _ in range(len(rooms))]
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    mark[i][j] = True
                    q.append((i, j))
        self.bfs(rooms, q, mark)

    def bfs(self, rooms, q, mark):
        layer = 1
        while len(q) > 0:
            for _ in range(len(q)):
                i, j = q.popleft()
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if x < 0 or y < 0 or x >= len(rooms) or y >= len(rooms[0]) or mark[x][y]:
                        continue
                    mark[x][y] = True
                    if rooms[x][y] > 0 and rooms[x][y] > layer:
                        q.append((x, y))
                        rooms[x][y] = layer
            layer += 1

