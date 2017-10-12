class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rst = [-1] * len(nums)
        stack = []
        for i in range(len(nums) * 2):
            num = nums[i % len(nums)]
            while len(stack) > 0 and num > nums[stack[-1]]:
                rst[stack.pop()] = num
            if i < len(nums):
                stack.append(i)
        return rst
