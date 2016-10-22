/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int count = 0;
        int point;
        ListNode* temp = head;
        while (temp != NULL) {
            temp = temp->next;
            count++;
        }
        
        if (count < n) {
            return NULL;
        } else if (count == n) {
            head = head->next;
            return head;
        }
        
        temp = head;
        point = count - n - 1;
        for (int i = 0; i < point; i++) {
            temp = temp->next;
        }
        
        ListNode* tempNode = temp->next;
        ListNode* nextNode = tempNode->next;
        
        delete tempNode;
        
        temp->next = nextNode;
        
        return head;
    }
};
