class Solution {
    func uniquePaths(_ m: Int, _ n: Int) -> Int {
        var map = Array(repeating: Array(repeating: 1, count: n), count: m)
        
        for i in 1 ..< m {
            for j in 1 ..< n {
                map[i][j] = map[i-1][j] + map[i][j-1]
            }
        }
        
        return map[m-1][n-1]
    }
}
