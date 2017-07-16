class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return False

        for num in range(1, (len(s) / 2) + 1):
            if len(s) % num == 0:
                if self.isRepeated(s, num):
                    return True
        return False

    def isRepeated(self, s, num):
        new_s = s[num:] + s[:num]
        return new_s == s

    def isRepeated2(self, s, num):
        for i in range(num):
            char = s[i]
            for j in range(i + num, len(s), num):
                if s[i] != s[j]:
                    return False
        return True
