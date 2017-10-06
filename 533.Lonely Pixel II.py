class Solution(object):
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        from collections import defaultdict
        row_mark, col_mark = defaultdict(set), defaultdict(set)
        for i, row in enumerate(picture):
            for j, cell in enumerate(row):
                if cell == 'B':
                    row_mark[i].add(j)
                    col_mark[j].add(i)
        rst = 0
        for i, row in enumerate(picture):
            for j, cell in enumerate(row):
                if len(row_mark[i]) == N and len(col_mark[j]) == N and i in col_mark[j] and cell == 'B':
                    rst += 1
                    for r in col_mark[j]:
                        if not row_mark[i] == row_mark[r]:
                            rst -= 1
                            break
        return rst
