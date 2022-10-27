// Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

// Example 1:
// Input: root = [3,9,20,null,null,15,7]
// Output: [[3],[9,20],[15,7]]
// Example 2:
// Input: root = [1]
// Output: [[1]]
// Example 3:
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
    List<List<Integer>> results = new ArrayList<>();
    public List<List<Integer>> levelOrder(TreeNode root) {
        if (root == null)
            return results;
        results.add(Arrays.asList(root.val));
        findLevelOrder(root, 1);
        
        
        return results;
    }
    
    void findLevelOrder(TreeNode node, int level) {
        if (node.left != null) {
            if (results.size() < level + 1)
                results.add(new ArrayList<>());
            results.get(level).add(node.left.val);
            findLevelOrder(node.left, level + 1);
        }
        if (node.right != null) {
            if (results.size() < level + 1)
                results.add(new ArrayList<>());
            results.get(level).add(node.right.val);
            findLevelOrder(node.right, level + 1);
        }
    }
}
