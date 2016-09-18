class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = []
        self.last = None
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)
        self.last = x
        

    def pop(self):
        """
        :rtype: nothing
        """
        if self.empty():
            return

        x = None
        for i in range(len(self.queue) - 1):
            x = self.queue.pop(0)
            self.queue.append(x)
        self.last = x
        self.queue.pop(0)
        
    def top(self):
        """
        :rtype: int
        """
        return self.last
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0
