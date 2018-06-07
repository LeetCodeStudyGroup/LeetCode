class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area = abs((A - C) * (B - D)) + abs((E - G) * (F - H))
        unit = 0
        if A < G and E < C and F < D and B < H:
            w = min(C, G) - max(A, E)
            h = min(D, H) - max(B, F)
            unit = w * h 
        return area - unit
