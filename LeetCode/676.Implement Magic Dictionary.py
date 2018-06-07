class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = TrieNode()

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            node = self.trie
            for c in word:
                if c not in node.child:
                    node.child[c] = TrieNode()
                node = node.child[c]
            node.is_word = True

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        return self.modify_search(self.trie, word, 0)

    def modify_search(self, node, word, i):
        if i == len(word):
            return False

        for key in node.child.keys():
            if key == word[i]:
                if self.modify_search(node.child[key], word, i + 1):
                    return True
            else:
                if self.normal_search(node.child[key], word, i + 1):
                    return True
        return False

    def normal_search(self, node, word, i):
        for j in range(i, len(word)):
            if word[j] not in node.child:
                return False
            node = node.child[word[j]]
        return node.is_word

class TrieNode(object):
    def __init__(self):
        self.child = {}
        self.is_word = False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
