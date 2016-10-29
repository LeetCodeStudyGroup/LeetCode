# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nodes = []
        self.add_node(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.nodes) > 0

    def next(self):
        """
        :rtype: int
        """
        node = self.nodes.pop()
        self.add_node(node.right)
        return node.val
        
    def add_node(self, node):
        while node:
            self.nodes.append(node)
            node = node.left

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
