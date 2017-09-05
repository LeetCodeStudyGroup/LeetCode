# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
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

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        if s == None:
            return None
        num, inx = self.parsenum(s, 0, len(s) - 1)
        return num

    def parsenum(self, s, start, end):
        if start > end:
            return None, start

        nested = NestedInteger()
        if s[start] == '[':
            start += 1
            while start <= end and (s[start - 1] == '[' or s[start - 1] == ','):
                num, start = self.parsenum(s, start, end)
                if num != None:
                    nested.add(num)
            start += 1
        else:
            num, start = self.parseint(s, start, end)
            if num != None:
                nested.setInteger(num)
            else:
                nested = None

        return nested, start

    def parseint(self, s, start, end):
        num = ''
        while start <= end:
            if not self.is_num(s, start):
                break
            num += s[start]
            start += 1
        if num == "":
            return None, start + 1
        return int(num), start + 1

    def is_num(self, s, i):
        return (ord(s[i]) >= ord('0') and ord(s[i]) <= ord('9')) or s[i] == '-'
