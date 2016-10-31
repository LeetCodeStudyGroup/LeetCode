class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0]
        base = 1
        for i in range(1, num + 1):
            if i == base * 2:
                base *= 2
            result.append(result[i - base] + 1)
        return result
