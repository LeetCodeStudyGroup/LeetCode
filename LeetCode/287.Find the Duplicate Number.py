class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = nums[0], nums[nums[0]]
        while fast != slow:
            slow, fast = nums[slow], nums[nums[fast]]
        fast = 0
        while fast != slow:
            slow, fast = nums[slow], nums[fast]
        return slow

    def findDuplicate2(self, nums):
        start, end = 0, len(nums) - 1
        while start < end:
            mid = start + (end - start) / 2
            count = 0
            for num in nums:
                if num < mid:
                    count += 1
            if count <= mid:
                start = mid + 1
            else:
                end = mid
        return start
