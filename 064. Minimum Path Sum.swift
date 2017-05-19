class Solution {
    func minPathSum(_ grid: [[Int]]) -> Int {
        let m = grid.count
        let n = grid[0].count
        var sumGrid = Array(repeating: Array(repeating: 0, count: n), count:m)
        
        sumGrid[0][0] = grid[0][0]
        
        for i in 1 ..< m {
            sumGrid[i][0] = sumGrid[i-1][0] + grid[i][0]
        }
        
        for j in 1 ..< n {
            sumGrid[0][j] = sumGrid[0][j-1] + grid[0][j]
        }
        
        for i in 1 ..< m {
            for j in 1 ..< n  {
                sumGrid[i][j] = min(sumGrid[i-1][j], sumGrid[i][j-1]) + grid[i][j]
            }
        }
        
        return sumGrid[m-1][n-1]
    }
}
