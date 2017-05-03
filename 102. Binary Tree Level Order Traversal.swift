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

// 1. 取得 root 的子樹 加入 queue

// 2. 取出 queue 的每個元素，將 他們的子節點 加入另一個新的 queue中； 此新的queue就是 一層 的所有節點
// 2-1. while old queue != nil, 取出 queue.first
// 2-2. 將 queue.first (新的子樹) 加入 new queue
// 2-3. util  new queue is empty
class Solution {
    var result: [[Int]] = []
    
    func levelOrder(_ root: TreeNode?) -> [[Int]] {

        guard let node = root else {
            return []
        }
        
        var queue = Queue<TreeNode>()
        queue.enqueue(node)
        helper(queue)
        
        return result
    }
    
    func helper(_ queue: Queue<TreeNode>) {
        var addElement = [Int]()
        var newQueue = Queue<TreeNode>()
        
        var myQueue = queue
        while !myQueue.isEmpty {
            if let node = myQueue.dequeue() {
                // add val to result
                addElement.append(node.val)
                
                // add left, right node
                if node.left != nil {
                    newQueue.enqueue(node.left!)
                }
                
                if node.right != nil {
                    newQueue.enqueue(node.right!)
                }
            }
        }
        
        result.append(addElement)

        // 出口
        if newQueue.count > 0 {
            helper(newQueue)
        }
    }
}

public struct Queue<T> {
    fileprivate var array = [T]()
    
    public var isEmpty: Bool {
        return array.isEmpty
    }
    
    public var count: Int {
        return array.count
    }
    
    public mutating func enqueue(_ element: T) {
        array.append(element)
    }
    
    public mutating func dequeue() -> T? {
        if isEmpty {
            return nil
        } else {
            return array.removeFirst()
        }
    }
    
    public var front: T? {
        return array.first
    }
}
