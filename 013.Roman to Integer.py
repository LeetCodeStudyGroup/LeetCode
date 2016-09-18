class Solution(object):
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ret = 0
        str_inx = 0
        while str_inx < len(s):
            if (str_inx + 1) < len(s) and num_map[s[str_inx + 1]] > num_map[s[str_inx]]:
                ret += num_map[s[str_inx + 1]] - num_map[s[str_inx]]
                str_inx += 1
            else:
                ret += num_map[s[str_inx]]
            str_inx += 1
        return ret
