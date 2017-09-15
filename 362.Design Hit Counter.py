class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import deque
        self.q = deque()
        self.max_time = 300

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.q.append(timestamp)
        self.update(timestamp)

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        self.update(timestamp)
        return len(self.q)

    def update(self, timestamp):
        if len(self.q) > 0:
            while len(self.q) > 0 and (timestamp - self.q[0]) >= self.max_time:
                self.q.popleft()


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
