# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        prenode = dummy = ListNode(0)
        dummy.next = head
        ptr = head
        is_dup = False
        while ptr.next != None:
            if ptr.val == ptr.next.val:
                ptr.next = ptr.next.next
                is_dup = True
            else:
                if is_dup:
                    prenode.next = ptr.next
                else:
                    prenode = ptr
                ptr = ptr.next
                is_dup = False
        if is_dup:
            prenode.next = None
        return dummy.next
