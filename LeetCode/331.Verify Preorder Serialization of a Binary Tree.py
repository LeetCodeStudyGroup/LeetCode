class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes = preorder.split(',')
        stack, i = 0, 0
        while i < len(nodes) - 1:
            while i < len(nodes) and nodes[i] != '#':
                stack, i = stack + 1, i + 1
            while i < len(nodes) and nodes[i] == '#':
                if stack == 0:
                    return i == len(nodes) - 1
                stack, i = stack - 1, i + 1
        return i == len(nodes) - 1 and nodes[i] == '#'
