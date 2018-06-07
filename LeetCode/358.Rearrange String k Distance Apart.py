from collections import defaultdict
from heapq import *

class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k == 0:
            return s

        chars = defaultdict(int)
        for c in s:
            chars[c] += 1
        pq = []
        for key, val in chars.items():
            heappush(pq, (-val, key)) # max heap

        rst = []
        length = len(s)
        while len(pq) > 0:
            cache = []
            for _ in range(k):
                if len(pq) == 0:
                    return ''
                val, key = heappop(pq)
                val += 1
                rst.append(key)
                if len(rst) == len(s):
                    break
                if val < 0:
                    cache.append((val, key))
            for item in cache:
                heappush(pq, item)
        return ''.join(rst)
