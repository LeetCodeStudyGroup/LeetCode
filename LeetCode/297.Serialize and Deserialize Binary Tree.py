# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        rst = [str(root.val)]
        queue = deque()
        queue.append(root)
        have_node = True
        while have_node > 0:
            local = []
            have_node = False
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    local.append(str(node.left.val))
                    queue.append(node.left)
                    have_node = True
                else:
                    local.append("#")

                if node.right:
                    local.append(str(node.right.val))
                    queue.append(node.right)
                    have_node = True
                else:
                    local.append("#")
            rst += local
        return ','.join(rst)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None

        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        queue = deque()
        queue.append(root)

        i = 1
        while i < len(nodes):
            for j in range(len(queue)):
                node = queue.popleft()
                if nodes[i] != '#':
                    node.left = TreeNode(int(nodes[i]))
                    queue.append(node.left)
                i += 1
                if nodes[i] != '#':
                    node.right = TreeNode(int(nodes[i]))
                    queue.append(node.right)
                i += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
