class Solution {
    // <key=sum, value=times>
    var map = Dictionary<Int, Int>()
    
    func findFrequentTreeSum(_ root: TreeNode?) -> [Int] {
        
        let _ = sumOfTree(root)
        
        var result = [Int]()
        
        var maxTimes = Int.min
        for item in map {
            let thisTimes = item.value
            if thisTimes > maxTimes {
                maxTimes = thisTimes
                result.removeAll()
                result.append(item.key)
            } else if thisTimes == maxTimes {
                result.append(item.key)
            }
        }

        return result
    }
    
    func sumOfTree(_ root: TreeNode?) -> Int {
        if root == nil {
            return 0
        }
        
        //sum of left, right
        let sum = (root?.val)! + sumOfTree(root?.left) + sumOfTree(root?.right)
        
        //add sum into sums
        putMap(sum)
        
        return sum
    }
    
    func putMap(_ sum: Int) {
        //add sum into sums
        if let val = map[sum] {
            map[sum] = val + 1
        } else {
            map[sum] = 1
        }
    }
}
