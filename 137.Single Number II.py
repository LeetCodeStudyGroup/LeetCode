class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        one = two = 0
        for num in nums:
            one = one ^ num & ~two
            two = two ^ num & ~one
        return one

    def singleNumber2(self, nums):
        result = 0
        for i in range(32):
            count = 0
            for num in nums:
                count += (num >> i) & 1
            if i == 31:
                if count % 3 == 1:
                    result = -(0x7fffffff - result + 1)
            else:
                result |= (count % 3) << i
        return result
