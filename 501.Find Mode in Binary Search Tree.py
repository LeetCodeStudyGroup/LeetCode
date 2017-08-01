# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.cur_val = None
        self.cur_cnt = 0
        self.max_cnt = 0
        self.values = []

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            self.inorder(root)
            self.update()
        return self.values

    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        self.handler(node)
        self.inorder(node.right)

    def handler(self, node):
        if self.cur_val == None or self.cur_val == node.val:
            self.cur_cnt += 1
        else:
            self.update()
        self.cur_val = node.val

    def update(self):
        if self.cur_cnt == self.max_cnt:
            self.values.append(self.cur_val)
        elif self.cur_cnt > self.max_cnt:
            self.values = [self.cur_val]
            self.max_cnt = self.cur_cnt
        self.cur_cnt = 1
