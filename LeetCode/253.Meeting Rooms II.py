# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        starts = [interval.start for interval in intervals]
        ends = [interval.end for interval in intervals]
        starts.sort()
        ends.sort()
        room, inx = 0, 0
        for i in range(len(starts)):
            if starts[i] < ends[inx]:
                room += 1
            else:
                inx += 1
        return room

    def minMeetingRooms2(self, intervals):
        intervals = sorted(intervals, cmp=lambda x, y: x.start - y.start)
        times = []
        for interval in intervals:
            is_select = False
            for i in range(len(times)):
                if times[i] <= interval.start:
                    times[i] = interval.end
                    is_select = True
                    break
            if not is_select:
                times.append(interval.end)
        return len(times)
