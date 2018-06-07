class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        if len(rectangles) == 0 or len(rectangles[0]) == 0:
            return False

        import sys
        x1 = y1 = sys.maxint
        x2 = y2 = -sys.maxint
        area, mem = 0, set()
        for rect in rectangles:
            x1 = min(x1, rect[0])
            y1 = min(y1, rect[1])
            x2 = max(x2, rect[2])
            y2 = max(y2, rect[3])

            area += (rect[2] - rect[0]) * (rect[3] - rect[1])
            nodes = [(rect[0], rect[1]), (rect[0], rect[3]), (rect[2], rect[3]), (rect[2], rect[1])]
            for node in nodes:
                if node in mem:
                    mem.remove(node)
                else:
                    mem.add(node)

        for x in [x1, x2]:
            for y in [y1, y2]:
                if (x, y) not in mem:
                    return False
        return len(mem) == 4 and area == (x2 - x1) * (y2 - y1)
