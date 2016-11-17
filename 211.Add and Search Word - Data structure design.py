class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.exist = False
        self.path = {}

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
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
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if len(word) == 0: return True
        return self.search_node(word, self.root, 0)

    def search_node(self, word, node, i):
        if i == len(word) - 1:
            if word[i] == '.':
                for key in node.path.keys():
                    if node.path[key].exist:
                        return True
            return word[i] in node.path and node.path[word[i]].exist
        elif word[i] == '.':
            for key in node.path.keys():
                if self.search_node(word, node.path[key], i + 1):
                    return True
        elif word[i] in node.path:
            return self.search_node(word, node.path[word[i]], i + 1)
        return False

# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("word")
wordDictionary.search("pattern")
