class Solution {
    var nextRight: TreeNode? = nil
    
    func flatten(_ root: TreeNode?) {
        
        guard root != nil else {
            return
        }
        
        flatten(root?.right)
        flatten(root?.left)
        
        root?.right = nextRight
        root?.left = nil
        nextRight = root
    }
}
