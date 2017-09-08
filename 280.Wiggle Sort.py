class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return

        self.size = len(nums)
        pivot = self.find_medium(nums, 0, len(nums) - 1, (len(nums) + 1) / 2)
        i, j, k = 0, 0, len(nums) - 1
        while j <= k:
            if nums[self.index(j)] < pivot:
                nums[self.index(i)], nums[self.index(j)] = nums[self.index(j)], nums[self.index(i)]
                i += 1
                j += 1
            elif nums[self.index(j)] > pivot:
                nums[self.index(j)], nums[self.index(k)] = nums[self.index(k)], nums[self.index(j)]
                k -= 1
            else:
                j += 1

    def index(self, i):
        if i == self.size / 2:
            return self.size - 1
        elif i < self.size / 2:
            return i * 2
        else:
            return (self.size - i - 1) * 2 + 1

    def find_medium(self, nums, start, end, k):
        i, j = start, end
        pivot = nums[(start + end) / 2]
        while i <= j:
            while i <= j and nums[i] < pivot:
                i += 1
            while j <= j and nums[j] > pivot:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        if start + k - 1 >= i:
            return self.find_medium(nums, i, end, k - (i - start))
        if start + k - 1 <= j:
            return self.find_medium(nums, start, j, k)
        return nums[j + 1]
