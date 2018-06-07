# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        self.do_connect(root, root)

    def do_connect(self, node, head):
        if not node:
            return
        if node.left:
            node.left.next = self.find_next(node.right, node.next)
        if node.right:
            node.right.next = self.find_next(None, node.next)
        if node.next:
            self.do_connect(node.next, head)
        else:
            next = self.find_next(None, head)
            self.do_connect(next, next)

    def find_next(self, node, next_node):
        while not node and next_node:
            node = next_node.left if next_node.left else next_node.right
            next_node = next_node.next
        return node
