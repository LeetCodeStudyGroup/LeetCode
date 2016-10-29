# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = self.get_cycle_node(head)
        if not fast:
            return None
        slow = head
        while fast != slow and fast.next != slow:
            slow = slow.next
            fast = fast.next
        return slow

    def get_cycle_node(self, head):
        if not head or not head.next:
            return None
        slow = head.next
        fast = head.next.next
        while fast and fast.next:
            if slow == fast or slow == fast.next:
                return slow
            slow = slow.next
            fast = fast.next.next
        return None
