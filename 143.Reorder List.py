# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        cnt = 0
        tmp = head
        while tmp:
            cnt += 1
            tmp= tmp.next
        if cnt <= 2:
            return

        cnt = (cnt + 1) / 2 - 1
        tmp = head
        while cnt > 0:
            cnt -= 1
            tmp= tmp.next
        if tmp == None:
            return
        half = tmp.next
        tmp.next = None

        last = dummy = ListNode(0)
        ptr = dummy.next = half
        while ptr.next:
            t = ptr.next
            ptr.next = last
            last = ptr
            ptr = t
        ptr.next = last
        half.next = None

        p1 = head
        p2 = ptr
        ptr = dummy
        while p1 and p2:
            ptr.next = p1
            p1 = p1.next
            ptr.next.next = p2
            p2 = p2.next
            ptr = ptr.next.next
        ptr.next = p1
