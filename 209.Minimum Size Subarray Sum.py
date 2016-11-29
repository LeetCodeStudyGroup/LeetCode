class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i = j = val = cnt = 0
        min_len = len(nums) + 1
        while j < len(nums):
            if val < s:
                if i == len(nums):
                    break
                i, cnt, val = i + 1, cnt + 1, val + nums[i]
            else:
                j, cnt, val = j + 1, cnt - 1, val - nums[j]
            if val >= s and cnt < min_len:
                min_len = cnt
        return min_len if j != 0 else 0

class Solution2(object):
    def minSubArrayLen(self, s, nums):
        min_len, sums, val = len(nums), [], 0
        for num in nums:
            val += num
            sums.append(val)
        if len(nums) == 0 or sums[-1] < s:
            return 0
        for i in range(len(nums)):
            j = self.findWindowEnd(i, sums, s)
            if j == len(nums):
                break
            min_len = min(j - i + 1, min_len)
        return min_len
    
    def findWindowEnd(self, start, sums, s):
        i, j = start, len(sums) - 1
        offset = 0 if start == 0 else sums[start - 1]
        while i <= j:
            m = (i + j) / 2
            if (sums[m] - offset >= s):
                j = m - 1
            else:
                i = m + 1
        return i
