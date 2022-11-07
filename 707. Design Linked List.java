/**
707. Design Linked List
Medium

1875

1329

Add to List

Share
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

*/

class MyLinkedList {
    class Node {
        int val;
        Node next;
        public Node(int val) {
            this.val = val;
        }
    }
    private Node head;
    private int size;
    
    public MyLinkedList() {
        head = new Node(0);
        size = 0;
    }
    
    public int get(int index) {
        if (index >= size)
            return -1;
        
        Node point = head;
        for (int i=0; i<index; i++) {
            point = point.next;
        }
        
        return point.next.val;
    }
    
    public void addAtHead(int val) {
        Node point = new Node(val);
        point.next = head.next;
        head.next = point;
        size++;
    }
    
    public void addAtTail(int val) {
        Node point = head;
        while(point.next != null) {
            point = point.next;
        }
        Node temp = new Node(val);
        point.next = temp;
        size++;
    }
    
    public void addAtIndex(int index, int val) {
        Node point = head;
        for (int i=0; i<index; i++) {
            if (point.next == null)
                return;
            point = point.next;
        }
        Node temp = new Node(val);
        temp.next = point.next;
        point.next = temp;
        size++;
    }
    
    public void deleteAtIndex(int index) {
        Node point = head;
        for (int i=0; i<index; i++) {
            point = point.next;
        }
        if (point != null && point.next != null) {
            point.next = point.next.next;
            size--;
        }
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */
