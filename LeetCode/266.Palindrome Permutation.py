class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mem = set()
        for c in s:
            if c in mem:
                mem.remove(c)
            else:
                mem.add(c)
        return len(mem) <= 1
