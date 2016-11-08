class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_table = {}
        t_table = {}
        for i in range(len(s)):
            if s[i] not in s_table and t[i] not in t_table:
                s_table[s[i]], t_table[t[i]] = t[i], s[i]
            elif s[i] not in s_table or t[i] not in t_table or s_table[s[i]] != t[i] or t_table[t[i]] != s[i]:
                return False
        return True
