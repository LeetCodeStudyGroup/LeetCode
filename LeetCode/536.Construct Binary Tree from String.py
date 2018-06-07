# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if s == '':
            return None
        inx = self.find_next(s, 0)
        root = TreeNode(int(s[:inx]))
        stack = [root]
        while inx < len(s):
            inx += 1
            if s[inx - 1] == '(':
                start = inx
                inx = self.find_next(s, start)
                if start != inx:
                    node = TreeNode(int(s[start:inx]))
                    if stack[-1].left == None:
                        stack[-1].left = node
                    else:
                        stack[-1].right = node
                    stack.append(node)
            else:
                stack.pop()
        return root

    def find_next(self, s, start):
        inx = start
        while inx < len(s) and s[inx] != '(' and s[inx] != ')':
            inx += 1
        return inx

    def str2tree2(self, s):
        if s == '':
            return None

        val, left, right = self.get_tree(s)
        root = TreeNode(int(val))
        root.left = self.str2tree(left)
        root.right = self.str2tree(right)
        return root

    def get_tree(self, s):
        left = 0
        while left < len(s) and s[left] != '(':
            left += 1
        right, cnt = left + 1, 1
        while right < len(s) and cnt != 0:
            if s[right] == '(':
                cnt += 1
            elif s[right] == ')':
                cnt -= 1
            right += 1
        return s[:left], s[left:right], s[right:]
