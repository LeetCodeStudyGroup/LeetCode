# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cnt = 0
        tmp = head
        while tmp:
            tmp = tmp.next
            cnt += 1
        if cnt == 0:
            return head
        k %= cnt
        if k == 0:
            return head

        ptr1 = ptr2 = head
        while k > 0:
            if ptr1 == None:
                ptr1 = head
            ptr1 = ptr1.next
            k -= 1
        while ptr1.next != None:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        tmp = ptr2.next
        ptr2.next = None
        ptr1.next = head
        head = tmp
        return head
