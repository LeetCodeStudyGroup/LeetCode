class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ary = []
        for i, num in enumerate(nums):
            ary.append((num, i))
        ary.sort()
        ary.reverse()

        rst = [''] * len(nums)
        for i in range(len(ary)):
            if i == 0:
                rst[ary[i][1]] = 'Gold Medal'
            elif i == 1:
                rst[ary[i][1]] = 'Silver Medal'
            elif i == 2:
                rst[ary[i][1]] = 'Bronze Medal'
            else:
                rst[ary[i][1]] = str(i + 1)
        return rst
