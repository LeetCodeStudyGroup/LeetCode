/*
    Reverse a linked list from position m to n. Do it in-place and in one-pass.

    For example:
    Given 1->2->3->4->5->NULL, m = 2 and n = 4,

    return 1->4->3->2->5->NULL.

    Note:
    Given m, n satisfy the following condition:
    1 ≤ m ≤ n ≤ length of list.
    */

    /**
     * Definition for singly-linked list.
     * public class ListNode {
     *     int val;
     *     ListNode next;
     *     ListNode(int x) { val = x; }
     * }
     */

    public ListNode reverseBetween(ListNode head, int m, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode firstPoint = dummy, endPoint = dummy;
        if (head == null || m == n)
            return head;
        for (int i=0; i<=n; i++) {
            if (i == m-1)
                firstPoint = endPoint;
            endPoint = endPoint.next;
        }
        ListNode one = firstPoint.next;
        ListNode two = one.next;
        ListNode three;
        ListNode end = firstPoint.next;
        while (two != null && two != endPoint) {
            three = two.next;
            two.next = one;
            one = two;
            two = three;
        }
        firstPoint.next.next = endPoint;
        firstPoint.next = one;

        return dummy.next;
    }
