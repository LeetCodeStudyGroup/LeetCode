class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        self.rst = []
        self.backtrack(word, 0, 0, '')
        return self.rst
            
    def backtrack(self, word, num, inx, chars):
        n = str(num) if num > 0 else ''
        if inx == len(word):
            self.rst.append(chars + n)
        else:
            self.backtrack(word, num + 1, inx + 1, chars)
            self.backtrack(word, 0, inx + 1, chars + n + word[inx])

    def generateAbbreviations2(self, word):
        self.rst = []
        self.helper(word, 0, [])
        return self.rst

    def helper(self, word, inx, chars):
        if inx > len(word):
            return
        if inx == len(word):
            self.rst.append(''.join(chars))
            return

        for i in range(len(word) + 1 - inx):
            next_chars = chars[:]
            next_inx = inx + i
            if i > 0:
                next_chars.append(str(i))
            if next_inx + 1 <= len(word):
                next_chars.append(word[next_inx])
                next_inx += 1
            self.helper(word, next_inx, next_chars)
