from heapq import *
from collections import defaultdict

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        heights = []
        for building in buildings:
            heights.append((building[0], -building[2]))
            heights.append((building[1], building[2]))
        heights.sort()

        rst = []
        pq, removed, pre = [0], defaultdict(int), 0  # max priority queue
        for h in heights:
            if h[1] < 0:
                heappush(pq, h[1])
            elif h[1] > 0:
                removed[-h[1]] += 1

            while removed[pq[0]] > 0:
                removed[pq[0]] -= 1
                heappop(pq)

            if pq[0] != pre:
                rst.append([h[0], -pq[0]])
                pre = pq[0]
        return rst
