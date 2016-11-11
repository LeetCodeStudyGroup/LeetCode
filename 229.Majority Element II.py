class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val1 = val2 = None
        cnt1 = cnt2 = 0
        for num in nums:
            if val1 == num:
                cnt1 += 1
            elif val2 == num:
                cnt2 += 1
            elif cnt1 == 0:
                val1, cnt1 = num, 1
            elif cnt2 == 0:
                val2, cnt2 = num, 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        result = []
        if nums.count(val1) > len(nums) / 3:
            result.append(val1)
        if nums.count(val2) > len(nums) / 3:
            result.append(val2)
        return result
