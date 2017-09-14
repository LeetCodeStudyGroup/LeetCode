class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        rst = 0
        i, j = 0, -1
        for k in range(len(s)):
            if k > 0 and s[k] == s[k - 1]:
                continue
            if j > -1 and s[k] != s[j]:
                rst = max(rst, k - i)
                i = j + 1
            j = k - 1
        return max(rst, len(s) - i)

    def lengthOfLongestSubstringTwoDistinct2(self, s):
        from collections import defaultdict
        mem = defaultdict(int)
        rst = 0
        start = 0
        for i, c in enumerate(s):
            mem[c] += 1
            while len(mem) > 2:
                mem[s[start]] -= 1
                if mem[s[start]] == 0:
                    mem.pop(s[start])
                start += 1
            rst = max(rst, i - start + 1)
        return rst
