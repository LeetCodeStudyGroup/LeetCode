# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        i = 0
        while i < m - 1:
            cur = cur.next
            i += 1
        start = last = cur
        end = cur = cur.next
        while i < n:
            tmp = cur.next
            cur.next = last
            last = cur
            cur = tmp
            i += 1
        start.next = last
        end.next = cur
        return dummy.next
