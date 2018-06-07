class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        diff = 0
        for num in nums:
            diff ^= num
        diff &= -diff  #find last '1' bit
        result = [0, 0]
        for num in nums:
            if diff & num:
                result[0] ^= num
            else:
                result[1] ^= num
        return result
