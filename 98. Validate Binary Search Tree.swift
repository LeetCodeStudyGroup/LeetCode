class Solution {
    func isValidBST(_ root: TreeNode?) -> Bool {
        
        if root == nil {
            return true
        }
        
        return helper(root, minVal: Int.min, maxVal: Int.max)
    }
    
    func helper(_ root: TreeNode?, minVal: Int, maxVal: Int) -> Bool {
        guard let node = root else {
            return true
        }
        
        if node.val <= minVal || node.val >= maxVal {
            return false
        }

        return helper(node.left, minVal: minVal, maxVal: node.val) && helper(node.right, minVal: node.val, maxVal: maxVal)
    }
}
