class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        record = {}
        for c in s:
            if c in record:
                record[c] += 1
            else:
                record[c] = 1
        for c in t:
            if c not in record:
                return False
            record[c] -= 1
            if record[c] == 0:
                del record[c]
        return len(record) == 0
