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

// traverse
class Solution {
    var result = [Int]()
    
    func inorderTraversal(_ root: TreeNode?) -> [Int] {
        helper(root)
        return result
    }
    
    // 定義： add root 至 result
    func helper(_ root: TreeNode?) {
        
        // 出口
        guard let node = root else {
            return
        }
        
        // 分析
        helper(node.left)
        result.append(node.val)
        helper(node.right)
    }
}


// devide and conquer
class Solution_2 {
    func inorderTraversal(_ root: TreeNode?) -> [Int] {
       return helper(root)
    }
    
    // 定義：返回一個 以 root 為 inorder 的數組
    func helper(_ root: TreeNode?) -> [Int] {
      
        // 出口
        guard let node = root else {
            return []
        }
        
        // devide, conquer, merge
        let left = helper(node.left)
        let right = helper(node.right)
        
        var result = [Int]()
        result.append(contentsOf: left)
        result.append(node.val)
        result.append(contentsOf: right)
        
        return result
    }
}
