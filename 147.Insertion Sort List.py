# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        cur = head
        while cur.next:
            if cur.val > cur.next.val:
                target = cur.next
                cur.next = target.next
                if target.val < head.val:
                    target.next = head
                    head = target
                else:
                    ptr = head
                    while ptr.next:
                        if target.val < ptr.next.val:
                            target.next = ptr.next
                            ptr.next = target
                            break
                        ptr = ptr.next
            else:
                cur = cur.next
        return head
