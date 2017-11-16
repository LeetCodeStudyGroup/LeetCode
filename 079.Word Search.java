/*
    Given a 2D board and a word, find if the word exists in the grid.

    The word can be constructed from letters of sequentially adjacent cell,
     where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

    For example,
    Given board =

    [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]
    word = "ABCCED", -> returns true,
    word = "SEE", -> returns true,
    word = "ABCB", -> returns false.
     */

    public boolean exist(char[][] board, String word) {
        char words[] = word.toCharArray();
        for (int i=0; i<board.length; i++) {
            for (int j=0; j<board[0].length; j++) {
                if (findWord(board, i, j, words, 0))
                    return true;
            }
        }
        return false;
    }


    public boolean findWord(char[][] board, int row, int column, char[] word, int index) {
        if (index == word.length)
            return true;
        if (row < 0 || column < 0 || row == board.length || column == board[0].length)
            return false;
        if (board[row][column] != word[index])
            return false;

        board[row][column] ^= 256;
        boolean exist = findWord(board, row+1, column, word, index+1)
                || findWord(board, row, column+1, word, index+1)
                || findWord(board, row-1, column, word, index+1)
                || findWord(board, row, column-1, word, index+1);
        board[row][column] ^= 256;

        return exist;
    }
