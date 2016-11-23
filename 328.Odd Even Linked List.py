# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd, even = ListNode(0), ListNode(0)
        ptr_odd, ptr_even = odd, even
        ptr, is_odd = head, True
        while ptr:
            if is_odd:
                ptr_odd.next = ptr
                ptr_odd = ptr_odd.next
            else:
                ptr_even.next = ptr
                ptr_even = ptr_even.next
            ptr, is_odd = ptr.next, not is_odd
        ptr_odd.next, ptr_even.next = even.next, None
        return odd.next
