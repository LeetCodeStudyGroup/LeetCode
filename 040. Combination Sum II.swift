class Solution {
    func combinationSum2(_ candidates: [Int], _ target: Int) -> [[Int]] {
        
        var results = [[Int]]()
        dfsToGetResults(candidates.sorted(), [], 0, target, &results)
        
        return results
    }
    
    // 定義：找出以 combination 為 root 的 所有results
    private func dfsToGetResults(_ candidates: [Int], _ root: [Int], _ startIndex: Int, _ target: Int, _ results: inout [[Int]]) {
        // 出口
        if root.reduce(0, +) == target {
            results.append(root)
            return
        }
        
        // 拆解
        for index in startIndex ..< candidates.count {
            
            if index != startIndex && candidates[index] == candidates[index-1]  {
                continue
            }
            
            if root.reduce(0, +) + candidates[index] > target {
                return
            }
            
            var nextRoot = root
            nextRoot.append(candidates[index])
            dfsToGetResults(candidates, nextRoot, index+1, target, &results)
        }
    }
}
