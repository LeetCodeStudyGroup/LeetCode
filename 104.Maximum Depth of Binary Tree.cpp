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
    int maxDepth(TreeNode* root) {
        if (root == NULL)
            return 0;
        
        int left = maxDepth(root->left) + 1;
        int right = maxDepth(root->right) + 1;
        
        return max(left, right);
    }
};
// ========================================================================
class Solution {
public:
    int maxDepth(TreeNode* root) {
        queue<TreeNode*> q;
        int level = 0;
        if(root == NULL)
            return level;
        
        q.push(root);
        q.push(NULL);
        while (q.size() > 0) {
            TreeNode* node = q.front();
            q.pop();
            if (node == NULL) {
                if(q.size() > 0)
                    q.push(NULL);
                level++;
            } else {
                if (node->left != NULL)
                    q.push(node->left);
                if (node->right != NULL)
                    q.push(node->right);
            }
        }
        
        return level;
    }
};
