# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1): return 1
        if not isBadVersion(n): return -1
        start, end = 1, n
        while start < end:
            mid = (start + end) / 2
            mid_result = isBadVersion(mid)
            next_result = isBadVersion(mid + 1)
            if not mid_result and next_result:
                return mid + 1
            elif mid_result:
                end = mid
            else:
                start = mid + 1
        return -1
