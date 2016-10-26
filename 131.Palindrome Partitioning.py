class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        tables = []
        for i in range(len(s)):
            table = [i]
            for j in range(i + 1, len(s)):
                if self.is_partition(s, i, j):
                    table.append(j)
            tables.append(table)
        result = []
        self.find_partition(result, tables, s, [], 0)
        return result

    def find_partition(self, result, tables, s, sets, inx):
        if inx == len(s):
            result.append(sets)
            return
        for i in tables[inx]:
            new_set = sets[:]
            new_set.append(s[inx:i + 1])
            self.find_partition(result, tables, s, new_set, i + 1)
        
    def is_partition(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
