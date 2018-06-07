# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(postorder) == 0: return None
        root = TreeNode(postorder[-1])
        self.build(inorder, postorder, len(postorder) - 2, 0, len(inorder) - 1, root)
        return root

    def build(self, inorder, postorder, post_end, in_start, in_end, root):
        inx = in_start
        while inorder[inx] != root.val:
            inx += 1
        if inx > in_start:
            root.left = TreeNode(postorder[post_end - (in_end - inx)])
            self.build(inorder, postorder, post_end - (in_end - inx) - 1, in_start, inx - 1, root.left)
        if inx < in_end:
            root.right = TreeNode(postorder[post_end])
            self.build(inorder, postorder, post_end - 1, inx + 1, in_end, root.right)
