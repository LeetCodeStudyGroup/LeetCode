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
        self.do_connect(root, None)
        
    def do_connect(self, node, next_node):
        if not node:
            return
        node.next = next_node
        self.do_connect(node.left, node.right)
        if node.next:
            self.do_connect(node.right, node.next.left)
        else:
            self.do_connect(node.right, None)
