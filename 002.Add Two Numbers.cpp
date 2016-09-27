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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head, *dummy, *result;
        head = dummy = result = new ListNode(0);
        int carry = 0;
        if(l1 == NULL || l2 == NULL)
            return result;
            
        while(l1 != NULL || l2 != NULL) {
            int sum = 0;
            if (l1 != NULL && l2 != NULL) {
                sum = l1->val + l2->val + carry;
                l1 = l1->next;
                l2 = l2->next;
            }
            else if(l1 != NULL) {
                sum = l1->val + carry;
                l1 = l1->next;
            }
            else {
                sum = l2->val + carry;
                l2 = l2->next;
            }
            carry = sum / 10;
            result->next = new ListNode(sum % 10);
            result = result->next;
        }
        
        if(carry != 0)
            result->next = new ListNode(carry);
        
        head = dummy->next;
        delete dummy;
        
        return head;
    }
};
