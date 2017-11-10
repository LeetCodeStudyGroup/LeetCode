/*
    Follow up for "Unique Paths":

    Now consider if some obstacles are added to the grids. How many unique paths would there be?

    An obstacle and empty space is marked as 1 and 0 respectively in the grid.

    For example,
    There is one obstacle in the middle of a 3x3 grid as illustrated below.

    [
      [0,0,0],
      [0,1,0],
      [0,0,0]
    ]
    The total number of unique paths is 2.

    Note: m and n will be at most 100.
     */

    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        if (obstacleGrid == null || obstacleGrid.length == 0 || obstacleGrid[0].length == 0)
            return 0;
        int row = obstacleGrid.length;
        int colume = obstacleGrid[0].length;
        int[][] result = new int[row][colume];

        if (obstacleGrid[row-1][colume-1] == 1)
            return 0;

        for (int i=0; i<row; i++) {
            if (obstacleGrid[i][0] == 1 || (i > 0 && result[i-1][0] == 0))
                result[i][0] = 0;
            else
                result[i][0] = 1;
        }

        for (int i=0; i<colume; i++) {
            if (obstacleGrid[0][i] == 1 || (i > 0 && result[0][i-1] == 0))
                result[0][i] = 0;
            else
                result[0][i] = 1;
        }

        for (int i=1; i<row; i++) {
            for (int j=1; j<colume; j++) {
                if (obstacleGrid[i-1][j] == 1 && obstacleGrid[i][j-1] == 1)
                    result[i][j] = 0;
                else if (obstacleGrid[i-1][j] == 1)
                    result[i][j] = result[i][j-1];
                else if (obstacleGrid[i][j-1] == 1)
                    result[i][j] = result[i-1][j];
                else
                    result[i][j] = result[i][j-1] + result[i-1][j];
            }
        }


        return result[row - 1][colume - 1];
    }
