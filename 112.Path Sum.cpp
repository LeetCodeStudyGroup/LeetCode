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
    bool hasPathSum(TreeNode* root, int sum) {
        if (root == NULL)
            return false;
            
        if (root->left == NULL && root->right == NULL &&root->val - sum == 0)
            return true;
        
        if (root->left != NULL && root->right != NULL)
            return hasPathSum(root->left, sum - root->val) || hasPathSum(root->right, sum - root->val);
        
        if (root->left != NULL)
            return hasPathSum(root->left, sum - root->val);
            
        if (root->right != NULL)
            return hasPathSum(root->right, sum - root->val);
            
        return false;
    }
};
// ==============================================================================
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
    bool checkSum(TreeNode* node, int current, int sum) {
        if (node == NULL) {
            if (current == sum)
                return true;
            else
                return false;
        }
        
        int currentSum = current + node->val;
        
        if (node->left != NULL && node->right != NULL)
            return checkSum(node->left, currentSum, sum) || checkSum(node->right, currentSum, sum);
        else if (node->right != NULL)
            return checkSum(node->right, currentSum, sum);
        else
            return checkSum(node->left, currentSum, sum);
    }
    
    bool hasPathSum(TreeNode* root, int sum) {
        if (root == NULL)
            return false;
        
        return checkSum(root, 0, sum);
    }
};
