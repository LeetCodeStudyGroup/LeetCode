class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strs = str.split(' ')
        if len(strs) != len(pattern):
            return False
        pat_record = {}
        str_record = {}
        for i in range(len(pattern)):
            if pattern[i] in pat_record and strs[i] in str_record:
                if pat_record[pattern[i]] != strs[i] or str_record[strs[i]] != pattern[i]:
                    return False
            elif pattern[i] not in pat_record and strs[i] not in str_record:
                pat_record[pattern[i]] = strs[i]
                str_record[strs[i]] = pattern[i]
            else:
                return False
        return True
