class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if beginWord == endWord:
            return 1
        words = set(wordList)
        if endWord not in words:
            return 0
        words.remove(endWord)
        starts, ends = set([beginWord]), set([endWord])
        layer = 2
        while len(starts) > 0:
            new_starts = set()
            for begin in starts:
                if self.transfer(begin, new_starts, ends, words):
                    return layer
            starts = new_starts
            if len(starts) > len(ends):
                starts, ends = ends, starts
            layer += 1
        return 0

    def transfer(self, begin, starts, ends, words):
        for i in range(len(begin)):
            for j in range(26):
                char = chr(j + ord('a'))
                if char == begin[i]:
                    continue
                string = begin[:i] + char + begin[i + 1:]
                if string in ends:
                    return True
                if string in words:
                    starts.add(string)
                    words.remove(string)
        return False
