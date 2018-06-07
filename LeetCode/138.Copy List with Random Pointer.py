# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        ptr = head
        while ptr:
            tmp = ptr.next
            node = RandomListNode(ptr.label)
            ptr.next = node
            node.next = tmp
            ptr = tmp

        ptr = head
        while ptr:
            if ptr.random:
                ptr.next.random = ptr.random.next
            ptr = ptr.next.next

        dummy = RandomListNode(0)
        ptr, ptr2 = head, dummy
        while ptr:
            ptr2.next = ptr.next
            ptr.next = ptr.next.next
            ptr = ptr.next
            ptr2 = ptr2.next
        
        return dummy.next
