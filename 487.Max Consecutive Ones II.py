class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rst = 0
        last, cur = 0, 0
        for i, num in enumerate(nums):
            if num == 1:
                cur += 1
            else:
                rst = max(rst, last + cur + 1)
                if i + 1 == len(nums) or nums[i + 1] == 1:
                    last = cur
                cur = 0
        rst = max(rst, last + cur + 1)
        return min(len(nums), rst)
