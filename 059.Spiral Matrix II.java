/*
    Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

    For example,
    Given n = 3,

    You should return the following matrix:
    [
     [ 1, 2, 3 ],
     [ 8, 9, 4 ],
     [ 7, 6, 5 ]
    ]
     */

    public int[][] generateMatrix(int n) {
        int[][] answer = new int[n][n];
        int rowStart = 0;
        int rowEnd = n;
        int columeStart = 0;
        int columeEnd = n;
        int count = 1;

        while (count <= n * n) {
            for (int i = columeStart; i < columeEnd; i++, count++) {
                answer[rowStart][i] = count;
            }
            rowStart++;
            for (int i = rowStart; i < rowEnd; i++, count++) {
                answer[i][columeEnd - 1] = count;
            }
            columeEnd--;
            for (int i = columeEnd - 1; i >= columeStart; i--, count++) {
                answer[rowEnd - 1][i] = count;
            }
            rowEnd--;
            for (int i = rowEnd - 1; i >= rowStart; i--, count++) {
                answer[i][columeStart] = count;
            }
            columeStart++;
        }

        return answer;
    }
