class Solution {
    func uniquePathsWithObstacles(_ obstacleGrid: [[Int]]) -> Int {
        let m = obstacleGrid.count
        let n = obstacleGrid[0].count
        
        var map = Array(repeating: Array(repeating: 0, count: n), count: m)
        
        for i in 0 ..< m {
            if obstacleGrid[i][0] == 1 {
                break
            }
            map[i][0] = 1
        }
        
        for j in 0 ..< n {
            if obstacleGrid[0][j] == 1 {
                break
            }
            map[0][j] = 1
        }
        
        for i in 1 ..< m {
            for j in 1 ..< n {
                if obstacleGrid[i][j] == 1  {
                    map[i][j] = 0
                    continue
                }
                map[i][j] = map[i-1][j] + map[i][j-1]
            }
        }
        
        return map[m-1][n-1]
    }
}
