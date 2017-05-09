class Solution {
    func mergeTwoLists(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
        
        if l1 == nil && l2 == nil {
            return nil
        }
        
        guard let list_1 = l1 else {
            return l2
        }
        
        guard let list_2 = l2 else {
            return l1
        }

        if list_1.val < list_2.val {
            list_1.next = mergeTwoLists(list_1.next, list_2)
            return list_1
        } else  {
            list_2.next = mergeTwoLists(list_1, list_2.next)
            return list_2
        }
    }
}
