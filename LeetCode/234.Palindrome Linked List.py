# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: return True
        last = None
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            nxt, slow.next = slow.next, last
            last, slow = slow, nxt
        if fast:
            slow = slow.next
        while slow and last:
            if slow.val != last.val:
                return False
            slow = slow.next
            last = last.next
        return True

    def isPalindrome2(self, head):
        ptr, cnt = head, 0
        while ptr:
            cnt += 1
            ptr = ptr.next
        if cnt <= 1:
            return True
        head1, head2 = self.reverse(head, cnt)
        while head1 and head2:
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next
        return True

    def reverse(self, head, cnt):
        last = dummy = ListNode(0)
        ptr = dummy.next = head
        k = cnt / 2
        while k > 0:
            nxt, ptr.next = ptr.next, last
            last, ptr = ptr, nxt
            k -= 1
        head.next = None
        if cnt % 2 == 1:
            ptr = ptr.next
        return last, ptr
