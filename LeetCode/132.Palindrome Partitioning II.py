class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        pal = [[False for x in range(len(s))] for y in range(len(s))]
        cut = [0] * len(s)
        for i in range(len(s) - 1, -1, -1):
            cut[i] = len(s) - i + 1
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i < 2 or pal[i + 1][j - 1]):
                    pal[i][j] = True
                    if j == len(s) - 1:
                        cut[i] = 0
                    else:
                        cut[i] = min(cut[i], cut[j + 1] + 1)
        return cut[0]
