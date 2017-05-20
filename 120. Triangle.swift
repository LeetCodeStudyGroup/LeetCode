class Solution {
    func minimumTotal(_ triangle: [[Int]]) -> Int {
        var preSumList = [Int]()
        var curSumList = [Int]()
        
        for i in 0 ..< triangle.count {
            curSumList = [Int]()
            
            for j in 0 ..< triangle[i].count {
                let curSum = triangle[i][j] + minPreSum(j, preSumList)
                curSumList.append(curSum)
            }
            
            preSumList = curSumList
        }
        
        var minSum = Int.max
        for sum in curSumList {
            minSum = min(minSum, sum)
        }
        
        return minSum
    }
    
    private func minPreSum(_ cur: Int, _ preSumList: [Int]) -> Int {
        
        if preSumList.count == 0 {
            return 0
        }
        
        var preIndexSum = Int.max
        var curIndexSum = Int.max
        
        // pre index
        if cur - 1 >= 0 {
            preIndexSum = preSumList[cur - 1]
        }
        
        if cur < preSumList.count {
            curIndexSum = preSumList[cur]
        }
        
        return min(preIndexSum, curIndexSum)
    }
}
