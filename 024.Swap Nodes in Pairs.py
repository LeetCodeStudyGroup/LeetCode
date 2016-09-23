# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_node = ListNode(0)
        dummy_node.next = head
        ptr = dummy_node
        while ptr != None and ptr.next != None and ptr.next.next != None:
            first = ptr.next
            second = ptr.next.next
            first.next = second.next
            second.next = first
            ptr.next = second
            ptr = first
        return dummy_node.next
