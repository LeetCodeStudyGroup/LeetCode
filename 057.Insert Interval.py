# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        array = intervals
        interval = newInterval
        i = 0
        while i < len(array):
            if interval.start >= array[i].start and interval.end <= array[i].end:
                return array
            elif interval.start <= array[i].start and interval.end >= array[i].end:
                array.pop(i)
            elif interval.start >= array[i].start and interval.start <= array[i].end:
                interval.start = min(array[i].start, interval.start)
                array.pop(i)
            elif interval.end <= array[i].end and interval.end >= array[i].start:
                interval.end = max(array[i].end, interval.end)
                array.pop(i)
            else:
                i += 1
        if len(array) == 0 or interval.start > array[-1].end:
            array.append(interval)
        elif interval.end < array[0].start:
            array.insert(0, interval)
        else:
            for i in range(1, len(array)):
                if array[i - 1].end <= interval.start and array[i].start >= interval.end:
                    array.insert(i, interval)
                    break
        return array

    def insert2(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return [newInterval]
        root = self.build_tree(intervals, 0, len(intervals) - 1)
        self.insert_node(root, newInterval)
        return self.create_left_list(root, [])

    def build_tree(self, intervals, start, end):
        if start > end:
            return None
        if start == end:
            return SegmentTreeNode(intervals[start])
        tree = SegmentTreeNode(Interval(intervals[start].start, intervals[end].end))
        mid = (start + end) / 2
        tree.left = self.build_tree(intervals, start, mid)
        tree.right = self.build_tree(intervals, mid + 1, end)
        return tree

    def create_left_list(self, node, result):
        if node.left == None and node.right == None:
            result.append(node.interval)
        else:
            self.create_left_list(node.left, result)
            self.create_left_list(node.right, result)
        return result

    def insert_node(self, node, interval):
        if interval.start <= node.interval.start and interval.end >= node.interval.end:
            # cover node
            node.interval = interval
            node.left = None
            node.right = None
        elif node.left and interval.start > node.interval.end:
            self.insert_node(node.right, interval)
        elif node.left and interval.end < node.interval.start:
            self.insert_node(node.left, interval)
        else:
            # inside node
            array = self.create_left_list(node, [])
            new_node = self.build_tree(array, 0, len(array) - 1)
            node.interval = new_node.interval
            node.left = new_node.left
            node.right = new_node.right

class SegmentTreeNode(object):
    def __init__(self, interval):
        self.interval = interval
        self.left = None
        self.right = None
