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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        while (l1 != NULL && l2 != NULL) {
            ListNode* temp = new ListNode(0);
            if (l1->val <= l2->val) {
                temp->val = l1->val;
                l1 = l1->next;
            } else {
                temp->val = l2->val;
                l2 = l2->next;
            }
            current->next = temp;
            current = current->next;
        }
        
        if (l1 != NULL) {
            current->next = l1;
        } else {
            current->next = l2;
        }
        
        return dummy->next;
    }
};

// ================== improve ========================

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        while (l1 != NULL && l2 != NULL) {
            if (l1->val <= l2->val) {
                current->next = l1;
                l1 = l1->next;
            } else {
                current->next = l2;
                l2 = l2->next;
            }
            current = current->next;
        }
        
        if (l1 != NULL) {
            current->next = l1;
        } else {
            current->next = l2;
        }
        
        return dummy->next;
    }
};
