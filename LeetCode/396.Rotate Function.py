class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        total = val = 0
        for i in range(len(A)):
            val += A[i] * i
            total += A[i]
        max_val = val
        for i in range(1, len(A)):
            val += total - A[len(A) - i] * len(A)
            max_val = max(val, max_val)
        return max_val
