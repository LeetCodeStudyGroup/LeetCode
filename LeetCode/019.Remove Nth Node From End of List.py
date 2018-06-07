# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        ptr = head
        target = 0
        while ptr != None:
            ptr = ptr.next
            target += 1
        target -= n

        if target < 0:
            return head
        elif target == 0:
            head = head.next
            return head

        ptr = head
        while target > 1:
            ptr = ptr.next
            target -= 1
        ptr.next = ptr.next.next
        return head
            