class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.quick_select(nums, 0, len(nums) - 1, k - 1)
        return self.heap_sort(nums, k)

    def quick_select(self, nums, left, right, k):
        if left == right:
            return nums[left]
        pivot = self.partition(nums, left, right, (left + right) / 2)
        if pivot == k:
            return nums[k]
        elif pivot > k:
            return self.quick_select(nums, left, pivot - 1, k)
        else:
            return self.quick_select(nums, pivot + 1, right, k)

    def partition(self, nums, left, right, pivot):
        nums[pivot], nums[right] = nums[right], nums[pivot]
        inx = left
        for i in range(left, right):
            if nums[i] > nums[right]:
                nums[inx], nums[i] = nums[i], nums[inx]
                inx += 1
        nums[inx], nums[right] = nums[right], nums[inx]
        return inx
        
    def heap_sort(self, nums, k):
        for i in range(len(nums) / 2 - 1, -1, -1):
	        self.max_heapify(nums, i, len(nums))
        for i in range(len(nums) - 1, len(nums) - k, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.max_heapify(nums, 0, i)
        return nums[0]

    def max_heapify(self, nums, inx, length):
        left, right = inx * 2 + 1, inx * 2 + 2
        max_inx = inx
        if right < length and nums[max_inx] < nums[right]:
            max_inx = right
        if left < length and nums[max_inx] < nums[left]:
            max_inx = left
        if max_inx != inx:
            nums[inx], nums[max_inx] = nums[max_inx], nums[inx]
            self.max_heapify(nums, max_inx, length)

    def select_sort(self, nums, k):
        for i in range(k):
            inx = reduce(lambda x, y: x if nums[x] > nums[y] else y, range(len(nums) - i))
            nums[inx], nums[len(nums) - i - 1] = nums[len(nums) - i - 1], nums[inx]
        return nums[-k]
