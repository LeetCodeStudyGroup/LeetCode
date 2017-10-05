class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = 0
        for edge in edges:
            n = max(n, max(edge))
        uf = UnionFind(n + 1)
        for edge in edges:
            if not uf.union(edge[0], edge[1]):
                return edge
        return []

class UnionFind(object):
    def __init__(self, n):
        self.parent = [x for x in range(n)]
        self.rank = [0] * n

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False

        if self.rank[p1] >= self.rank[p2]:
            self.rank[p1] += 1
            self.parent[p2] = p1
        else:
            self.rank[p2] += 1
            self.parent[p1] = p2
        return True
