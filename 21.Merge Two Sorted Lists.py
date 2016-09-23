# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy_node = ListNode(0)
        ptr_cur = dummy_node
        ptr1 = l1
        ptr2 = l2
        while ptr1 != None and ptr2 != None:
            if ptr1.val < ptr2.val:
                ptr_cur.next = ptr1
                ptr1 = ptr1.next
            else:
                ptr_cur.next = ptr2
                ptr2 = ptr2.next
            ptr_cur = ptr_cur.next

        if ptr1 != None:
            ptr_cur.next = ptr1
        if ptr2 != None:
            ptr_cur.next = ptr2
                
        return dummy_node.next
