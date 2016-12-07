class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        courses = [[] for x in range(numCourses)]
        for pair in prerequisites:
            courses[pair[0]].append(pair[1])
        record = set()
        for i in range(numCourses):
            if self.find_circle(courses, record, set(), i):
                return False
        return True

    def find_circle(self, courses, record, nodes, inx):
        if len(courses[inx]) == 0 or inx in record:
            return False
        if inx in nodes:
            return True
        nodes.add(inx)
        for num in courses[inx]:
            if self.find_circle(courses, record, nodes, num):
                return True
        nodes.remove(inx)
        record.add(inx)
        return False
