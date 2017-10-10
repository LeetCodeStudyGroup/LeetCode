class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        rst = 0
        if len(M) == 0 or len(M[0]) == 0:
            return rst

        m, n = len(M), len(M[0])
        hor = [[-1] * n for _ in range(m)]
        ver = [[-1] * n for _ in range(m)]
        diagonal = [[0] * n for _ in range(m)]
        autidia = [[0] * n for _ in range(m)]
        for i, rows in enumerate(M):
            for j, cell in enumerate(rows):
                if cell == 1:
                    hor[i][j] = hor[i][j - 1] + 1 if j > 0 else 1
                    ver[i][j] = ver[i - 1][j] + 1 if i > 0 else 1
                    diagonal[i][j] = diagonal[i - 1][j - 1] + 1 if i > 0 and j > 0 else 1
                    autidia[i][j] = autidia[i - 1][j + 1] + 1 if i > 0 and j < n - 1 else 1
                else:
                    hor[i][j] = 0
                    ver[i][j] = 0
                    diagonal[i][j] = 0
                    autidia[i][j] = 0
                rst = max(rst, hor[i][j], ver[i][j], diagonal[i][j], autidia[i][j])
        return rst
