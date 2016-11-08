class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        record = [0] * (len(citations) + 1)
        for i in range(len(citations)):
            if citations[i] >= len(citations):
                record[len(citations)] += 1
            else:
                record[citations[i]] += 1
        val = 0
        for i in range(len(record) - 1, -1, -1):
            val += record[i]
            if val >= i:
                return i
        return 0

    def hIndex2(self, citations):
        citations.sort()
        for i in range(len(citations)):
            if citations[i] >= len(citations) - i:
                return citations[i]
        return 0
