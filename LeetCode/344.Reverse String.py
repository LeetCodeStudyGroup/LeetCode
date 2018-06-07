class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        x = []
        j = len(s) - 1
        while j >= 0:
            x.append(s[j])
            j -= 1
        return ''.join(x)
        # return s[::-1]
