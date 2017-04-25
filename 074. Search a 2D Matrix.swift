class Solution {
    func searchMatrix(_ matrix: [[Int]], _ target: Int) -> Bool {
        
        guard matrix.count != 0 && matrix[0].count != 0 else {
            return false
        }
        
        let possibleIndex = firstIndexSearch(matrix, target)
        let possibleList = matrix[possibleIndex]
        
        // 請利用 binary search 實作
        return possibleList.contains(target)
    }
    
    func firstIndexSearch(_ matrix: [[Int]], _ target: Int) -> Int{
        
        var frontIndex = 0
        var rearIndex = matrix.count - 1
        
        while frontIndex <= rearIndex {
            
            if frontIndex == rearIndex {
                return frontIndex
            }
            
            let searchIndex = (frontIndex + rearIndex) / 2

            if matrix[searchIndex].first == target{
                return searchIndex
            } else if matrix[searchIndex].first! < target {
                if matrix[searchIndex].last! < target {
                    frontIndex = searchIndex + 1
                } else {
                    return searchIndex
                }
                
            } else {
                rearIndex = searchIndex - 1
            }
        }
        
        return 0
    }
}
