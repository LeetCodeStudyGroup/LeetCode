class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        self.search(result, s, 0, 0, '', 0)
        return result
        
    def search(self, result, s, start, end, str_res, cnt):
        if end == len(s) and cnt == 4:
            result.append(str_res)
        if end < len(s) and cnt < 4:
            cs = s[start:end + 1]
            if len(cs) > 1 and cs[0] == '0':
                return
            if int(cs) <=255:
                self.search(result, s, start, end + 1, str_res, cnt)
                str_res = str_res + '.' + cs if cnt > 0 else cs
                self.search(result, s, end + 1, end + 1, str_res, cnt + 1)
