# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        self.ary, self.inx = nestedList, 0
        self.move()

    def next(self):
        """
        :rtype: int
        """
        val = self.ary[self.inx]
        self.inx += 1
        self.move()
        return val.getInteger()

    def move(self):
        if self.inx == len(self.ary):
            if len(self.stack) == 0:
                return
            self.ary, self.inx = self.stack.pop()
        val = self.ary[self.inx]
        while not val.isInteger():
            self.inx += 1
            if self.inx < len(self.ary):
                self.stack.append((self.ary, self.inx))
            self.ary, self.inx = val.getList(), 0
            if self.inx == len(self.ary):
                if len(self.stack) == 0:
                    return
                self.ary, self.inx = self.stack.pop()
            val = self.ary[self.inx]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.inx < len(self.ary)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
