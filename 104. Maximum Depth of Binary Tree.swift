public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?
    public init(_ val: Int) {
        self.val = val
        self.left = nil
        self.right = nil
    }
}

class Solution {
    var maxdepth = 0
    
    func maxDepth(_ root: TreeNode?) -> Int {
        helper(root, depthLevel: 0)
        return maxdepth
    }
    
    func helper(_ root: TreeNode?, depthLevel: Int) {
        
        guard let node = root else {
            return
        }
        
        let currentLevel = depthLevel + 1
        
        if node.left == nil && node.right == nil {
            maxdepth = max(maxdepth, currentLevel)
            return
        }
        
        if node.left != nil {
            helper(node.left, depthLevel: currentLevel)
        }
        
        if node.right != nil {
            helper(node.right, depthLevel: currentLevel)
        }
    }
}
