/*
    Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

    Follow up:
    Did you use extra space?
    A straight forward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?
     */

    public void setZeroes(int[][] matrix) {
        int row = matrix.length;
        if (row == 0)
            return;
        int column = matrix[0].length;
        int rowZero[] = new int[row];
        int columnZero[] = new int[column];

        for (int i=0; i<row; i++) {
            for (int j=0; j<column; j++) {
                if (matrix[i][j] == 0) {
                    rowZero[i] = 1;
                    columnZero[j] = 1;
                }
            }
        }

        for (int i=0; i<row; i++) {
            for (int j=0; j<column; j++) {
                if (rowZero[i] == 1 || columnZero[j] == 1)
                    matrix[i][j] = 0;
            }
        }
    }
