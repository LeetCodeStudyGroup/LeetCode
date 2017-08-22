class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if beginWord == endWord:
            return [[beginWord]]
        words = set(wordList)
        if endWord not in words:
            return []

        rst, left, right = [], [], []
        if self.build(beginWord, endWord, words, left, right):
            lrst, rrst = [], []
            self.dfs(lrst, left, 0, [beginWord])
            self.dfs(rrst, right, 0, [endWord])
            for l in lrst:
                for r in rrst:
                    if l[-1] == r[-1]:
                        lst = list(l[:-1])
                        lst.extend(reversed(r))
                        rst.append(lst)
        return rst

    def dfs(self, rst, graph, inx, lst):
        if inx == len(graph):
            rst.append(lst)
            return

        if lst[-1] in graph[inx]:
            for word in graph[inx][lst[-1]]:
                next_list = list(lst)
                next_list.append(word)
                self.dfs(rst, graph, inx + 1, next_list)

    def build(self, beginWord, endWord, words, left, right):
        starts, ends = set([beginWord]), set([endWord])
        backup = set(words)
        is_find = False
        while len(starts) > 0:
            left.append({})
            next_starts, next_words = set(), set(words)
            for begin in starts:
                tmp = set()
                if self.transfer(begin, tmp, ends, words, next_words):
                    is_find = True
                left[-1][begin] = tmp
                for w in tmp:
                    next_starts.add(w)
            if is_find:
                break
            starts, words = next_starts, next_words
            if len(starts) > len(ends):
                starts, ends = ends, starts
                left, right = right, left
                words, backup = backup, words
        return is_find

    def transfer(self, begin, starts, ends, words, next_words):
        is_find = False
        for i in range(len(begin)):
            for j in range(26):
                char = chr(j + ord('a'))
                if char == begin[i]:
                    continue
                string = begin[:i] + char + begin[i + 1:]
                if string in ends:
                    is_find = True
                if string in words:
                    starts.add(string)
                    if string in next_words:
                        next_words.remove(string)
        return is_find
