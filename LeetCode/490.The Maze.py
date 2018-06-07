class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        if maze == None or len(maze) == 0 or len(maze[0]) == 0:
            return False

        mark = [[False] * len(maze[0]) for _ in range(len(maze))]
        return self.helper(maze, start, destination, mark)

    def helper(self, maze, start, dest, mark):
        if start == dest:
            return True

        if mark[start[0]][start[1]]:
            return False

        mark[start[0]][start[1]] = True
        i, j = start
        while i + 1 < len(maze) and maze[i + 1][j] != 1:
            i += 1
        if i != start[0]:
            if self.helper(maze, [i, j], dest, mark):
                return True

        i, j = start
        while i - 1 >= 0 and maze[i - 1][j] != 1:
            i -= 1
        if i != start[0]:
            if self.helper(maze, [i, j], dest, mark):
                return True

        i, j = start
        while j + 1 < len(maze[0]) and maze[i][j + 1] != 1:
            j += 1
        if j != start[1]:
            if self.helper(maze, [i, j], dest, mark):
                return True

        i, j = start
        while j - 1 >= 0 and maze[i][j - 1] != 1:
            j -= 1
        if j != start[1]:
            if self.helper(maze, [i, j], dest, mark):
                return True

        return False
