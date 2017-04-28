class Solution {
    var paths = [[Int]]()
    
    func binaryTreePaths(_ root: TreeNode?) -> [String] {

        guard let node = root else {
            return []
        }
        
        helper(root, path: [])
        
        return pathsToString(paths)
    }
    
    func helper(_ root: TreeNode?, path: [Int]) {
        
        guard let node = root else {
            return
        }
        
        // record the path of the root to this node
        var newPath = path
        newPath.append(node.val)
        
        // add paths
        if node.left == nil && node.right == nil {
            paths.append(newPath)
            return
        }
        
        // 左子樹
        if root?.left != nil {
            helper(node.left, path: newPath)
        }
        
        // 右子樹
        if root?.right != nil {
            helper(node.right, path: newPath)
        }
    }
    
    func pathsToString(_ paths: [[Int]]) -> [String] {
        var stringPaths = [String]()
        
        for path in paths {
            
            var stringPath = ""
            for index in path.startIndex ..< path.endIndex {
                if index == path.startIndex {
                    stringPath = String(path[index])
                } else {
                    stringPath = stringPath + "->" + String(path[index])
                }
            }
            stringPaths.append(stringPath)
        }
        
        return stringPaths
    }
}
