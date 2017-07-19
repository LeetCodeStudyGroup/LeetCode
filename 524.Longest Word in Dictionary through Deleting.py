class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        rst = ""
        for string in d:
            if self.is_find(s, string):
                if len(rst) < len(string) or (len(rst) == len(string) and rst > string):
                    rst = string
        return rst

    def is_find(self, s, d):
        i, j = 0, 0
        while i < len(s) and j < len(d):
            if s[i] == d[j]:
                j += 1
                if j == len(d):
                    return True
            i += 1
        return False
