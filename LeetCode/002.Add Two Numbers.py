# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None: return l2
        if l2 == None: return l1

        ptr1 = l1
        ptr2 = l2
        val = ptr1.val + ptr2.val
        ptr1.val = val % 10
        val = val / 10

        while ptr1.next != None and ptr2.next != None:
            val += ptr1.next.val + ptr2.next.val
            ptr1.next.val = val % 10
            val = val / 10
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        if ptr1.next == None and ptr2.next != None:
            ptr1.next = ptr2.next

        self.add_tail(ptr1, val)
        return l1
        
    def add_tail(self, ptr, val):
        while ptr.next != None and val != 0:
            val += ptr.next.val
            ptr.next.val = val % 10
            val = val / 10
            ptr = ptr.next
        if ptr.next == None and val > 0:
            node = ListNode(val)
            ptr.next = node
