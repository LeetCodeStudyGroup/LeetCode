from collections import defaultdict

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph = defaultdict(list)
        chars = set()
        for word in words:
            for c in word:
                chars.add(c)
        graph[''] = list(chars)
        self.build_graph(graph, words)

        rst = ''
        stack, visited = [], set()
        if not self.topological_sort(graph, '', stack, visited, set()):
            return rst

        while len(stack) > 0:
            rst += stack.pop()
        return rst

    def build_graph(self, graph, words):
        if len(words) <= 1:
            return

        new_words = defaultdict(list)
        char = words[0][0]
        for word in words:
            if char != word[0]:
                graph[char].append(word[0])
                char = word[0]
            if len(word) > 1:
                new_words[word[0]].append(word[1:])

        for key in new_words.keys():
            self.build_graph(graph, new_words[key])

    def topological_sort(self, graph, c, stack, visited, loop):
        if c in visited:
            return True
        if c in loop:
            return False

        loop.add(c)
        for n in graph[c]:
            if not self.topological_sort(graph, n, stack, visited, loop):
                return False
        visited.add(c)
        stack.append(c)
        return True
