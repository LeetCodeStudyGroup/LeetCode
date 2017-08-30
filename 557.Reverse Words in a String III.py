class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(x[::-1] for x in s.split())

    def reverseWords2(self, s):
        strs = s.split(' ')
        rst, start, end = '', 0, 0
        for end in range(len(s)):
            if s[end] == ' ':
                rst += s[start:end][::-1] + ' '
                start = end + 1
        if start > end:
            return rst[:-1]
        return rst + s[start:][::-1]
