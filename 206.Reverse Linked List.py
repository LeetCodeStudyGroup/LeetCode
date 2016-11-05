# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = ptr = head
        last = dummy
        while ptr:
            ptr.next, last, ptr = last, ptr, ptr.next
        if last == dummy:
            return None
        head.next = None
        return last

    def reverseList2(self, head):
        if not head:
            return None
        new_head = self.recursive(head)
        head.next = None
        return new_head
        
    def recursive(self, node):
        if not node:
            return None
        elif not node.next:
            return node
        else:
            head = self.recursive(node.next)
            node.next.next = node
            return head
