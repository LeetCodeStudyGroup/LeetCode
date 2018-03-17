# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 is None and l2 is None:
            return None
        
        dummyNode = ListNode(-1)
        new_index = dummyNode
        l1_index = l1
        l2_index = l2
        
        while l1_index is not None and l2_index is not None:
            if l1_index.val <= l2_index.val:
                new_index.next = ListNode(l1_index.val)
                l1_index = l1_index.next
            else:
                new_index.next = ListNode(l2_index.val)
                l2_index = l2_index.next
        
            new_index = new_index.next
            
        while l1_index is not None:
            new_index.next = ListNode(l1_index.val)
            l1_index = l1_index.next
            new_index = new_index.next
            
            
        while l2_index is not None:
            new_index.next = ListNode(l2_index.val)
            l2_index = l2_index.next
            new_index = new_index.next
            
        return dummyNode.next
