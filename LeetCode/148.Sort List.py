# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = head
        count = 0
        while tmp:
            count += 1
            tmp = tmp.next
        return self.mergesort(head, count)

    def mergesort(self, node, n):
        if n <= 1:
            return node
        cnt = n / 2
        tmp = node
        for i in range(cnt - 1):
            tmp = tmp.next
        node2 = tmp.next
        tmp.next = None
        node1 = self.mergesort(node, cnt)
        node2 = self.mergesort(node2, n - cnt)
        return self.merge(node1, node2)
        
    def merge(self, node1, node2):
        tmp = dummy = ListNode(0)
        p1 = node1
        p2 = node2
        while p1 and p2:
            if p1.val < p2.val:
                tmp.next = p1
                p1 = p1.next
            else:
                tmp.next = p2
                p2 = p2.next
            tmp = tmp.next
        while p1:
            tmp.next = p1
            tmp = tmp.next
            p1 = p1.next
        while p2:
            tmp.next = p2
            tmp = tmp.next
            p2 = p2.next
        tmp.next = None
        return dummy.next
        
    def quicksort(self, node):
        if node == None or node.next == None:
            return node
        small = large = None
        ptr_s = ptr_l = None
        tmp = node.next
        while tmp:
            n = tmp.next
            tmp.next = None
            if tmp.val > node.val:
                if large == None:
                    large = ptr_l = tmp
                else:
                    ptr_l.next = tmp
                    ptr_l = ptr_l.next
            else:
                if small == None:
                    small = ptr_s = tmp
                else:
                    ptr_s.next = tmp
                    ptr_s = ptr_s.next
            tmp = n
        tmp = dummy = ListNode(0)
        tmp.next = self.sort(small)
        while tmp.next:
            tmp = tmp.next
        tmp.next = node
        node.next = self.sort(large)
        return dummy.next
