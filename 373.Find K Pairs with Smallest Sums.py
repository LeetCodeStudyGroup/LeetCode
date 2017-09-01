from heapq import *
import sys

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if len(nums1) == 0 or len(nums2) == 0:
            return []

        rst, h = [], [(nums1[0] + nums2[0], 0, 0)]
        while len(h) > 0 and len(rst) < k:
            val, i, j = heappop(h)
            rst.append([nums1[i], nums2[j]])
            heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))
            if j == 0:
                heappush(h, (nums1[i + 1] + nums2[j], i + 1, j))
        return rst
from heapq import *
import sys

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if len(nums1) == 0 or len(nums2) == 0:
            return []

        rst, h = [], [(nums1[0] + nums2[0], 0, 0)]
        while len(h) > 0 and len(rst) < k:
            val, i, j = heappop(h)
            rst.append([nums1[i], nums2[j]])
            heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))
            if j == 0:
                heappush(h, (nums1[i + 1] + nums2[j], i + 1, j))
        return rst
from heapq import *
import sys

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if len(nums1) == 0 or len(nums2) == 0:
            return []

        rst, h = [], [(nums1[0] + nums2[0], 0, 0)]
        while len(h) > 0 and len(rst) < k:
            val, i, j = heappop(h)
            rst.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))
            if j == 0 and i + 1 < len(nums1):
                heappush(h, (nums1[i + 1] + nums2[j], i + 1, j))
        return rst

    def kSmallestPairs2(self, nums1, nums2, k):
        if len(nums1) == 0 or len(nums2) == 0:
            return []

        rst, h = [], []
        for i in range(len(nums1)):
            for n2 in nums2:
                heappush(h, (nums1[i] + n2, [nums1[i], n2]))
            next_val = sys.maxint
            if i + 1 < len(nums1):
                next_val = nums1[i + 1] + nums2[0]
            while len(h) > 0 and h[0][0] < next_val:
                rst.append(heappop(h)[1])
                k -= 1
                if k == 0:
                    return rst
        return rst
from heapq import *
import sys

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if len(nums1) == 0 or len(nums2) == 0:
            return []

        rst, h = [], [(nums1[0] + nums2[0], 0, 0)]
        while len(h) > 0 and len(rst) < k:
            val, i, j = heappop(h)
            rst.append([nums1[i], nums2[j]])
            heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))
            if j == 0:
                heappush(h, (nums1[i + 1] + nums2[j], i + 1, j))
        return rst
from heapq import *
import sys

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if len(nums1) == 0 or len(nums2) == 0:
            return []

        rst, h = [], [(nums1[0] + nums2[0], 0, 0)]
        while len(h) > 0 and len(rst) < k:
            val, i, j = heappop(h)
            rst.append([nums1[i], nums2[j]])
            heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))
            if j == 0:
                heappush(h, (nums1[i + 1] + nums2[j], i + 1, j))
        return rst
from heapq import *
import sys

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if len(nums1) == 0 or len(nums2) == 0:
            return []

        rst, h = [], [(nums1[0] + nums2[0], 0, 0)]
        while len(h) > 0 and len(rst) < k:
            val, i, j = heappop(h)
            rst.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))
            if j == 0 and i + 1 < len(nums1):
                heappush(h, (nums1[i + 1] + nums2[j], i + 1, j))
        return rst

    def kSmallestPairs2(self, nums1, nums2, k):
        if len(nums1) == 0 or len(nums2) == 0:
            return []

        rst, h = [], []
        for i in range(len(nums1)):
            for n2 in nums2:
                heappush(h, (nums1[i] + n2, [nums1[i], n2]))
            next_val = sys.maxint
            if i + 1 < len(nums1):
                next_val = nums1[i + 1] + nums2[0]
            while len(h) > 0 and h[0][0] < next_val:
                rst.append(heappop(h)[1])
                k -= 1
                if k == 0:
                    return rst
        return rst
