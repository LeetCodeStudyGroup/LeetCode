class Solution {

    func permute(_ nums: [Int]) -> [[Int]] {
        var results = [[Int]]()
        dfsForPermutations([], nums.sorted(), &results)
        return results
    }
    
    // 找出以 root 為起始，input 為 待輸入 的排列組合
    private func dfsForPermutations(_ root: [Int], _ unarrange: [Int], _ results: inout [[Int]]) {
        
        // 出口
        if unarrange.count == 0 {
            results.append(root)
        }
        
        // 解析
        var tempUnarrange = unarrange
        for index in 0 ..< tempUnarrange.count {
            let item = tempUnarrange[index]
            var nextRoot = root
            nextRoot.append(item)
            
            tempUnarrange.remove(at: index)
            dfsForPermutations(nextRoot, tempUnarrange, &results)
            tempUnarrange.insert(item, at: index)
        }
    }
}
