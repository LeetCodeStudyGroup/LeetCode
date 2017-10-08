from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        rst, q = [], deque()
        for i, num in enumerate(nums):
            while len(q) > 0 and q[0] < i - k + 1:
                q.popleft()
            while len(q) > 0 and nums[q[-1]] < num:
                q.pop()
            q.append(i)
            if (i >= k - 1):
                rst.append(nums[q[0]])
        return rst
