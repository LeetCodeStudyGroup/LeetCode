# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        max_cnt = 0
        if len(points) < 2:
            return len(points)

        for i in range(len(points)):
            temp_cnt = {}
            local_max = overlap = 0
            for j in range(i + 1, len(points)):
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    overlap += 1
                    continue
                v = self.calu(points[i], points[j])
                if v in temp_cnt:
                    temp_cnt[v] += 1
                else:
                    temp_cnt[v] = 1
                local_max = max(local_max, temp_cnt[v])
            max_cnt = max(max_cnt, local_max + overlap + 1)
        return max_cnt

    def calu(self, p1, p2):
        a = (p2.x - p1.x)
        b = (p2.y - p1.y)
        g = self.gcd(a, b)
        return (a / g, b / g) if g != 0 else (a, b)
        #if b == 0:
        #    return 0
        #return float(a) / b

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)
                
