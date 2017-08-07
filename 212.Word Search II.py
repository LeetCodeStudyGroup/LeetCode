class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if len(board) == 0 or len(board[0]) == 0:
            return []
        rst, record = [], set()
        trie = Trie(words)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie.root.next:
                    record.add((i, j))
                    self.dfs(board, rst, trie.root.next[board[i][j]], record, i, j)
                    record.remove((i, j))
        return rst

    def dfs(self, board, rst, node, record, i, j):
        if node.word:
            rst.append(node.word)
            node.word = None

        matrix = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        for offi, offj in matrix:
            newi, newj = i + offi, j + offj
            if self.check_range(board, newi, newj) and (newi, newj) not in record and board[newi][newj] in node.next:
                record.add((newi, newj))
                self.dfs(board, rst, node.next[board[newi][newj]], record, newi, newj)
                record.remove((newi, newj))

    def check_range(self, board, i, j):
        return i >= 0 and i < len(board) and j >= 0 and j < len(board[0])

class Trie(object):
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            node = self.root
            if len(word) == 0:
                continue
            for c in word:
                if c not in node.next:
                    node.next[c] = TrieNode()
                node = node.next[c]
            node.word = word

class TrieNode(object):
    def __init__(self):
        self.word = None
        self.next = {}
