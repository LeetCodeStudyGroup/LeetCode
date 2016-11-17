# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        node, count = root, 0
        while True:
            count += 1
            ll, lr = self.get_deap(node.left)
            if ll != lr:
                node = node.left
                count += 2 ** lr - 1
            else:
                count += 2 ** ll - 1
                rl, rr = self.get_deap(node.right)
                if rl != rr:
                    node = node.right
                else:
                    count += 2 ** rl - 1
                    break
        return count

    def get_deap(self, root):
        l_deap = r_deap = 0
        ptr = root
        while ptr:
            l_deap += 1
            ptr = ptr.left
        ptr = root
        while ptr:
            r_deap += 1
            ptr = ptr.right
        return l_deap, r_deap

    def countNodes2(self, root):
        if not root: return 0
        l_deap = r_deap = 0
        ptr = root
        while ptr:
            l_deap += 1
            ptr = ptr.left
        ptr = root
        while ptr:
            r_deap += 1
            ptr = ptr.right
        if l_deap == r_deap:
            return 2 ** r_deap - 1
        val, find = self.counting(root, r_deap)
        return 2 ** r_deap - 1 + val

    def counting(self, node, h):
        if h == 1:
            ret = 0
            if node.left:
                ret += 1
            if node.right:
                ret += 1
            return ret, ret != 2
        else:
            left, find = self.counting(node.left, h - 1)
            if find:
                return left, find
            else:
                right, find = self.counting(node.right, h - 1)
                return left + right, find
