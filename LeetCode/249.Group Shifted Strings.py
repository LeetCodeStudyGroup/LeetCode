class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        table = defaultdict(dict)
        for s in strings:
            group = self.get_group(table[len(s)], s)
            if group not in table[len(s)]:
                table[len(s)][group] = []
            table[len(s)][group].append(s)

        rst = []
        for key in table.keys():
            for group in table[key]:
                rst.append(table[key][group])
        return rst

    def get_group(self, groups, s):
        for group in groups.keys():
            if self.is_same(group, s):
                return group
        return s

    def is_same(self, s1, s2):
        if s1[0] < s2[0]:
            s1, s2 = s2, s1
        diff = ord(s1[0]) - ord(s2[0])
        for i in range(1, len(s1)):
            val = ord(s2[i]) + diff
            if val > ord('z'):
                val -= 26
            if val != ord(s1[i]):
                return False
        return True
