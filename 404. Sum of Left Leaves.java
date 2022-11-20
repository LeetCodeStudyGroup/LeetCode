/**
Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
Example 2:

Input: root = [1]
Output: 0
*/

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
    public int sumOfLeftLeaves(TreeNode root) {
        if (root == null)
            return 0;
        
        return sum(root, false);
    }
    
    int sum(TreeNode node, boolean isLeft) {
        if (node.left == null && node.right == null && isLeft) return node.val;
        if (node.left != null && node.right != null) 
            return sum(node.left, true) + sum(node.right, false);
        if (node.left != null)
            return sum(node.left, true);
        if (node.right != null)
            return sum(node.right, false);
        
        return 0;
    }
}
