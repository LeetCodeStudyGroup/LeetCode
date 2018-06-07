class Solution(object):
    def minDistance(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """
        import sys
        rst, total, min_val = 0, 0, sys.maxint
        for nut in nuts:
            d_tree = self.get_dist(nut, tree)
            min_val = min(min_val, self.get_dist(nut, squirrel) - d_tree)
            total += d_tree
        return min_val + total * 2

    def get_dist(self, n1, n2):
        return abs(n1[0] - n2[0]) + abs(n1[1] - n2[1])
