class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        return self.partition(nums)

    def partition(self, nums):
        i, j, k, n = 0, 0, len(nums) - 1, len(nums)
        index = lambda i, n: (i * 2 + 1) % (n | 1)
        pivot = self.find_medium(nums, 0, len(nums) - 1, (len(nums) + 1) / 2)
        while j <= k:
            if nums[index(j, n)] > pivot:
                nums[index(i, n)], nums[index(j, n)] = nums[index(j, n)], nums[index(i, n)]
                i += 1
                j += 1
            elif nums[index(j, n)] < pivot:
                nums[index(k, n)], nums[index(j, n)] = nums[index(j, n)], nums[index(k, n)]
                k -= 1
            else:
                j += 1

    def find_medium(self, nums, start, end, k):
        if start == end:
            return nums[start]
        i, j = start, end
        pivot = nums[(i + j) / 2]
        while i <= j:
            while i <= j and nums[i] < pivot:
                i += 1
            while i <= j and nums[j] > pivot:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        if start + k - 1 <= j:
            return self.find_medium(nums, start, j, k)
        if start + k - 1 >= i:
            return self.find_medium(nums, i, end, k - (i - start))
        return nums[j + 1]
