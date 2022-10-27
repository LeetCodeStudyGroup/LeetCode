// Given the root of a binary tree, return the preorder traversal of its nodes' values.
// Example 1:
// Input: root = [1,null,2,3]
// Output: [1,2,3]
// Example 2:
// Input: root = []
// Output: []

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    List<Integer> result = new ArrayList<>();
    public List<Integer> preorderTraversal(TreeNode root) {
        if (root != null) {
            preorder(root);
        }
        
        return result;
    }
    
    void preorder(TreeNode node) {
        if (node != null) {
            result.add(node.val);
            preorder(node.left);
            preorder(node.right);
        }
    }
}
