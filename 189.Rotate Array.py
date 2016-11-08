class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k == 0: return
        k %= len(nums)
        self.reverse(nums, 0, len(nums) - 1 - k)
        self.reverse(nums, len(nums) - k, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)

    def reverse(self, nums, s, e):
        while s < e:
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e -= 1

    def rotate2(self, nums, k):
        k %= len(nums)
        backup = nums[len(nums) - k:]
        for i in range(len(nums) - 1, k - 1, -1):
            nums[i] = nums[i - k]
        for i in range(len(backup)):
            nums[i] = backup[i]

    def rotate3(self, nums, k):
        self.recursive(nums, k % len(nums), 0)

    def recursive(self, nums, k, i):
        if i == len(nums):
            return
        t = nums[i]
        self.recursive(nums, k, i + 1)
        nums[(i + k) % len(nums)] = t

    def rotate4(self, nums, k):
        if len(nums) == 0: return
        for _ in range(k):
            temp = nums[-1]
            for i in range(len(nums) - 1, 0, -1):
                nums[i] = nums[i - 1]
            nums[0] = temp
