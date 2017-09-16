class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        ary = [0] * len(s)
        for i in range(len(s)):
            for string in dict:
                end = i + len(string)
                if end <= len(s) and string == s[i:end]:
                    ary[i] += 1
                    if end < len(s):
                        ary[end] -= 1

        count = 0
        rst = ''
        for i in range(len(ary)):
            if count == 0 and ary[i] > 0:
                rst += '<b>'
            if count > 0 and count + ary[i] == 0:
                rst += '</b>'
            rst += s[i]
            count += ary[i]
        if count > 0:
            rst += '</b>'
        return rst
