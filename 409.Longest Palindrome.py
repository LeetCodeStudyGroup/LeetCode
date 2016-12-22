class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt, record = 0, set()
        for c in s:
            if c in record:
                record.remove(c)
                cnt += 2
            else:
                record.add(c)
        if len(record) > 0:
            cnt += 1
        return cnt

