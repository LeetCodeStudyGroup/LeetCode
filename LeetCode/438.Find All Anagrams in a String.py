class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        mark = {}
        for c in p:
            mark[c] = mark[c] + 1 if c in mark else 1
        result = []
        record = {}
        inx = i = 0
        while i <= len(s) - len(p):
            while inx < i + len(p):
                if s[inx] not in mark:
                    self.reset(s, i, inx, mark)
                    inx = i = inx + 1
                    break
                elif mark[s[inx]] == 0:
                    self.reset(s, i, record[s[inx]], mark)
                    i = record[s[inx]] + 1
                    inx += 1
                    break
                mark[s[inx]] -= 1
                if s[inx] not in record or record[s[inx]] < i:
                    record[s[inx]] = inx
                inx += 1
            if inx == i + len(p):
                result.append(i)
                self.reset(s, i, i + 1, mark)
                i += 1
        return result
        
    def reset(self, s, start, end, mark):
        for i in range(start, end):
            mark[s[i]] += 1
