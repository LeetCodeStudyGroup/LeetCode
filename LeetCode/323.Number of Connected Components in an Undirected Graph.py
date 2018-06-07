class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        uf = UnionFind(n)
        for edge in edges:
            uf.union(edge[0], edge[1])
        return uf.cnt

class UnionFind(object):
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.cnt = n

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False

        if self.rank[p1] == self.rank[p2]:
            if p1 > p2:
                self.parent[p2] = p1
                self.rank[p1] += 1
            else:
                self.parent[p1] = p2
                self.rank[p2] += 1
        elif self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        else:
            self.parent[p1] = p2
        self.cnt -= 1
        return True

    def find(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]
