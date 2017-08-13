class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        if len(p) == 0:
            return 0

        count = [0] * 26
        i, cnt = 1, 1
        count[ord(p[0]) - ord('a')] = 1
        for i in range(1, len(p)):
            cnt = cnt + 1 if self.isContinue(p[i - 1], p[i]) else 1
            inx = ord(p[i]) - ord('a')
            count[inx] = max(count[inx], cnt)
        return sum(count)
    
    def isContinue(self, s1, s2):
        return (ord(s2) - ord(s1)) == 1 or (s1 == 'z' and s2 == 'a')
