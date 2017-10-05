class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        from collections import defaultdict
        row_mark, col_mark = defaultdict(int), defaultdict(int)
        for i, row in enumerate(picture):
            for j, cell in enumerate(row):
                if cell == 'B':
                    row_mark[i] += 1
                    col_mark[j] += 1
        rst = 0
        for i, row in enumerate(picture):
            for j, cell in enumerate(row):
                if cell == 'B' and row_mark[i] == 1 and col_mark[j] == 1:
                    rst += 1
        return rst
