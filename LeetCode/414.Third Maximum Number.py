class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 3
        max_val = []
        for num in nums:
            if num not in max_val:
                val = num
                for i in range(k):
                    if len(max_val) > i and val > max_val[i]:
                        max_val[i], val = val, max_val[i]
                if len(max_val) < k:
                    max_val.append(val)
        return max_val[2] if len(max_val) == k else max_val[0]

    def thirdMax2(self, nums):
        if len(nums) == 0: return 0
        self.init_heap(nums)
        max, k, i = nums[0], 2, 0
        while i < k and i < len(nums):
            last = len(nums) - i - 1
            nums[0], nums[last] = nums[last], nums[0]
            self.heapify(nums, 0, last)
            if nums[0] == nums[last] or nums[0] == max:
                k += 1
            i += 1
        return nums[0] if i != len(nums) else max

    def init_heap(self, nums):
        base = 1
        while base * 2 < len(nums):
            base *= 2
        while base > 0:
            for i in range(base - 1, base * 2 - 1):
                self.heapify(nums, i, len(nums))
            base /= 2
        self.heapify(nums, 0, len(nums))

    def heapify(self, nums, root, size):
        left, right = root * 2 + 1, root * 2 + 2
        inx = root
        if left < size and nums[inx] < nums[left]:
            inx = left
        if right < size and nums[inx] < nums[right]:
            inx = right
        if inx != root:
            nums[inx], nums[root] = nums[root], nums[inx]
            self.heapify(nums, inx, size)
