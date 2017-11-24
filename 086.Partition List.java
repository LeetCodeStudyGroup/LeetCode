 /*
    Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

    You should preserve the original relative order of the nodes in each of the two partitions.

    For example,
    Given 1->4->3->2->5->2 and x = 3,
    return 1->2->2->4->3->5.
     */

    /**
     * Definition for singly-linked list.
     * public class ListNode {
     *     int val;
     *     ListNode next;
     *     ListNode(int x) { val = x; }
     * }
     */

    public ListNode partition(ListNode head, int x) {
        ListNode smallNode = new ListNode(0);
        ListNode smallHead = smallNode;
        ListNode largeNode = new ListNode(0);
        ListNode largeHead = largeNode;
        while (head != null) {
            if (head.val >= x) {
                largeNode.next = head;
                largeNode = largeNode.next;
            } else {
                smallNode.next = head;
                smallNode = smallNode.next;
            }
            head = head.next;
        }

        smallNode.next = largeHead.next;
        largeNode.next = null;

        return smallHead.next;
    }
