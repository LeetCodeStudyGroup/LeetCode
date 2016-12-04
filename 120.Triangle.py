class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0: return 0
        paths = [0] * len(triangle[-1])
        for i in range(len(triangle) - 1, 0, -1):
            next = [0] * (len(triangle[i]) - 1)
            for j in range(len(next)):
                x = triangle[i][j] + paths[j]
                y = triangle[i][j + 1] + paths[j + 1]
                next[j] = x if x < y else y
            paths = next
        return paths[0] + triangle[0][0]
