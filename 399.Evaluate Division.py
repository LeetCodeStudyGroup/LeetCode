class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        from collections import defaultdict
        graph = defaultdict(dict)
        for i, e in enumerate(equations):
            graph[e[0]][e[0]] = 1.0
            graph[e[0]][e[1]] = values[i]
            graph[e[1]][e[0]] = 1 / values[i]

        rst = []
        for a, b in queries:
            if a not in graph or b not in graph:
                rst.append(-1.0)
            else:
                rst.append(self.helper(graph, a, b, 1.0, set()))
        return rst

    def helper(self, graph, start, end, val, record):
        if end in graph[start]:
            return val * graph[start][end]

        record.add(start)
        for key in graph[start].keys():
            if key not in record:
                rst = self.helper(graph, key, end, val * graph[start][key], record)
                if rst != -1.0:
                    return rst
        record.remove(start)
        return -1.0
