class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.put(result, [], sorted(nums), 0)
        return result
        
    def put(self, result, subset, nums, inx):
        if inx == len(nums):
            result.append(subset)
            return
        if (inx + 1 < len(nums) and nums[inx] != nums[inx + 1]) or inx + 1 == len(nums):
            self.put(result, subset[:], nums, inx + 1)
        subset.append(nums[inx])
        self.put(result, subset, nums, inx + 1)
