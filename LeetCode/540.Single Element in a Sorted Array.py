class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start + 2 < end:
            mid = start + (end - start) / 2
            if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
                return nums[mid]
            elif nums[mid] == nums[mid + 1]:
                if (mid - start) % 2 == 0:
                    start = mid
                else:
                    end = mid + 1
            else:
                if (mid - start + 1) % 2 == 0:
                    start = mid + 1
                else:
                    end = mid
        if start + 2 < len(nums) and nums[start] == nums[start + 1]:
            return nums[start + 2]
        return nums[start]
