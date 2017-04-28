class Solution {
    var isBalancedBool = true
    
    func isBalanced(_ root: TreeNode?) -> Bool {
        guard root != nil else {
            return true
        }
        
        let _ = helper(root)
        return isBalancedBool
    }
    
    func helper(_ root: TreeNode?) -> Int {
        
        if !isBalancedBool {
            return -1
        }

        var leftDepth = 0
        if root?.left != nil {
            leftDepth = helper(root?.left)
        }
        
        var rightDepth = 0
        if root?.right != nil {
            rightDepth = helper(root?.right)
        }
        
        if isBalancedBool {
            isBalancedBool = isBalancedTree(leftDepth, rightDepth)
            // 1 is this node
            return 1 + max(leftDepth, rightDepth)
            
        } else {
            return -1
        }
    }
    
    func isBalancedTree(_ leftDepth: Int, _ rightDepth: Int) -> Bool {
        let result = leftDepth - rightDepth
        return (result >= -1 && result <= 1)
    }
}
