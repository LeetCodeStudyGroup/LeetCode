 /**
     * 501. Find Mode in Binary Search Tree
     * Easy
     * Companies
     * Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.
     *
     * If the tree has more than one mode, return them in any order.
     *
     * Assume a BST is defined as follows:
     *
     * The left subtree of a node contains only nodes with keys less than or equal to the node's key.
     * The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
     * Both the left and right subtrees must also be binary search trees.
     *
     *
     * Example 1:
     * Input: root = [1,null,2,2]
     * Output: [2]
     * Example 2:
     * Input: root = [0]
     * Output: [0]
     */

    // Solution 1
    HashMap<Integer, Integer> duplicateCountMap = new HashMap<>();
    List<Integer> maxDuplicateList = new ArrayList<>();
    int duplicateCount = 0;
    public int[] findMode(TreeNode root) {
        if (root == null)
            return null;
        findDuplicate(root);

        int[] max = new int[maxDuplicateList.size()];
        for (int i = 0; i < maxDuplicateList.size(); i++)
            max[i] = maxDuplicateList.get(i);
        return max;
    }

    void findDuplicate(TreeNode root) {
        if (root != null) {
            int temp = duplicateCountMap.containsKey(root.val)? duplicateCountMap.get(root.val) + 1 : 1;
            if (temp > duplicateCount) {
                duplicateCount = temp;
                maxDuplicateList.clear();
                maxDuplicateList.add(root.val);
            } else if (temp == duplicateCount)
                maxDuplicateList.add(root.val);
            duplicateCountMap.put(root.val, temp);
            findDuplicate(root.left);
            findDuplicate(root.right);
        }
    }

    // Solution 2
    Integer prev = null;
    int count = 1;
    int max = 0;
    public int[] findMode(TreeNode root) {
        if (root == null) return new int[0];
        List<Integer> list = new ArrayList<>();
        traverse(root, list);

        int[] res = new int[list.size()];
        for (int i = 0; i < list.size(); ++i) res[i] = list.get(i);
        return res;
    }

    private void traverse(TreeNode root, List<Integer> list) {
        if (root == null) return;
        traverse(root.left, list);
        if (prev != null) {
            if (root.val == prev)
                count++;
            else
                count = 1;
        }
        if (count > max) {
            max = count;
            list.clear();
            list.add(root.val);
        } else if (count == max) {
            list.add(root.val);
        }
        prev = root.val;
        traverse(root.right, list);
    }
