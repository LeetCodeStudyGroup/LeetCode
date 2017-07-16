class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) == 0 or len(t) == 0:
            return ""

        req, count = {}, len(t)
        i, j = -1, 0
        start, end = -1, len(s)
        for c in t:
            if c in req:
                req[c] += 1
            else:
                req[c] = 1

        while j < len(s):
            if count > 0 and i + 1 < len(s):
                i += 1
                if s[i] in req:
                    req[s[i]] -= 1
                    if req[s[i]] >= 0:
                        count -= 1
            else:
                if count == 0 and (i - j) < (end -start):
                    start, end = j, i
                if s[j] in req:
                    req[s[j]] += 1
                    if req[s[j]] > 0:
                        count += 1
                j += 1
        return s[start:end + 1] if start != -1 else ""

    def minWindow2(self, s, t):
        if len(s) == 0 or len(t) == 0 or len(t) > len(s):
            return ""

        index = {}
        start, end = -1, len(s)
        for c in t:
            if c in index:
                index[c].append(-1)
            else:
                index[c] = [-1]

        for i in range(len(s)):
            if s[i] in index:
                index[s[i]][0] = i
                index[s[i]] = sorted(index[s[i]])
                rst, ls, le = self.find(index)
                if rst and (end - start) > (le - ls):
                    start, end = ls, le
        return s[start:end + 1] if start != -1 else ""

    def find(self, index):
        keys = index.keys()
        start, end = index[keys[0]][0], index[keys[0]][-1]
        for key in keys:
            if index[key][0] == -1:
                return False, -1, -1
            start = min(index[key][0], start)
            end = max(index[key][-1], end)
        return True, start, end
