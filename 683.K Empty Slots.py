from collections import deque
import sys

class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        ary = [0] * len(flowers)
        for i, slot in enumerate(flowers):
            ary[slot - 1] = i + 1

        min_day = sys.maxint
        i, left, right = 0, 0, k + 1
        while i < len(ary) and right < len(ary):
            if ary[i] < ary[left] or ary[i] <= ary[right]:
                if i == right:
                    min_day = min(min_day, max(ary[left], ary[right]))
                left, right = i, k + 1 + i
            i += 1

        return min_day if min_day < sys.maxint else -1

    def kEmptySlots2(self, flowers, k):
        if k >= len(flowers) - 1:
            return -1

        ary = [0] * len(flowers)
        for i, slot in enumerate(flowers):
            ary[slot - 1] = i + 1

        q = deque()
        for i in range(1, k + 1):
            while len(q) > 0 and q[-1] > ary[i]:
                q.pop()
            q.append(ary[i])

        min_day = sys.maxint
        for i in range(k + 1, len(ary)):
            day = max(ary[i], ary[i - k - 1])
            if (len(q) == 0 or day < q[0]):
                min_day = min(min_day, day)

            if k > 0:
                if len(q) > 0 and q[0] == ary[i - k]:
                    q.popleft()
                while len(q) > 0 and q[-1] > ary[i]:
                    q.pop()
                q.append(ary[i])

        return min_day if min_day < sys.maxint else -1
