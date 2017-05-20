// felix - top to down
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


// leetcode - down to top
class Solution2 {
    func minimumTotal(_ triangle: [[Int]]) -> Int {
        var sunList = Array(repeating:Int.max, count: triangle.count)
        
        for i in stride(from: triangle.count - 1, to: -1, by: -1){
            print(i)
            for j in 0 ..< triangle[i].count {
                if i == triangle.count - 1 {
                    sunList[j] = triangle[i][j]
                } else {
                    sunList[j] = triangle[i][j] + minPreSum(j, sunList)
                }
            }
        }
        
        return sunList[0]
    }
    
    private func minPreSum(_ cur: Int, _ list: [Int]) -> Int {
        if list.count == 0 {
            return 0
        }
        
        var curIndexSum = Int.max
        var nextIndexSum = Int.max

        curIndexSum = list[cur]
        
        if cur + 1 < list.count {
            nextIndexSum = list[cur + 1]
        }
        
        return min(curIndexSum, nextIndexSum)
    }
}
