class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.exist = False
        self.path = {}

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node, i = self.root, 0
        while i < len(word) and word[i] in node.path:
            node = node.path[word[i]]
            i += 1
        while i < len(word):
            node.path[word[i]] = TrieNode()
            node = node.path[word[i]]
            i += 1
        node.exist = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node, i = self.root, 0
        for s in word:
            if s not in node.path:
                return False
            node = node.path[s]
        return node.exist

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node, i = self.root, 0
        for s in prefix:
            if s not in node.path:
                return False
            node = node.path[s]
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
