class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        cache, index = {}, {}
        for i in range(len(t)):
            if t[i] in cache:
                cache[t[i]].append(i)
            else:
                cache[t[i]], index[t[i]] = [i], 0
        inx = -1
        for c in s:
            if c not in cache:
                return False
            else:
                while index[c] < len(cache[c]) and inx > cache[c][index[c]]:
                    index[c] += 1
                if index[c] == len(cache[c]):
                    return False
                inx = cache[c][index[c]]
                index[c] += 1
        return True

    def isSubsequence2(self, s, t):
        i = j = 0
        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                j += 1
            i += 1
        return j == len(s)
