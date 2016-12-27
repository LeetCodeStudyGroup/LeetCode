import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        i, r = 0, random.randrange(self.nums.count(target))
        while True:
            if self.nums[i] == target:
                if r == 0: break
                r -= 1
            i += 1
        return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
