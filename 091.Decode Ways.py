class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        record = {len(s): 1}
        return self.counter(record, s, 0)

    def counter(self, record, s, inx):
        if inx in record:
            return record[inx]
        if s[inx] != '0':
            if inx + 1 < len(s):
                record[inx] = 0
                if s[inx + 1] != '0':
                    record[inx] += self.counter(record, s, inx + 1)
                target = int(s[inx] + s[inx + 1])
                if target >= 10 and target <= 26:
                    record[inx] += self.counter(record, s, inx + 2)
            else:
                record[inx] = self.counter(record, s, inx + 1)
            return record[inx]
        return 0
