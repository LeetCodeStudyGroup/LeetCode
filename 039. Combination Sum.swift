class Solution {
    func combinationSum(_ candidates: [Int], _ target: Int) -> [[Int]] {
        
        // 排序 + 消除重複
        let trimCandidates = removeDuplicates(candidates)
        
        // 定義：找出以 combination 為 root 的 所有results
        var results = [[Int]]()
        dfsToGetResults(trimCandidates, [], 0, target, &results)

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
            
            if root.reduce(0, +) + candidates[index] > target {
                return
            }
            
            var nextRoot = root
            nextRoot.append(candidates[index])
            dfsToGetResults(candidates, nextRoot, index, target, &results)
        }
    }
    
    
    private func removeDuplicates(_ candidates: [Int]) -> [Int] {
        var result = [Int]()
        
        for item in candidates.sorted() {
            if result.last != item {
                result.append(item)
            }
        }
        return result
    }
}
