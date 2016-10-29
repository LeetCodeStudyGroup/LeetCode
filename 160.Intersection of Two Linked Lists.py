# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import gc

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        hA, hB = headA, headB
        nodeA, nodeB = headA, headB
        while nodeA and nodeB:
            if nodeA == nodeB:
                return nodeA
            nodeA = nodeA.next
            nodeB = nodeB.next
        if not nodeB:
            hA, hB = headB, headA
            nodeA, nodeB = nodeB, nodeA
        nodeA = hB
        gc.collect()
        while nodeB:
            nodeA = nodeA.next
            nodeB = nodeB.next
        nodeB = hA
        while nodeA and nodeB:
            if nodeA == nodeB:
                return nodeA
            nodeA = nodeA.next
            nodeB = nodeB.next
        return None
