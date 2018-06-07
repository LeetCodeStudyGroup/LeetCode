class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.first = None
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        if self.first == None:
            self.first = x
        

    def pop(self):
        """
        :rtype: nothing
        """
        if self.empty():
            return

        temp_stack = []
        for i in range(len(self.stack) - 1):
            self.first = self.stack.pop(-1)
            temp_stack.append(self.first)
        self.stack.pop(-1)
 
        for i in range(len(temp_stack)):
            self.stack.append(temp_stack.pop(-1))

        if self.empty():
            self.first = None
        

    def peek(self):
        """
        :rtype: int
        """
        return self.first
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0
