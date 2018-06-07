class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 11:
            return []

        rst, record, val = [], {}, 0
        for i in range(9):
            val = self.encode(val, s[i])

        for i in range(9, len(s)):
            val = self.encode(val, s[i])
            if val in record:
                record[val] += 1
            else:
                record[val] = 1
        for key in record.keys():
            if record[key] > 1:
                rst.append(self.decode(key))
        return rst

    def decode(self, val):
        mapping = { 0:'A', 1:'C', 2:'G', 3:'T' }
        rst = ''
        for i in range(10):
            v = val & 0x3
            rst = mapping[v] + rst
            val = val >> 2
        return rst

    def encode(self, val, c):
        mapping = { 'A':0, 'C':1, 'G':2, 'T':3 }
        val = val << 2
        val += mapping[c]
        return val & 0xfffff
