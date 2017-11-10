/*
    Given a m x n grid filled with non-negative numbers,
    find a path from top left to bottom right which minimizes the sum of all numbers along its path.

    Note: You can only move either down or right at any point in time.

    Example 1:
    [[1,3,1],
     [1,5,1],
     [4,2,1]]
    Given the above grid map, return 7. Because the path 1→3→1→1→1 minimizes the sum.
     */

    public int minPathSum(int[][] grid) {
        if (grid == null)
            return 0;

        int row = grid.length;
        int colume = grid[0].length;

        if (row == 0 && colume == 0)
            return 0;
        int[][] sum = new int[row][colume];
        sum[0][0] = grid[0][0];

        for (int i=1; i<row; i++) {
            sum[i][0] = sum[i-1][0] + grid[i][0];
        }

        for (int i=1; i<colume; i++) {
            sum[0][i] = sum[0][i-1] + grid[0][i];
        }

        for (int i=1; i<row; i++) {
            for (int j=1; j<colume; j++) {
                sum[i][j] = Math.min(sum[i-1][j], sum[i][j-1]) + grid[i][j];
            }
        }

        return sum[row-1][colume-1];
    }
