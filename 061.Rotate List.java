 /*
    Given a list, rotate the list to the right by k places, where k is non-negative.

    For example:
    Given 1->2->3->4->5->NULL and k = 2,
    return 4->5->1->2->3->NULL.
     */
    /**
     * Definition for singly-linked list.
     * public class ListNode {
     *     int val;
     *     ListNode next;
     *     ListNode(int x) { val = x; }
     * }
     */
    public ListNode rotateRight(ListNode head, int k) {
        if(head == null)
            return head;

        int count = 1;
        ListNode dummy = new ListNode(0);
        ListNode tail = head;

        while (tail.next != null) {
            count++;
            tail = tail.next;
        }

        tail.next = head;

        k %= count;
        if (k != 0) {
            for (int i=0; i<count-k; i++) {
                tail = tail.next;
            }
        }

        dummy.next = tail.next;
        tail.next = null;
        return dummy.next;
    }
