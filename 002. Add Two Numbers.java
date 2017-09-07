//    You are given two non-empty linked lists representing two non-negative integers.
//    The digits are stored in reverse order and each of their nodes contain a single digit.
//    Add the two numbers and return it as a linked list.
//
//    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
//
//    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
//    Output: 7 -> 0 -> 8

    /**
     * Definition for singly-linked list.
     * public class ListNode {
     *     int val;
     *     ListNode next;
     *     ListNode(int x) { val = x; }
     * }
     */

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode next = head;
        int carry = 0;

        while (l1 != null || l2 != null || carry != 0) {
            int result = ((l1 != null) ?l1.val : 0) + ((l2 != null) ?l2.val : 0) + carry;
            carry = result / 10;
            next.next = new ListNode(result % 10);
            next = next.next;
            l1 = (l1 != null) ? l1.next : l1;
            l2 = (l2 != null) ? l2.next : l2;
        }

        return head.next;
    }
