class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0 or len(strs[0]) == 0:
            return ""
        
        ret = ""
        inx = 0
        while inx < len(strs[0]):
            cur_char = strs[0][inx]
            i = 1
            while i < len(strs):
                if  inx >= len(strs[i]) or strs[i][inx] != cur_char:
                    return ret
                i += 1
            ret += cur_char
            inx += 1
        return ret
