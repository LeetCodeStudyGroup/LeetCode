class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if len(num) == 0:
            return True
        i, j = 0, len(num) - 1
        while i <= j:
            if not self.check(num[i], num[j]):
                return False
            i, j = i + 1, j - 1
        return True

    def check(self, a, b):
        pairs = [('0', '0'), ('1', '1'), ('8', '8'), ('6', '9'), ('9', '6')]
        for x, y in pairs:
            if a == x and b == y:
                return True
        return False
