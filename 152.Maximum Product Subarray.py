class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        product = 1
        max_product = last_pos = first_neg = None
        for num in nums:
            if num != 0:
                product *= num
                if product > 0:
                    last_pos = product
                local_max = max(num, product)
                if first_neg and last_pos:
                    local_max = max(local_max, max(last_pos, product / first_neg))
                elif first_neg:
                    local_max = max(local_max, product / first_neg)
                if max_product == None or local_max > max_product:
                    max_product = local_max
                if first_neg == None and product < 0:
                    first_neg = product
            else:
                if max_product == None or max_product < 0:
                    max_product = 0
                last_pos = first_neg = None
                product = 1
        return max_product
