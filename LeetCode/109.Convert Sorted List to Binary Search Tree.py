# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        return self.BST(head, None)

    def BST(self, head, tail):
        if head == tail:
            return None
        fast = slow = head
        while fast.next != tail and fast.next.next != tail:
            fast = fast.next.next
            slow = slow.next
        node = TreeNode(slow.val)
        if slow != fast:
            node.left = self.BST(head, slow)
        node.right = self.BST(slow.next, tail)
        return node
