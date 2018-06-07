class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        result = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i = self.binary_search(nums1, i + 1, len(nums1) - 1, nums2[j])
            else:
                j = self.binary_search(nums2, j + 1, len(nums2) - 1, nums1[i])
        return result

    def binary_search(self, nums, start, end, target):
        if start >= end or nums[start] > target:
            return start
        elif nums[end] < target:
            return end + 1

        mid = (start + end) / 2
        if nums[mid] < target and nums[mid + 1] >= target:
            return mid + 1
        elif nums[mid] < target:
            return self.binary_search(nums, mid + 1, end, target)
        else:
            return self.binary_search(nums, start, mid, target)

    def intersect2(self, nums1, nums2):
        record = {}
        for num in nums1:
            if num in record:
                record[num] += 1
            else:
                record[num] = 1
        result = []
        for num in nums2:
            if num in record and record[num] > 0:
                result.append(num)
                record[num] -= 1
        return result
