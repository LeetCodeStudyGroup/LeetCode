class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        from collections import deque
        self.qs = deque()
        for v in [v1, v2]:
            if len(v) > 0:
                self.qs.append(deque(v))

    def next(self):
        """
        :rtype: int
        """
        q = self.qs.popleft()
        ret = q.popleft()
        if len(q) > 0:
            self.qs.append(q)
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.qs)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
