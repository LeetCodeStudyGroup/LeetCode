class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from collections import defaultdict
        path = defaultdict(list)
        mask = defaultdict(int)
        for t1, t2 in tickets:
            mask[(t1, t2)] += 1
            path[t1].append(t2)
        for key in path.keys():
            path[key].sort()

        return self.dfs(path, mask, ["JFK"], "JFK", len(tickets) + 1)

    def dfs(self, path, mask, cur, frm, count):
        if len(cur) == count:
            return cur

        for to in path[frm]:
            if mask[(frm, to)] > 0:
                nxt = cur[:]
                nxt.append(to)
                mask[(frm, to)] -= 1
                lst = self.dfs2(path, mask, nxt, to, count)
                if len(lst) == count:
                    return lst
                mask[(frm, to)] += 1
        return cur

