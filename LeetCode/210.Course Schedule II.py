class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        courses = [[] for x in range(numCourses)]
        for pair in prerequisites:
            courses[pair[0]].append(pair[1])
        rst, record = [], set()
        for i in range(numCourses):
            if self.find_order(courses, rst, record, set(), i):
                return []
        return rst

    def find_order(self, courses, rst, record, nodes, inx):
        if inx in record:
            return False
        elif inx in nodes:
            return True
        if len(courses[inx]) > 0:
            nodes.add(inx)
            for num in courses[inx]:
                if self.find_order(courses, rst, record, nodes, num):
                    return True
            nodes.remove(inx)
        if inx not in record:
            rst.append(inx)
            record.add(inx)
        return False
