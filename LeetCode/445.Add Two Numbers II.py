# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_len, l2_len = self.get_len(l1), self.get_len(l2)
        if l2_len > l1_len:
            l1, l2, l1_len, l2_len = l2, l1, l2_len, l1_len

        sum_list = ListNode(0)
        ptr_sum, ptr_l1, ptr_l2 = sum_list, l1, l2
        for _ in range(l1_len - l2_len):
            ptr_sum.next = ListNode(ptr_l1.val)
            ptr_sum, ptr_l1 = ptr_sum.next, ptr_l1.next

        for _ in range(l2_len):
            ptr_sum.next = ListNode(ptr_l1.val + ptr_l2.val)
            ptr_sum, ptr_l1, ptr_l2 = ptr_sum.next, ptr_l1.next, ptr_l2.next

        self.add_carry(sum_list)
        return sum_list if sum_list.val > 0 else sum_list.next

    def add_carry(self, node):
        if node.next:
            node.val += self.add_carry(node.next)
        carry = 0
        if node.val >= 10:
            carry, node.val = 1, node.val % 10
        return carry

    def get_len(self, ptr):
        cnt = 0
        while ptr:
            ptr, cnt = ptr.next, cnt + 1
        return cnt
