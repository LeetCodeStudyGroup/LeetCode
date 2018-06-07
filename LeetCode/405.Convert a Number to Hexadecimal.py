class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return '0'
        self.chr_table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        is_neg = False
        if num < 0:
            num, is_neg = 0 - num - 1, True
        nums = []
        while num > 0:
            nums.append(num % 16)
            num /= 16
        return self.convert(nums, is_neg)

    def convert(self, nums, is_neg):
        rst = 'f' * (8 - len(nums)) if is_neg else ""
        for i in range(len(nums) - 1, -1, -1):
            inx = 15 - nums[i] if is_neg else nums[i]
            rst += self.chr_table[inx]
        return rst
