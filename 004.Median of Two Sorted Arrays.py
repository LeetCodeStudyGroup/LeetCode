class Solution(object):
    # O(log (m+n))
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        size = len(nums1) + len(nums2)
        count = size / 2
        isOdd = (size % 2) == 1
        if not isOdd:
            count -= 1

        if isOdd:
            if len(nums1) == 0:
                return nums2[count]
            if len(nums2) == 0:
                return nums1[count]
            if count >= len(nums2) and nums2[-1] <= nums1[count - len(nums2)]:
                return nums1[count - len(nums2)]
            if count >= len(nums1) and nums1[-1] <= nums2[count - len(nums1)]:
                return nums2[count - len(nums1)]
        else:
            if len(nums1) == 0:
                return (nums2[count] + nums2[count + 1]) / 2.0
            if len(nums2) == 0:
                return (nums1[count] + nums1[count + 1]) / 2.0
            if count >= len(nums2) and nums2[-1] <= nums1[count - len(nums2)]:
                return (nums1[count - len(nums2)] + nums1[count - len(nums2) + 1]) / 2.0
            if count >= len(nums1) and nums1[-1] <= nums2[count - len(nums1)]:
                return (nums2[count - len(nums1)] + nums2[count - len(nums1) + 1]) / 2.0

        i = j = 0
        while count > 1:
            target = count / 2
            if i + target >= len(nums1):
                j += target
            elif j + target >= len(nums2):
                i += target
            else:
                if nums1[i + target] < nums2[j + target]:
                    i += target
                else:
                    j += target
            count -= target

        if count == 1:
            if nums1[i] < nums2[j]:
                i += 1
            else:
                j +=1

        if isOdd:
            if nums1[i] > nums2[j]:
                return nums2[j]
            else:
                return nums1[i]
        else:
            result = nums1[i] + nums2[j]
            if i + 1 < len(nums1):
                result = min(result, nums1[i] + nums1[i + 1])
            if j + 1 < len(nums2):
                result = min(result, nums2[j] + nums2[j + 1])
            return result / 2.0

    # O(m + n)
    def findMedianSortedArrays2(self, nums1, nums2):
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
