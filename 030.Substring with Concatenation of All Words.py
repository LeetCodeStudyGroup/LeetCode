class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        rst = []
        if len(words) == 0 or len(s) == 0:
            return rst
        size = len(words[0])
        req = {}
        for word in words:
            req[word] = req[word] + 1 if word in req else 1
        for i in range(size):
            self.find(s, words, req, rst, size, i)
        return rst

    def find(self, s, words, req, rst, size, i):
        record = {}
        count = 0
        j = i
        while i + size <= len(s) and j + size <= len(s):
            string = s[i:i + size]
            if string in req:
                if count < len(words) and (string not in record or record[string] < req[string]):
                    record[string] = record[string] + 1 if string in record else 1
                    count += 1
                    i += size
                else:
                    record[s[j:j + size]] -= 1
                    count -= 1
                    j += size
                if count == len(words):
                    rst.append(j)
            else:
                record = {}
                count = 0
                i += size
                j = i
