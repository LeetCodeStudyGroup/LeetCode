/**
     * Given an integer n, return all the structurally unique BST's (binary search trees),
     * which has exactly n nodes of unique values from 1 to n. Return the answer in any order.
     *
     * Example 1:
     * Input: n = 3
     * Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
     *
     *
     * Example 2:
     * Input: n = 1
     * Output: [[1]]
     */
    public List<TreeNode> generateTrees(int n) {

        if(n == 0) {
            return null;
        }

        return solve(1 ,n);
    }

    public List<TreeNode> solve(int start ,int end) {
        if (start > end) {
            ArrayList<TreeNode> al = new ArrayList();
            al.add(null);
            return al;
        }

        List<TreeNode> treeList = new ArrayList();
        for (int current = start; current <= end; current++) {
            List<TreeNode> leftTrees = solve(start ,current-1);
            List<TreeNode> rightTrees = solve(current+1 ,end);

            for (int l=0; l<leftTrees.size(); l++) {
                for (int r=0; r<rightTrees.size(); r++) {
                    TreeNode node = new TreeNode(current);
                    node.left = leftTrees.get(l);
                    node.right = rightTrees.get(r);
                    treeList.add(node);
                }
            }
        }
        return treeList;
    }
