class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        rst = [0] * length
        for start, end, num in updates:
            rst[start] += num
            if end + 1 < length:
                rst[end + 1] -= num

        for i in range(1, len(rst)):
            rst[i] += rst[i - 1]
        return rst
