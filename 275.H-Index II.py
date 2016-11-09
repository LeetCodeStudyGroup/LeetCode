class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        start, end = 0, len(citations) - 1
        while start <= end:
            mid = (start + end) / 2
            if citations[mid] < len(citations) - mid:
                start = mid + 1
            else:
                end = mid - 1
        return len(citations) - start

    def hIndex2(self, citations):
        return self.search(citations, 0, len(citations) - 1)

    def search(self, citations, start, end):
        if start > end or citations[-1] == 0:
            return 0
        elif citations[0] >= len(citations):
            return len(citations)

        mid = (start + end) / 2
        if citations[mid] < len(citations) - mid and citations[mid + 1] >= len(citations) - (mid + 1):
            return len(citations) - (mid + 1)
        elif citations[mid] < len(citations) - mid:
            return self.search(citations, mid + 1, end)
        else:
            return self.search(citations, start, mid)

    def hIndex_TLE(self, citations):
        for i in range(len(citations)):
            if citations[i] >= len(citations) - i:
                return len(citations) - i
        return 0
