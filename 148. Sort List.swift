class Solution {
    func sortList(_ head: ListNode?) -> ListNode? {
        
        if head == nil || head?.next == nil {
            return head
        }
        
        // find mid
        let mid = findMid(head)
        var rightSort = sortList(mid?.next)
        mid?.next = nil
        
        var leftSort = sortList(head)
        
        // merge
        let resultHead = mergeSort(&leftSort, &rightSort)
        
        return resultHead
    }
    
    func findMid(_ head: ListNode?) -> ListNode? {
        
        if head == nil {
            return head
        }
        
        var slow = head
        var fast = head!.next
        
        while fast != nil && fast!.next != nil {
            slow = slow!.next
            fast = fast!.next!.next
        }
        
        return slow
    }


    func mergeSort(_ left: inout ListNode?, _ right: inout ListNode?) -> ListNode? {
        let head = ListNode(0)
        var tail: ListNode? = head
        
        while left != nil && right != nil {
            if left!.val < right!.val {
                tail?.next = left
                tail = tail?.next
                left = left?.next
            } else {
                tail?.next = right
                tail = tail?.next
                right = right?.next
            }
        }
        
        if left != nil {
            tail?.next = left
        }
        
        if right != nil {
            tail?.next = right
        }
        
        return head.next
    }

}
