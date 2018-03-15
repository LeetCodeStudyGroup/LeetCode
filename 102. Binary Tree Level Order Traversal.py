# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import Queue

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if root is None:
            return []
        
        rlist = []
        
        queue = Queue()
        queue.put(root)
        
        while not queue.empty():
            temp = []
            size = queue.qsize()
            for i in range(size):
                node = queue.get()
                temp.append(node.val)
                
                if node.left is not None:
                    queue.put(node.left)
                    
                if node.right is not None:
                    queue.put(node.right)
                
            rlist.append(temp)
        
        return rlist
