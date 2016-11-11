class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & (set(nums2)))

    def intersection2(self, nums1, nums2):
        record = set(nums1)
        result = set()
        for num in nums2:
            if num in record:
                result.add(num)
        return list(result)
