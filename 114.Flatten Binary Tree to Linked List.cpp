/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    void flatten(TreeNode* root) {
        if (root == NULL)
            return;
        
        helper(root);
    }
    
    TreeNode* helper(TreeNode* current) {
        if (current == NULL)
            return NULL;
            TreeNode* left = helper(current->left);
            TreeNode* right = helper(current->right);
            
            if (left != NULL) {
                left->right = current->right;
                current->right = current->left;
                current->left = NULL;
            }
            
            if (right != NULL) {
                return right;
            }
            
            if (left != NULL) {
                return left;
            }
            
            return current;
    }
};
