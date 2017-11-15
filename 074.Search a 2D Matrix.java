/*
    Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.
    For example,

    Consider the following matrix:

    [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
    Given target = 3, return true.
     */

    public boolean searchMatrix(int[][] matrix, int target) {
        int row = matrix.length;
        if (row == 0)
            return false;
        int column = matrix[0].length;
        if (column == 0)
            return false;
        for (int i = 0; i < row; i++) {
            if(matrix[i][column-1] >= target) {
                int left = 0;
                int right = column - 1;
                while (left <= right) {
                    int middle = (left + right) / 2;
                    if (matrix[i][middle] == target)
                        return true;
                    if (matrix[i][middle] > target) {
                        if (middle == right)
                            right = middle - 1;
                        else
                            right = middle;
                    } else {
                        if (middle == left)
                            left = middle + 1;
                        else
                            left = middle;
                    }
                }
            }
        }

        return false;
    }
