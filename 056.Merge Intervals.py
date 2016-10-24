# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: x.start)
        i = 0
        while i < len(intervals) - 1:
            if self.do_merge(intervals[i], intervals[i + 1]):
                intervals.pop(i + 1)
            else:
                i += 1
        return intervals

    def do_merge(self, inv1, inv2):
        if inv2.start >= inv1.start and inv2.end <= inv1.end:
            return True
        elif inv2.start >= inv1.start and inv2.start <= inv1.end:
            inv1.end = inv2.end
            return True
        elif inv2.end >= inv1.start and inv2.end <= inv1.end:
            inv1.start = inv2.start
            return True
        return False
