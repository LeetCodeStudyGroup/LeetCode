/**
     * 98. Validate Binary Search Tree
     * Medium
     *
     * Companies
     * Given the root of a binary tree, determine if it is a valid binary search tree (BST).
     *
     * A valid BST is defined as follows:
     *
     * The left subtree of a node contains only nodes with keys less than the node's key.
     * The right subtree of a node contains only nodes with keys greater than the node's key.
     * Both the left and right subtrees must also be binary search trees.
     *
     *
     * Example 1:
     *
     *
     * Input: root = [2,1,3]
     * Output: true
     * Example 2:
     *
     *
     * Input: root = [5,1,4,null,null,3,6]
     * Output: false
     * Explanation: The root node's value is 5 but its right child's value is 4.
     *
     *
     * Constraints:
     *
     * The number of nodes in the tree is in the range [1, 104].
     * -231 <= Node.val <= 231 - 1
     */

    List<Integer> list = new ArrayList<>();
    public boolean isValidBST(TreeNode root) {
        if (root == null) return true;
        findBST(root);
        int previous = list.get(0);
        for (int i = 1; i < list.size(); i++) {
            if (previous >= list.get(i)) return false;
            previous = list.get(i);
        }

        return true;
    }

    public void findBST(TreeNode node) {
        if (node == null)
            return;
        findBST(node.left);
        list.add(node.val);
        findBST(node.right);
    }
