class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        rst = [0] * len(nums)
        i, j = 0, len(nums) - 1
        inx = len(nums) - 1 if a >= 0 else 0
        while i <= j:
            fi, fj = self.f(nums[i], a, b, c), self.f(nums[j], a, b, c)
            if a >= 0:
                if fi >= fj:
                    rst[inx] = fi
                    i += 1
                else:
                    rst[inx] = fj
                    j -= 1
                inx -= 1
            else:
                if fi <= fj:
                    rst[inx] = fi
                    i += 1
                else:
                    rst[inx] = fj
                    j -= 1
                inx += 1
        return rst

    def f(self, num, a, b, c):
        return a * num * num + b * num + c
