class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        i = self.binary_search(arr, x, 0, len(arr) - 1)
        j = i + 1
        i -= 1
        for _ in range(k):
            if j >= len(arr) or abs(arr[i] - x) <= abs(arr[j] - x):
                i -= 1
            else:
                j += 1
        return arr[i + 1:j]

    def binary_search(self, ary, target, start, end):
        while start + 1 < end:
            mid = start + (end - start) / 2
            if ary[mid] == target:
                return mid
            elif ary[mid] < target and ary[mid + 1] > target:
                if abs(target - ary[mid]) < abs(target - ary[mid - 1]):
                    return mid
                else:
                    return mid + 1
            elif ary[mid] < target:
                start = mid
            else:
                end = mid
        if abs(target - ary[end]) < abs(target - ary[start]):
            return end
        return start
