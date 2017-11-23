/*
    Given a sorted linked list, delete all duplicates such that each element appear only once.

    For example,
    Given 1->1->2, return 1->2.
    Given 1->1->2->3->3, return 1->2->3.
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

        while (two.next != null) {
            if (one.next.val == two.next.val) {
                one.next = two.next;
                two = two.next;
            } else {
                one = one.next;
                two = two.next;
            }
        }

        return dummy.next;
    }
