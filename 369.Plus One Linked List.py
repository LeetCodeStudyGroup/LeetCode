# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None

        dummy = ListNode(0)
        dummy.next = head
        self.twopoint(dummy)
        #self.helper(dummy)
        return dummy if dummy.val > 0 else dummy.next

    def twopoint(self, head):
        i, j = head, head
        while j.next != None:
            j = j.next
            if j.val != 9:
                i = j

        i.val += 1
        while i.next != None:
            i = i.next
            i.val = 0

    def helper(self, head):
        head.val += self.helper(head.next) if head.next else 1
        carry = head.val / 10
        head.val %= 10
        return carry
