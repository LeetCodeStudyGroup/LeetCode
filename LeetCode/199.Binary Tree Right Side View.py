# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        result = []
        node_list = [root]
        while len(node_list) > 0:
            result.append(node_list[0].val)
            for i in range(len(node_list)):
                node = node_list.pop(0)
                if node.right:
                    node_list.append(node.right)
                if node.left:
                    node_list.append(node.left)
        return result
