# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        first = node.label
        record = {first:UndirectedGraphNode(first)}
        nodes = [node]
        while len(nodes) > 0:
            for i in range(len(nodes)):
                node = nodes.pop()
                for n in node.neighbors:
                    if n.label not in record:
                        record[n.label] = UndirectedGraphNode(n.label)
                        nodes.append(n)
                    record[node.label].neighbors.append(record[n.label])
        return record[first]
