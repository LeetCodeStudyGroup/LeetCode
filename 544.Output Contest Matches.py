class Solution(object):
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        match = [ x + 1 for x in range(n)]
        while len(match) > 1:
            tmp, n = [], len(match)
            for i in range(n / 2):
                strs = [str(match[i]), str(match[n - i - 1])]
                tmp.append('(' + ','.join(strs) + ')')
            match = tmp

        return match[0]
