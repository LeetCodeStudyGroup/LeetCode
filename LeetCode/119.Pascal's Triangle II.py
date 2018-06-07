class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1] * (rowIndex + 1)
        extra = [1] * (rowIndex + 1)
        for i in range(rowIndex):
            j = 1
            while j <= i:
                extra[j] = result[j - 1] + result[j]
                j += 1
            result, extra = extra, result
        return result
