class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        nums = sorted([time[0], time[1], time[3], time[4]])
        nextnum = {}
        for i in range(len(nums)):
            if i + 1 < len(nums):
                nextnum[nums[i]] = nums[i + 1]
            else:
                nextnum[nums[i]] = -1

        limit, i = '9', 4
        if nextnum[time[i]] != -1 and nextnum[time[i]] <= limit:
            return time[:i] + nextnum[time[i]]
        limit, i = '5', 3
        if nextnum[time[i]] != -1 and nextnum[time[i]] <= limit:
            return time[:i] + nextnum[time[i]] + nums[0]

        limit, i = '4' if time[0] == '2' else '9', 1
        if nextnum[time[i]] != -1 and nextnum[time[i]] <= limit:
            return time[:i] + nextnum[time[i]] + ':' + nums[0] * 2
        limit, i = '1' if time[1] >= '4' else '2', 0
        if nextnum[time[i]] != -1 and nextnum[time[i]] <= limit:
                return val + nums[0] + ':' + nums[0] * 2

        return nums[0] * 2 + ':' + nums[0] * 2
