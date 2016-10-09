class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        i = 0
        while i < numRows:
            cur = []
            if i != 0:
                cur.append(1)
            j = 1
            while j < i:
                cur.append(result[i - 1][j-1] + result[i - 1][j])
                j += 1
            cur.append(1)
            result.append(cur)
            i += 1
        return result
