class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        table, sets = {0:1}, set([0])
        for num in nums:
            next_table, next_set = {}, set()
            for key in sets:
                self.map_add(next_table, key + num, table[key])
                self.map_add(next_table, key - num, table[key])
                next_set.add(key + num)
                next_set.add(key - num)
            table, sets = next_table, next_set
        return table[S] if S in table else 0

    def map_add(self, table, key, value):
        if key in table:
            table[key] += value
        else:
            table[key] = value
