class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rst = []
        for i in range(len(nums)):
            inx = abs(nums[i]) - 1
            if nums[inx] < 0:
                rst.append(inx + 1)
            else:
                nums[inx] = -nums[inx]
        return rst

    def findDuplicates2(self, nums):
        rst = set()
        for i in range(len(nums)):
            if nums[i] == i + 1 or nums[i] == -1:
                continue
            inx = nums[i] - 1
            nums[i] =  -1
            while nums[inx] != inx + 1 and nums[inx] != -1:
                nums[inx], inx = inx + 1, nums[inx] - 1
            if nums[inx] == -1:
                nums[inx] = inx + 1
            else:
                rst.add(inx + 1)
        return list(rst)
