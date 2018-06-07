class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ary = list(s)
        for i in range(0, len(ary), 2 * k):
            if i + k > len(ary):
                self.reverse(ary, i, len(s) - 1)
            else:
                self.reverse(ary, i, i + k - 1)
        return ''.join(ary)

    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
