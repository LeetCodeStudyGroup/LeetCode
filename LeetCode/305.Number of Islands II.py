class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        rst = []
        uf = UnionFind(m, n)
        for pos in positions:
            uf.add(pos)
            rst.append(uf.count)
        return rst

class UnionFind(object):
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.parent = {}
        self.rank = {}
        self.count = 0

    def add(self, pos):
        i, j = pos
        self.parent[(i, j)] = (i, j)
        self.rank[(i, j)] = 0
        self.count += 1
        for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
            if x >= 0 and y >= 0 and x < self.m and y < self.n and (x, y) in self.parent:
                self.union((i, j), (x, y))

    def find(self, pos):
        if pos != self.parent[pos]:
            self.parent[pos] = self.find(self.parent[pos])
        return self.parent[pos]

    def union(self, pos1, pos2):
        p1, p2 = self.find(pos1), self.find(pos2)
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
        self.count -= 1
        return True
