class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        self.r1 = set(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'])
        self.r2 = set(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'])
        self.r3 = set(['z', 'x', 'c', 'v', 'b', 'n', 'm'])
        rst = []
        for word in words:
            if len(word) == 0 or self.is_same_row(word.lower()):
                rst.append(word)
        return rst

    def is_same_row(self, word):
        row = None
        if word[0] in self.r1:
            row = self.r1
        elif word[0] in self.r2:
            row = self.r2
        elif word[0] in self.r3:
            row = self.r3
        else:
            return False
        for i in range(1, len(word)):
            if word[i] not in row:
                return False
        return True
