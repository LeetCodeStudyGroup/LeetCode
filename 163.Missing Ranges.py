class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        rst = []
        start = lower
        for num in nums:
            if num == start:
                start += 1
            elif num > start:
                rst.append(self.range2str(start, num - 1))
                start = num + 1
        if start <= upper:
            rst.append(self.range2str(start, upper))
        return rst

    def range2str(self, start, end):
        rst = str(start)
        if start != end:
            rst += '->' + str(end)
        return rst
