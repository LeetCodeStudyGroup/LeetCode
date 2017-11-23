/*
    Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

    For example,
    Given 1->2->3->3->4->4->5, return 1->2->5.
    Given 1->1->1->2->3, return 2->3.
     */

    /**
     * Definition for singly-linked list.
     * public class ListNode {
     *     int val;
     *     ListNode next;
     *     ListNode(int x) { val = x; }
     * }
     */

    public ListNode deleteDuplicates(ListNode head) {
        if (head == null || head.next == null)
            return head;
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode one = dummy;
        ListNode two = dummy.next;
        int now = head.val;
        while (two != null) {
            while(two.next != null && two.val == two.next.val){
                two = two.next;
            }
            if(one.next == two){
                one = one.next;
            } else {
                one.next = two.next;
            }
            two = two.next;
        }
        return dummy.next;
    }
