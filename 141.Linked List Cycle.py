# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        slow = head.next
        fast = head.next.next
        while fast and fast.next:
            if slow == fast or slow == fast.next:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
