class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
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
