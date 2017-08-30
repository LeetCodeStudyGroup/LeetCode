class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        count = 0
        for i in range(len(points)):
            dists = defaultdict(int)
            for j in range(len(points)):
                dists[self.get_dis(points, i, j)] += 1
            for d, cnt in dists.items():
                if cnt > 1:
                    count += cnt * (cnt - 1)
        return count

    def get_dis(self, points, i, j):
        x, y = points[i][0] - points[j][0], points[i][1] - points[j][1]
        return x * x + y * y
