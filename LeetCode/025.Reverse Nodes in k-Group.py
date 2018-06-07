# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur = head
        for i in range(k):
            if cur == None:
                return head
            cur = cur.next
        last = self.reverseKGroup(cur, k)
        ptr = head
        for i in range(k):
            tmp = ptr.next
            ptr.next = last
            last = ptr
            ptr = tmp
        return last

    def reverseKGroup2(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        last, ptr = dummy, head
        while ptr:
            next_ptr = ptr
            for i in range(k):
                if next_ptr == None:
                    return dummy.next
                next_ptr = next_ptr.next
            new_head = self.reverse(ptr, next_ptr)
            last.next = new_head
            last = ptr
            ptr = next_ptr
        return dummy.next

    def reverse(self, head, end):
        dummy = ListNode(0)
        dummy.next = head
        last, ptr = dummy, head
        while ptr != end:
            tmp = ptr.next
            ptr.next = last
            last = ptr
            ptr = tmp
        head.next = end
        return last
