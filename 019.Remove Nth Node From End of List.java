/*
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
*/

    /**
     * Definition for singly-linked list.
     * public class ListNode {
     *     int val;
     *     ListNode next;
     *     ListNode(int x) { val = x; }
     * }
     */

    public class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }

    public ListNode removeNthFromEnd(ListNode head, int n) {
        int length = 1;
        ListNode current = head;

        if (head == null)
            return head;
        while (current.next != null) {
            current = current.next;
            length++;
        }

        if (n > length)
            return head;

        ListNode first = new ListNode(0);
        current = first;
        first.next = head;

        for (int i=length-n; i>0; i--) {
            current = current.next;
        }

        current.next = current.next.next;

        return first.next;
    }
