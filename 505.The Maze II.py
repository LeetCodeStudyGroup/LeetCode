class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        if maze == None or len(maze) == 0 or len(maze[0]) == 0:
            return -1

        return self.bfs(maze, start, destination)

    def bfs(self, maze, start, dest):
        from collections import deque
        q = deque([[start, 0]])
        mark = [[-1] * len(maze[0]) for _ in range(len(maze))]
        dist = -1
        while len(q) > 0:
            for _ in range(len(q)):
                s, d = q.popleft()
                if s == dest:
                    if dist == -1 or d < dist:
                        dist = d
                    continue

                if mark[s[0]][s[1]] != -1 and d > mark[s[0]][s[1]]:
                    continue

                mark[s[0]][s[1]] = d
                i, j = s
                while i + 1 < len(maze) and maze[i + 1][j] == 0:
                    i += 1
                if i != s[0]:
                    q.append([[i, j], d + i - s[0]])

                i, j = s
                while i - 1 >= 0 and maze[i - 1][j] == 0:
                    i -= 1
                if i != s[0]:
                    q.append([[i, j], d + s[0] - i])

                i, j = s
                while j + 1 < len(maze[0]) and maze[i][j + 1] == 0:
                    j += 1
                if j != s[1]:
                    q.append([[i, j], d + j - s[1]])

                i, j = s
                while j - 1 >= 0 and maze[i][j - 1] == 0:
                    j -= 1
                if j != s[1]:
                    q.append([[i, j], d + s[1] - j])

        return dist
