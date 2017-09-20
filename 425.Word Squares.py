class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        self.rst = []
        if len(words) == 0:
            return self.rst

        trie = Trie(words)
        self.helper(trie, [], 0, len(words[0]))
        return self.rst

    def helper(self, trie, squares, inx, n):
        if inx == n:
            self.rst.append(squares[:])
            return

        prefix = ''
        for i in range(inx):
            prefix += squares[i][inx]

        for t in trie.find_by_prefix(prefix):
            squares.append(t)
            self.helper(trie, squares, inx + 1, n)
            squares.pop()

class Trie(object):
    def __init__(self, words):
        self.root = self.build_trie(words)

    def build_trie(self, words):
        trie = TrieNode('')
        for w in words:
            self.add_word(trie, w, 0)
        return trie

    def find_by_prefix(self, word):
        rst = []
        root = self.root
        for c in word:
            if c not in root.child:
                return rst
            root = root.child[c]
        return root.words

    def add_word(self, trie, word, i):
        if i == len(word):
            return

        trie.words.append(word)
        if word[i] not in trie.child:
            trie.child[word[i]] = TrieNode(word[i])
        self.add_word(trie.child[word[i]], word, i + 1)

class TrieNode(object):
    def __init__(self, char):
        self.char = char
        self.child = {}
        self.words = []
