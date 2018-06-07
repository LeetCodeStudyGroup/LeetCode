class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        a %= 1337
        base, val = a, 1
        for i in range(len(b) - 1, -1, -1):
            val *= base ** b[i]
            val %= 1337
            base = base ** 10 % 1337
        return val
