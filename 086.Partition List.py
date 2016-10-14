# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        less_list = ListNode(0)
        less = less_list
        greater_list = ListNode(0)
        greater = greater_list
        cur = head
        while cur != None:
            tmp = cur
            cur = cur.next
            if tmp.val < x:
                less.next = tmp
                less = less.next
                less.next = None
            else:
                greater.next = tmp
                greater = greater.next
                greater.next = None
        head = less_list.next
        if head:
            less.next = greater_list.next
        else:
            head = greater_list.next
        return head
        
        
