class Solution(object):
    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        """
        mark = [-1] * 256
        max_val = start = cur = 0
        while cur < len(s):
            start = max(mark[ord(s[cur])] + 1, start)
            mark[ord(s[cur])] = cur
            cur += 1
            max_val = max(max_val, cur - start)
        return max_val

    def lengthOfLongestSubstring(self, s):
        mark = [-1] * 256
        max_val = cur = start = 0
        while cur < len(s):
            if mark[ord(s[cur])] >= start:
                if cur - start > max_val:
                    max_val = cur - start
                start = mark[ord(s[cur])] + 1
            mark[ord(s[cur])] = cur
            cur += 1
        if cur - start > max_val:
            return cur - start
        return max_val
