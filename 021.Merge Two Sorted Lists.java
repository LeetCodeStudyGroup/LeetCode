/*
Merge two sorted linked lists and return it as a new list.

The new list should be made by splicing together the nodes of the first two lists.
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
        ListNode(int x) {
            val = x;
        }
    }

    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;

        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                current.next = l1;
                current = current.next;
                l1 = l1.next;
            } else {
                current.next = l2;
                current = current.next;
                l2 = l2.next;
            }
        }

        while (l1 != null) {
            current.next = l1;
            current = current.next;
            l1 = l1.next;
        }

        while (l2 != null) {
            current.next = l2;
            current = current.next;
            l2 = l2.next;
        }

        return dummy.next;
    }
