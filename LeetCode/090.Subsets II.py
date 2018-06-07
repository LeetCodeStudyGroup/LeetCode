class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.add(result, [], sorted(nums), 0)
        return result
        
    def add(self, result, subset, nums, inx):
        if len(nums) == inx:
            result.append(subset)
            return
        self.add(result, subset[:], nums, inx + 1)
        subset.append(nums[inx])
        while inx + 1 < len(nums) and nums[inx] == nums[inx + 1]:
            subset.append(nums[inx + 1])
            inx += 1
        self.add(result, subset, nums, inx + 1)
