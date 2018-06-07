class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 00 -> 10 -> 11 -> 00
        one = two = 0
        for num in nums:
            two = two ^ (num & one)
            one = one ^ (num & ~two)
        return one & ~two

    def singleNumber2(self, nums):
        one = two = 0
        for num in nums:
            one = one ^ num & ~two
            two = two ^ num & ~one
        return one

    def singleNumber3(self, nums):
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
