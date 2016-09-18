class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        size = len(nums1) + len(nums2)
        if size == 0:
            return 0
        elif size == 1:
            if len(nums1) == 0:
                return nums2[0]
            else:
                return nums1[0]


        mid_inx = size / 2
        first = second = last = None
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                last = nums2[j]
                j += 1
            else:
                last = nums1[i]
                i += 1
 
            if i + j == mid_inx:
                first = last
            elif i + j == mid_inx + 1:
                second = last
                break

        if j < len(nums2) and i == len(nums1):
            while j < len(nums2):
                last = nums2[j]
                j += 1
                if i + j == mid_inx:
                    first = last
                elif i + j == mid_inx + 1:
                    second = last
                    break

        elif i < len(nums1) and j == len(nums2):
            while i < len(nums1):
                last = nums1[i]
                i += 1
                if i + j == mid_inx:
                    first = last
                elif i + j == mid_inx + 1:
                    second = last
                    break

        if size % 2 == 0:
            return float(first + second) / 2
        else:
            return second
