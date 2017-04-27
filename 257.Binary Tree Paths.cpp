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
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> result;
        
        if (root != NULL)
            findPath(result, root, "");
            
        return result;
    }
    
    void findPath(vector<string> &result, TreeNode* current, string path) {
        // int to string
        stringstream ss;
        ss << current->val;
        if (path != "")
            path = path + "->" + ss.str();
        else
            path = ss.str();
        
        if (current->left != NULL || current->right != NULL) {
            if (current->left != NULL) {
                findPath(result, current->left, path);
            }
            if (current->right != NULL) {
                findPath(result, current->right, path);
            }
        } else {
            result.push_back(path);
        }
    }
};
