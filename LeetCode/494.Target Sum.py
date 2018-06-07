class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        table = {0:1}
        for num in nums:
            next_table = {}
            for key in table.keys():
                self.map_add(next_table, key + num, table[key])
                self.map_add(next_table, key - num, table[key])
            table = next_table
        return table[S] if S in table else 0

    def map_add(self, table, key, value):
        if key in table:
            table[key] += value
        else:
            table[key] = value
