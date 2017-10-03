class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if len(points) == 0:
            return True

        mem = {}
        for x, y in points:
            if y not in mem:
                mem[y] = set()
            mem[y].add(x)
        ys = mem.keys()
        yaxis = float(sum(mem[ys[0]])) / len(mem[ys[0]])

        for y in ys:
            for x in mem[y]:
                diff = (x - yaxis) * 2
                if x + diff not in mem[y] and x - diff not in mem[y] :
                    return False
        return True
