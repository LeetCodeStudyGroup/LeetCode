class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i = j = 0
        for size in s:
            if g[i] <= size:
                i += 1
            if i == len(g):
                break
        return i
