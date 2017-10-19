class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        import sys
        dist = -sys.maxint
        min_val, max_val = arrays[0][0], arrays[0][-1]
        for i in range(1, len(arrays)):
            dist = max(dist, max_val - arrays[i][0], arrays[i][-1] - min_val)
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])
        return dist
