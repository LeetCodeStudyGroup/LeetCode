# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0: return None
        root = TreeNode(preorder[0])
        nodes = [root]
        indexs = [(1, 0, len(inorder) - 1)]
        while len(nodes) > 0:
            node = nodes.pop()
            pre_start, in_start, in_end = indexs.pop()
            inx = in_start
            while inorder[inx] != node.val:
                inx += 1
            if inx > in_start:
                node.left = TreeNode(preorder[pre_start])
                nodes.append(node.left)
                indexs.append((pre_start + 1, in_start, inx - 1))
            if inx < in_end:
                node.right = TreeNode(preorder[pre_start + (inx - in_start)])
                nodes.append(node.right)
                indexs.append((pre_start + (inx - in_start) + 1, inx + 1, in_end))
        return root

    def buildTree2(self, preorder, inorder):
        if len(preorder) == 0: return None
        root = TreeNode(preorder[0])
        self.build(preorder, inorder, 1, 0, len(inorder) - 1, root)
        return root

    def build(self, preorder, inorder, pres, ins, ine, root):
        inx = ins
        while inorder[inx] != root.val:
            inx += 1
        if inx > ins:
            root.left = TreeNode(preorder[pres])
            self.build(preorder, inorder, pres + 1, ins, inx - 1, root.left)
        if inx < ine:
            d = inx - ins
            root.right = TreeNode(preorder[pres + d])
            self.build(preorder, inorder, pres + d + 1, inx + 1, ine, root.right)
