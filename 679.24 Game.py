class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.helper([float(num) for num in nums])

    def helper(self, nums):
        if len(nums) == 1:
            return abs(nums[0] - 24.0) <= 0.00001
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                nxt = self.create(nums[i], nums[j])
                tmp = nums[:]
                tmp.remove(nums[i])
                tmp.remove(nums[j])
                for n in nxt:
                    tmp.append(n)
                    if self.helper(tmp):
                        return True
                    tmp.pop()
        return False

    def create(self, a, b):
        rst = [a + b, a - b, b - a, a * b]
        if b > 0:
            rst.append(a / b)
        if a > 0:
            rst.append(b / a)
        return rst
