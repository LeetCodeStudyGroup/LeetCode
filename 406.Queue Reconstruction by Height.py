class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        max_k = 0
        for person in people:
            max_k = max(max_k, person[1])
        ks = [[] for x in range(max_k + 1)]
        for person in people:
            self.insert(ks[person[1]], person)
        result = ks[0]
        for i in range(1, len(ks)):
            for p in range(len(ks[i]) - 1, -1, -1):
                j = count = 0
                while j < len(result):
                    if count == i:
                        break
                    if result[j][0] >= ks[i][p][0]:
                        count += 1
                    j += 1
                result.insert(j, ks[i][p])
        return result

    def insert(self, people, person):
        for i in range(len(people)):
            if people[i][0] > person[0]:
                people.insert(i, person)
                return
        people.append(person)
