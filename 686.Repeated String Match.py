class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        times = len(B) / len(A)
        if times == 0:
            times += 1
        for i in range(2):
            if B in A * (times + i):
                return times + i
        return -1
