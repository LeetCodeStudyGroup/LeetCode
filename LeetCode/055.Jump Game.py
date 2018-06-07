class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return True
        record = [None] * len(nums)
        record[0] = True
        last = 0
        for pos in range(len(nums) - 1):
            if record[pos] and pos + nums[pos] > last:
                for i in range(last + 1, pos + nums[pos] + 1):
                    if i >= len(nums) - 1:
                        return True
                    record[i] = True
                    last = i
        return False
        #return self.find(None, nums, len(nums) - 1)
 
    def find(self, record, nums, pos):
        if pos <= 0:
            return True
        for i in range(pos):
            if nums[i] >= pos - i and self.find(record, nums, i):
                    record[i] = self.find(record, nums, i)
            if record[i]:
                return True
        return False
