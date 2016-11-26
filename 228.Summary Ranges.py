class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        res = []
        start = end = nums[0]
        for i in range(1, len(nums)):
            if end + 1 != nums[i]:
                self.insert(res, start, end)
                start = end = nums[i]
            else:
                end += 1
        self.insert(res, start, end)
        return res

    def insert(self, res, start, end):
        if start == end:
            res.append(str(end))
        else:
            res.append('->'.join([str(start), str(end)]))
