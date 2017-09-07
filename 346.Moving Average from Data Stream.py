class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        from collections import deque
        self.q = deque()
        self.size = size
        self.sum = 0.0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.q) == self.size:
            self.sum -= self.q.popleft()
        self.q.append(val)
        self.sum += val
        return self.sum / len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
