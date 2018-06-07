class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False

        match = {'(':')', '[':']', '{':'}'}
        record = []
        i = 0
        while i < len(s):
            if s[i] in match:
                record.append(match[s[i]])
            elif len(record) == 0 or s[i] != record.pop(-1):
                return False
            i += 1
        
        if len(record) == 0:
            return True
        return False
