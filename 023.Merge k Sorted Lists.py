# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        
        root = None
        index = 0
        while root == None:
            root = lists[index]
            index += 1

        while index < len(lists):
            index += 1
            ptr_root = root
            ptr_cur = lists[index]
            
            temp = ptr_cur
            while ptr_cur.val > ptr_root.val:
                temp = ptr_cur
                ptr_cur = ptr_cur.next
            
            
            while ptr_cur != None:
                if ptr_root.next == None:
                    ptr_root.next = ptr_cur
                    break
                if ptr_root_next.val > ptr_cur.val:
                    temp = ptr_root.next
                    temp2 = ptr_cur.next
                    ptr_root.next = ptr_cur
                    ptr_cur.next = temp
                    ptr_cur = temp2
                    ptr_root = ptr_root.next
                else:
                  pass
                ptr_cur = ptr_cur.next
                    
                    

        return root
