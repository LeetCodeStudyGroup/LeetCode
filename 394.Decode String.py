class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ''.join(self.decode(s, 0, False)[0])

    def decode(self, s, i, checking_number=True):
        num = []
        string = []
        while i < len(s) and s[i] != ']':
            if s[i] >= '0' and s[i] <= '9':
                if checking_number:
                    num.append(s[i])
                else:
                    substr, i = self.decode(s, i)
                    string.extend(substr)
            elif s[i] == '[':
                checking_number = False
            else:
                string.append(s[i])
            i += 1
        if len(num) == 0:
            num.append('1')
        return string * int(''.join(num)), i
