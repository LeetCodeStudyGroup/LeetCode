class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        if version1 == version2:
            return 0
        v1 = version1.split('.')
        v2 = version2.split('.')
        i = 0
        while i < len(v1) and i < len(v2):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
            i += 1
        j = i
        while j < len(v1):
            if int(v1[j]) > 0:
                return 1
            j += 1
        j = i
        while j < len(v2):
            if int(v2[j]) > 0:
                return -1
            j += 1
        return 0
