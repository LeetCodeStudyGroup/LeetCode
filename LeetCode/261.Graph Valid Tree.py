from collections import deque

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if n != len(edges) + 1:
            return False

        graph = [[] for _ in range(n)]
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        visited = [0] * n
        if not self.bfs(graph, visited):
            return False

        for visit in visited:
            if visit == 0:
                return False
        return True

    def bfs(self, graph, visited):
        q = deque([0])
        visited[0] = 1
        while len(q) > 0:
            for _ in range(len(q)):
                node = q.popleft()
                for nxt in graph[node]:
                    if visited[nxt] == 1:
                        return False
                    if visited[nxt] == 0:
                        q.append(nxt)
                visited[node] = 2
        return True

    def validTree2(self, n, edges):
        uf = UnionFind(n)
        for node1, node2 in edges:
            if not uf.union(node1, node2):
                return False
        return uf.count == 1

class UnionFind(object):
    def __init__(self, n):
        self.parent = [0] * n
        self.rank = [0] * n
        self.count = n
        for i in range(n):
            self.parent[i] = i

    def union(self, node1, node2):
        p1, p2 = self.find(node1), self.find(node2)
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1
        self.count -= 1
        return True

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
