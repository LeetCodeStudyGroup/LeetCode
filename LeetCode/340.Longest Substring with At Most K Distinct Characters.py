class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        d, low, rst = {}, -1, 0
        for i, c in enumerate(s):
            d[c] = i
            if len(d) > k:
                low = min(d.values())
                del d[s[low]]
            rst = max(rst, i - low)
        return rst

    def lengthOfLongestSubstringKDistinct2(self, s, k):
        str_map = {}
        max_len, cur = 0, 0
        for i, c in enumerate(s):
            if c in str_map:
                str_map[c] += 1
            else:
                str_map[c] = 1
                while len(str_map) > k:
                    char = s[i - cur]
                    str_map[char] -= 1
                    if str_map[char] == 0:
                        del str_map[char]
                    cur -= 1
            cur += 1
            max_len = max(max_len, cur)
        return max_len
