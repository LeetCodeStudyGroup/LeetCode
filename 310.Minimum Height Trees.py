class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1: return [0]
        nodes = [[] for i in range(n)]
        for e in edges:
            nodes[e[0]].append(e[1])
            nodes[e[1]].append(e[0])
        leaves = [i for i in range(n) if len(nodes[i]) == 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leave in leaves:
                j = nodes[leave].pop()
                nodes[j].remove(leave)
                if len(nodes[j]) == 1:
                    new_leaves.append(j)
            leaves = new_leaves
        return leaves
